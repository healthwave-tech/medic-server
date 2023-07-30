from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from users.serializer import UserDataSerializer
from django.contrib.auth import authenticate
from users.utils import decode_jwt
from .models import Appointment
from .serializer import AppointmentSerializer
from doctors.models import Doctor

# Create your views here.

@api_view(['POST'])
def get_user_appointments(request):
    decrypted_jwt = decode_jwt(request.META.get("HTTP_AUTHORIZATION").split(" ")[1])
    user = User.objects.get(username=decrypted_jwt['username'])


    appointments = Appointment.objects.all()

    serializer = AppointmentSerializer(appointments, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def set_appointment(request):
    decrypted_jwt = decode_jwt(request.META.get("HTTP_AUTHORIZATION").split(" ")[1])
    user = User.objects.get(username=decrypted_jwt['username'])

    date = request.data.get('date')
    time = request.data.get('time')
    doc_id = request.data.get('doc_id')

    doc = Doctor.objects.get(id=doc_id)

    payload = {
        'user' : user,
        'doctor' : doc,
        'date' : date,
    }


    appointment = Appointment.objects.create(**payload)

    # serializer = AppointmentSerializer(appointments, many=True)

    return Response({'status':'Appointment Book'}, status=status.HTTP_200_OK)