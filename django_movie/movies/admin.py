from django.contrib import admin

from django.utils.safestring import mark_safe
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'url')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')



class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'url')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')


class MovieAdmin(admin.ModelAdmin):
    list_display = (
    'id', 'title', 'tagline', 'description', 'poster', 'year', 'country', 'world_premiere', 'budget', 'fees_in_usa',
    'category', 'url', 'draft')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title','category__name')
    list_editable =('draft',)
    list_filter=('year','title')


class MovieShotsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'movie', 'image')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')
    list_filter = ('title','movie')


class ActorAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'age', 'description','get_image')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')
    list_filter = ('name',)
    readonly_fields=('get_image',)

    def get_image(self,obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description="Изображение"


class RatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'star', 'movie')
    list_display_links = ('id', 'star')
    search_fields = ('id', 'movie')


class RatingStarAdmin(admin.ModelAdmin):
    list_display = ('id', 'value')
    list_display_links = ('id', 'value')
    search_fields = ('id',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'name', 'text', 'parent', 'movie')
    list_display_links = ('id', 'email')
    search_fields = ('id', 'name')
    # readonly_fields=('name','email')



admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(MovieShots, MovieShotsAdmin)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(RatingStar, RatingStarAdmin)
admin.site.register(Review, ReviewAdmin)


