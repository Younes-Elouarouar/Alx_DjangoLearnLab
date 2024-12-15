from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from rest_framework.authtoken.models import Token  # Import Token model

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()  # Use the custom user model
        fields = ('id', 'username', 'email', 'bio', 'profile_picture', 'followers')

# Registration Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()  # Use the custom user model
        fields = ('username', 'email', 'password')  # Include password for registration

    def create(self, validated_data):
        # Create the user using the custom user model
        user = get_user_model().objects.create_user(**validated_data)  # This will hash the password
        return user

# Login Serializer
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        # Authenticate the user with the provided username and password
        user = authenticate(username=data['username'], password=data['password'])
        if user is None:
            raise serializers.ValidationError("Invalid credentials")
        return user
