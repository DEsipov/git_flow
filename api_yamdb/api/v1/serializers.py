from django.contrib.auth import get_user_model
from rest_framework import serializers

from reviews.models import Genre

User = get_user_model()


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ('id',)
        model = Genre


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'role', 'email', 'first_name', 'last_name', 'bio')
