from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterSerializer, LoginSerializer

# Register View
class RegisterView(APIView):
    def post(self, request):
        # Use RegisterSerializer to validate and save the new user
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user, token = serializer.save()  # Save the user and get the token

            # Return the token in the response
            return Response({"token": token.key}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Login View
class LoginView(APIView):
    def post(self, request):
        # Use LoginSerializer to authenticate the user
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data  # Validated user object
            token, created = Token.objects.get_or_create(user=user)  # Get or create a token for the user

            return Response({"token": token.key})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
