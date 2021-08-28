from rest_framework import  serializers
from .models import User
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'profile_image', 'cover_image', 'first_name', 'last_name', 'username', 'birthday', 'email', 'about', 'profession', 'address', 'country', 'city', 'postal_code', 'phone', 'skills', 'facebook_link', 'twitter_link', 'instagram_link', 'linkedin_link')

    

class UserSerializer2(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'profile_image', 'cover_image', 'first_name', 'last_name', 'username', 'birthday', 'email', 'about', 'profession', 'address', 'country', 'city', 'postal_code', 'phone', 'skills', 'facebook_link', 'twitter_link', 'instagram_link', 'linkedin_link', 'password')
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user