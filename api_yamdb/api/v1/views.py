from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet

from api.v1.serializers import GenreSerializer
from reviews.models import Genre

User = get_user_model()


class GenreViewSet(ModelViewSet):
    lookup_field = 'slug'
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    search_fields = ['=name', ]
