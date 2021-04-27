from rest_framework.response import Response
from django.db import models
from rest_framework import viewsets, renderers, permissions, status
from rest_framework.decorators import action
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import generics, mixins
from .service import *
from django_filters.rest_framework import DjangoFilterBackend
from .api import *

from .models import Movie, Genre, Actor
from .serializers import MovieListSerializer, MovieDetailSerializer, ReviewCreateSerializers, CreateRatingSerializer, \
    ActorListSerializer, ActorDetailSerializer


class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    filter_backends = (DjangoFilterBackend,)
    filterset_class = MovieFilter
    pagination_class = PaginatorMovies
    serializer_action_class = {'list':MovieListSerializer,'retrieve':MovieDetailSerializer}

    def get_queryset(self):
        movies = Movie.objects.filter(draft=False).annotate(
            rating_user=models.Count('ratings', filter=models.Q(ratings__ip=get_client_ip(self.request)))).annotate(
            middle_star=models.Sum(models.F('ratings__star')) / models.Count(models.F('ratings')))
        return movies

    def get_serializer_class(self):
        return self.serializer_action_class[self.action]
        # if self.action == 'list':
        #     return MovieListSerializer
        # elif self.action == 'retrieve':
        #     return MovieDetailSerializer


class ActorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Actor.objects.all()
    serializer_action_class = {'list': ActorListSerializer, 'retrieve': ActorDetailSerializer}
    def get_serializer_class(self):
        return self.serializer_action_class[self.action]


class ReviewCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = ReviewCreateSerializers


class AddStarRatingViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = CreateRatingSerializer

    def perform_create(self, serializer):
        serializer.save(ip=get_client_ip(self.request))

# class Logout(APIView):
#     def get(self,request,format=None):
#         request.user.auth_token.delete()
#         return Response(status=status.HTTP_200_OK)


# class MovieListView(generics.ListAPIView):
#     serializer_class = MovieListSerializer
#     filter_backends = (DjangoFilterBackend,)
#     filterset_class = MovieFilter
#
#     def get_queryset(self):
#         movies = Movie.objects.filter(draft=False).annotate(
#             rating_user=models.Count('ratings', filter=models.Q(ratings__ip=get_client_ip(self.request)))).annotate(
#             middle_star=models.Sum(models.F('ratings__star')) / models.Count(models.F('ratings')))
#         return movies

# class MovieDetailView(generics.RetrieveAPIView):
#     serializer_class = MovieDetailSerializer
#     queryset = Movie.objects.filter(draft=False)

# class ActorsListView(generics.ListAPIView):
#     queryset = Actor.objects.all()
#     serializer_class = ActorListSerializer

# class ActorsDetailView(generics.RetrieveAPIView):
#     queryset = Actor.objects.all()
#     serializer_class = ActorDetailSerializer

# class ReviewCreateView(generics.CreateAPIView):
#     serializer_class = ReviewCreateSerializers

# class AddStarRating(generics.CreateAPIView):
#     serializer_class = CreateRatingSerializer
#
#     def perform_create(self, serializer):
#         serializer.save(ip=get_client_ip(self.request))
