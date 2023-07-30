from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from users.utils import decode_jwt
from doctors.models import Doctor
from doctors.serializer import DoctorSerializer
from django.db.models import Q


# Create your views here.

@api_view(["POST"])
def get_doctors(request):
    # ensure user is authenticated
    decrypted_jwt = decode_jwt(request.META.get("HTTP_AUTHORIZATION").split(" ")[1])

    doctors = Doctor.objects.all()


    serializer = DoctorSerializer(doctors, many=True).data

    return Response({'status':'success', 'data':serializer}, status=status.HTTP_200_OK)

@api_view(['POST'])
def search_doctor(request):
     # ensure user is authenticated
    decrypted_jwt = decode_jwt(request.META.get("HTTP_AUTHORIZATION").split(" ")[1])
    serializer = []
    name = request.data.get('name').lower()
    users = User.objects.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))

    print(users)
    doctors = []

    for user in users:
        try:
            instance = Doctor.objects.get(user=user)
            doctors.append(instance)
        except Exception as e:
            print(e)
    
    serializer = DoctorSerializer(doctors, many=True).data

    return Response({'status':'success', 'data':serializer}, status=status.HTTP_200_OK)
