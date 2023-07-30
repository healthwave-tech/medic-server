from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from users.serializer import UserDataSerializer
from django.contrib.auth import authenticate

# Create your views here.

@api_view(['POST'])
def create_user(request):
    # Create a new user

    # treat email as unique username
    try:
        first_name = request.data['first_name'].strip()
        last_name = request.data['last_name'].strip()
        username = request.data['email'].lower().strip()
        password = request.data['password']
        user = User.objects.create(username=username,first_name=first_name,last_name=last_name)
        user.set_password(password)
        user.save()




    except Exception as e:
        # on failure handle gracefully
        # implement proper logging later
        print(e)

        return Response({'status':'error'},status=status.HTTP_400_BAD_REQUEST)
    
    serializer = UserDataSerializer(user)
        
    return Response({'status':'success', 'data':serializer.data}, status=status.HTTP_200_OK)

    
@api_view(['POST'])
def login_user(request):
    try:
        username = request.data.get('email').lower().strip()
        password = request.data.get('password')
        print(username, password)
        user = authenticate(request, username=username, password=password)

        if not user:
            return Response({'status':'unauthorized'},status=status.HTTP_401_UNAUTHORIZED)

    except Exception as e:
        # on failure handle gracefully
        # implement proper logging later
        print(e)

        return Response({'status':'error'},status=status.HTTP_400_BAD_REQUEST)
    
    serializer = UserDataSerializer(user)
        
    return Response({'status':'success', 'data':serializer.data}, status=status.HTTP_200_OK)
