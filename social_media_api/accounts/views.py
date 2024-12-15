from rest_framework import status, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.exceptions import PermissionDenied

User = get_user_model()

# Follow a user
@api_view(['POST'])
def follow_user(request, user_id):
    try:
        user_to_follow = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    # Ensure the user can't follow themselves
    if user_to_follow == request.user:
        raise PermissionDenied("You cannot follow yourself.")

    # Add the user to the 'following' list
    request.user.following.add(user_to_follow)
    return Response({"detail": f"You are now following {user_to_follow.username}"}, status=status.HTTP_200_OK)

# Unfollow a user
@api_view(['POST'])
def unfollow_user(request, user_id):
    try:
        user_to_unfollow = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    # Ensure the user can't unfollow themselves
    if user_to_unfollow == request.user:
        raise PermissionDenied("You cannot unfollow yourself.")

    # Remove the user from the 'following' list
    request.user.following.remove(user_to_unfollow)
    return Response({"detail": f"You have unfollowed {user_to_unfollow.username}"}, status=status.HTTP_200_OK)
