from rest_framework import serializers
from .models import Appointment
from django.contrib.auth.models import User
from users.utils import get_image
from users.serializer import UserSerializer
from doctors.serializer import DoctorSerializer

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = []

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['doctor'] =  DoctorSerializer(instance.doctor).data
        representation['date'] = instance.date
        representation['notes'] = instance.notes
        return representation 