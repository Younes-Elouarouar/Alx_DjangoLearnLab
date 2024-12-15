from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth import get_user_model

# Post Serializer
class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(queryset=get_user_model().objects.all(), slug_field='username')

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'created_at', 'updated_at']

# Comment Serializer
class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(queryset=get_user_model().objects.all(), slug_field='username')
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())

    class Meta:
        model = Comment
        fields = ['id', 'author', 'post', 'content', 'created_at', 'updated_at']
