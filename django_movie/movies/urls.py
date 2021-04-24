from django.urls import path
from. import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView,
)


# urlpatterns=[
#     path('movie/',views.MovieListView.as_view()),
#     path('movie/<int:pk>/',views.MovieDetailView.as_view()),
#     path('review/',views.ReviewCreateView.as_view()),
#     path('actors/',views.ActorsListView.as_view()),
#     path('actors/<int:pk>/',views.ActorsDetailView.as_view()),
#     path('rating/',views.AddStarRating.as_view()),
# ]

"""URL для ViewSet"""
urlpatterns=format_suffix_patterns([
    path('movie/',views.MovieViewSet.as_view(actions={'get':'list'})),
    path('movie/<int:pk>/',views.MovieViewSet.as_view(actions={'get':'retrieve'})),
    path('actors/',views.ActorViewSet.as_view(actions={'get':'list'})),
    path('actors/<int:pk>/',views.ActorViewSet.as_view(actions={'get':'retrieve'})),
    path('review/',views.ReviewCreateViewSet.as_view(actions={'post':'create'})),
    path('rating/',views.AddStarRatingViewSet.as_view(actions={'post':'create'})),
])

# router=DefaultRouter()
# router.register(r'actor-set',views.views.ActorViewSet,basename='actor')
# urlpatterns+=router.urls