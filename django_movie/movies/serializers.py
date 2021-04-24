from rest_framework import serializers

from .models import *


class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, value):
        serializer=ReviewSerializer(value,context=self.context)
        """тоже самое что и ниже"""
        # serializer=self.parent.parent.__class__(value,context=self.context)
        return serializer.data



class MovieListSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    rating_user=serializers.BooleanField()
    middle_star=serializers.IntegerField()


    class Meta:
        model=Movie
        fields=('id','title','tagline','category','rating_user','middle_star')




class ReviewCreateSerializers(serializers.ModelSerializer):

    class Meta:
        model=Review
        fields='__all__'


class FilterReviewListSerializer(serializers.ListSerializer):
    def to_representation(self,data):
        data=data.filter(parent=None)
        return super().to_representation(data)


class ReviewSerializer(serializers.ModelSerializer):
    children=RecursiveSerializer(many=True)
    class Meta:
        list_serializer_class=FilterReviewListSerializer
        model=Review
        fields=('name','text','children')


class ActorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Actor
        fields='__all__'

class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Actor
        fields=('id','name','image')


class MovieDetailSerializer(serializers.ModelSerializer):
    """Сериализуем поля для того чтобы вместо id выводились имена"""
    category=serializers.SlugRelatedField(slug_field='name',read_only=True)
    directors=ActorListSerializer(read_only=True,many=True)
    actors=ActorListSerializer(read_only=True,many=True)
    genres= serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    reviews=ReviewSerializer(many=True)

    """указываем reviews потому что в related_name так указано"""
    class Meta:
        model=Movie
        exclude=('draft',)


class CreateRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Rating
        fields=('star','movie')

    def create(self, validated_data):
        rating,_=Rating.objects.update_or_create(
            ip=validated_data.get('ip',None),
            movie=validated_data.get('movie',None),
            defaults={'star':validated_data.get('star')}
        )
        return rating

