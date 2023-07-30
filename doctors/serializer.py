from rest_framework import serializers
from .models import Doctor, Practice, Rating
from django.contrib.auth.models import User
from users.utils import get_image
from users.serializer import UserSerializer

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = []

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = UserSerializer(instance.user).data
        representation['doctorInfo'] = {
            'occupation' : instance.occupation,
            'qualification' : instance.qualification,
            'practices' : PracticeSerializer(instance.practices, many=True).data,
            'rating' : self.get_rating(instance)
        }

        return representation
    
    def get_rating(self, instance):
        ratings = Rating.objects.filter(user=instance)
        total = 0
        for i in ratings:
            total += i.rating

        return total
    


class PracticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Practice
        fields = []

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        representation['location'] = instance.location

        return representation