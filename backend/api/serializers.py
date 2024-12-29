from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Movie
from .models import Review

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = [
            'id', 'title', 'year', 'imdb_id', 'genres',
            'director', 'last_updated', 'is_active'
        ]

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'user', 'movie', 'rating', 'comment', 'submit_date']