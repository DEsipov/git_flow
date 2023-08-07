from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.v1.views import GenreViewSet

v1_router = DefaultRouter()
v1_router.register('genres', GenreViewSet, basename='genres')

urlpatterns = [
    path('', include(v1_router.urls))
]
