from rest_framework import status, permissions, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.exceptions import PermissionDenied
from .models import User

# Get the custom user model
User = get_user_model()

# Function-Based Views for follow/unfollow

@api_view(['POST'])
def follow_user(request, user_id):
    try:
        user_to_follow = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    if user_to_follow == request.user:
        raise PermissionDenied("You cannot follow yourself.")

    request.user.following.add(user_to_follow)
    return Response({"detail": f"You are now following {user_to_follow.username}"}, status=status.HTTP_200_OK)


@api_view(['POST'])
def unfollow_user(request, user_id):
    try:
        user_to_unfollow = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    if user_to_unfollow == request.user:
        raise PermissionDenied("You cannot unfollow yourself.")

    request.user.following.remove(user_to_unfollow)
    return Response({"detail": f"You have unfollowed {user_to_unfollow.username}"}, status=status.HTTP_200_OK)

# Class-Based View for Feed (Optional Example wi
