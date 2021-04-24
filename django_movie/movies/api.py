# from rest_framework.response import Response
# from django.db import models
# from rest_framework import viewsets, renderers, permissions, status
# from rest_framework.decorators import action
# from rest_framework import generics
# from rest_framework.views import APIView
# from rest_framework import generics
# from .service import get_client_ip, MovieFilter
# from django_filters.rest_framework import DjangoFilterBackend
#
# from .models import Movie, Genre, Actor
# from .serializers import MovieListSerializer, MovieDetailSerializer, ReviewCreateSerializers, CreateRatingSerializer, \
#     ActorListSerializer, ActorDetailSerializer
#
# class ActorViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Actor.objects.all()
#     def get_serializer(self, *args, **kwargs):
#         if self.action=='list':
#             return ActorListSerializer
#         elif self.action=='retrieve':
#             return ActorDetailSerializer
