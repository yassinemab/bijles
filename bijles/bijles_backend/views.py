from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import ProfileSerializer, UserSerializer

# Create your views here.


def hasPermission():
    pass


@api_view(["GET"])
def getAllUsers(request):
    users = Users.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addUser(request):
    # serializer = UserSerializer(data=request.data)
    profile_id = addProfile({"full_name": request.POST.get("full_name"),
                             "phone_number": request.POST.get("phone_number")})
    user = UserManager.createUser(
        request.email, request.password, profile_id, 2 if request.is_teacher else 1)

    return Response(user.data)


@api_view(['POST'])
def addProfile(request):
    serializer = ProfileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(serializer.data)
    else:
        raise ValueError(request.data)
    return Response(serializer.id)
