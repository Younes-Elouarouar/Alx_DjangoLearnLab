from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Post
from django.contrib.auth import get_user_model
["viewsets", "viewsets.ModelViewSet", "Comment.objects.all()"]
["generics.get_object_or_404(Post, pk=pk)", "Like.objects.get_or_create(user=request.user, post=post)", "Notification.objects.create"]
User = get_user_model()
"Post.objects.filter(author__in=following_users).order_by"
# Feed view showing posts from users the current user follows
class FeedView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()  # Will be overridden in the `get_queryset`

    def get_queryset(self):
        user = self.request.user
        following = user.following.all()
        return Post.objects.filter(author__in=following).order_by('-created_at')
