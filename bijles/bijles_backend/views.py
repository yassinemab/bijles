from xml.dom import NotFoundErr
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed, PermissionDenied
from .models import Users
from .models import Profiles
from .models.Roles import Roles as RolesModel
from .models.Requests import Requests as RequestsModel
from .models.Subjects import Subjects as SubjectsModel
from .models.RequestStatusses import RequestStatusses as RequestStatusModel
from .serializers import ProfileSerializer, UserSerializer, RequestsSerializer
import bcrypt
import jwt
import datetime
# Create your views here.


def hasPermission():
    pass


@api_view(["GET"])
def getAllUsers(request):
    users = Users.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


def getUser(request):
    token = request.COOKIES.get('jwt')
    if not token:
        raise AuthenticationFailed("Authentication failed.")

    try:
        payload = jwt.decode(token, ' $2a$12$Cyk/3gU.ErvVuhlzv16ULOFFEPytP934bMPWHMkH2J0pt0piZ0lMm ',
                             algorithm=['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed("Authentication failed.")

    user = Users.objects.filter(id=payload.get('id')).first()
    if not user:
        raise AuthenticationFailed("Authentication failed.")

    serializer = UserSerializer(user)
    return Response(serializer.data)


@api_view(['POST'])
def createRequest(request):
    user = getUser(request._request)
    user = Users.objects.filter(id=user.data["id"]).first()
    description = request.data["description"]
    subject = SubjectsModel.objects.filter(
        name=request.data["subject"]).first()
    if not subject:
        subject = SubjectsModel.objects.filter(name='Onbekend').first()
    requestStatusName = 'Concept' if request.data["concept"] else 'Published'
    requestStatus = RequestStatusModel.objects.filter(
        name=requestStatusName).first()
    jobRequest = RequestsModel.objects.create(
        student=user, description=description, subject=subject, request_status=requestStatus)

    return Response({'message': True})


@api_view(['GET'])
def getRequestById(request):
    jobRequest = RequestsModel.objects.filter(
        id=request.GET.get('id', '')).first()
    serializer = RequestsSerializer(jobRequest, many=False)
    return Response(serializer.data)

@api_view(["GET"])
def getOwnRequests(request):
    user = getUser(request._request)
    requests = RequestsModel.objects.filter(student_id=user.data["id"])
    serializer = RequestsSerializer(requests, many=True)
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteRequest(request):
    user = getUser(request._request)
    jobRequest = RequestsModel.objects.filter(id=request.data["id"], user_id=user.data["id"]).first()
    if not jobRequest:
        raise NotFoundErr("Request not found")
    jobRequest.delete()
    return Response({'message': True})


@api_view(["PUT"])
def updateRequest(request):
    jobRequest = RequestsModel.objects.filter(
        id=request.data["id"]).first()

    user = getUser(request._request)
    if not user or user != jobRequest.data["user"]:
        return PermissionDenied("No permissions to edit this")


    RequestStatus = RequestStatusModel.objects.filter(
        id=jobRequest.data["request_status"]).first()

    if RequestStatus.data["name"] != 'Concept':
        return PermissionDenied("Only concepts can be updated")

    subject = SubjectsModel.objects.filter(
        name=request.data["subject"]).first()
    if not subject:
        subject = SubjectsModel.objects.filter(name='Onbekend').first()

    RequestStatus = RequestStatusModel.objects.filter(name=request.data["request_status"]).first()
    if not RequestStatus:
        RequestStatus = RequestStatusModel.objects.filter(name="Onbekend").first()
    updatedRequest = RequestsModel(
        id=jobRequest.data["id"], description=request.data["description"], subject=subject, request_status=RequestStatus)
    updatedRequest.save()
    return Response({'message': True})


def addProfile(request, user):
    full_name = request.data["full_name"]
    phone_number = request.data["phone_number"]
    profile = Profiles.objects.create(
        full_name=full_name, phone_number=phone_number, user=user)
    profile.save()
    return Response(data={'message': True})


def changeProfile(request):
    pass
