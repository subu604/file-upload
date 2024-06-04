# serializers.py
from rest_framework import serializers
from .models import FileRevision
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user



class FileRevisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileRevision
        fields = ('id', 'file', 'version', 'uploaded_at', 'filename', 'user')
        read_only_fields = ('user',)

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)