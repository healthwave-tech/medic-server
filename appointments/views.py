from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from users.serializer import UserDataSerializer
from django.contrib.auth import authenticate
from users.utils import decode_jwt
from .models import Appointment
from .serializer import AppointmentSerializer

# Create your views here.

@api_view(['POST'])
def get_user_appointments(request):
    decrypted_jwt = decode_jwt(request.META.get("HTTP_AUTHORIZATION").split(" ")[1])
    user = User.objects.get(username=decrypted_jwt['username'])


    appointments = Appointment.objects.filter(user=user)

    serializer = AppointmentSerializer(appointments, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)