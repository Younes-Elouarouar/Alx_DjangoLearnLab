from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from django.contrib.auth import get_user_model
"Post.objects.filter(author__in=following_users).order_by"
User = get_user_model()

class FeedViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        # Get posts from users the current user is following
        followed_users = request.user.following.all()
        posts = Post.objects.filter(author__in=followed_users).order_by('-created_at')

        # Serialize the posts
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
