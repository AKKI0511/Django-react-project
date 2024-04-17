from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

# serializer validates if the given data is valid for the given model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    # Create new user after serializer gives the validated_data
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data) # ** is used to make dict key: value as , seperated value
        return user
    
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "author"]
        extra_kwargs = {"author": {"read_only": True}}