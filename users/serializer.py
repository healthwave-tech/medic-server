from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User
from users.utils import get_image

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = []

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        representation['first_name'] = instance.first_name
        representation['last_name'] = instance.last_name
        representation['profilePicture'] = get_image(instance.profile.profile_picture.url) if instance.profile.profile_picture else None

        
        return representation
    
class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = []

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        representation['first_name'] = instance.first_name
        representation['last_name'] = instance.last_name
        representation['email'] = instance.username
        representation['phone_number'] = str(instance.profile.phone_number)
        representation['profilePicture'] = get_image(instance.profile.profile_picture.url) if instance.profile.profile_picture else None
        representation['gender'] = instance.profile.gender
        representation['jwt'] = instance.profile._generate_jwt_token()


        return representation