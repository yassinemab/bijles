from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import PermissionDenied
from ..models import Users
from ..models.Requests import Requests as RequestsModel
from ..models.Subjects import Subjects as SubjectsModel
from ..models.Levels import Levels as LevelsModel
from ..models.Languages import Languages as LanguagesModel
from ..models.RequestStatusses import RequestStatusses as RequestStatusModel
from ..serializers import RequestsSerializer
from . import UsersView


@api_view(['POST'])
def createRequest(request):
    user = UsersView.getUser(request._request)
    user = Users.objects.filter(id=user.data["id"]).first()
    description = request.data["description"]
    subject = SubjectsModel.objects.filter(
        name=request.data["subject"]).first()
    if not subject:
        subject = SubjectsModel.objects.filter(name='Onbekend').first()

    requestStatusName = 'Concept' if request.data["concept"] else 'Published'
    requestStatus = RequestStatusModel.objects.filter(
        name=requestStatusName).first()

    level = LevelsModel.objects.filter(name=request.data["level"]).first()
    if not level:
        raise PermissionDenied("Level not found")

    language = LanguagesModel.objects.filter(
        name=request.data["language"]).first()
    if not language:
        raise PermissionDenied("Language not found")

    jobRequest = RequestsModel.objects.create(
        student=user, description=description, subject=subject, request_status=requestStatus, language=language, level=level)

    jobRequest.save()
    return Response({'message': True})


@api_view(['GET'])
def getRequestById(request):
    jobRequest = RequestsModel.objects.filter(
        id=request.GET.get('id', '')).first()
    serializer = RequestsSerializer(jobRequest, many=False)
    return Response(serializer.data)


@api_view(["GET"])
def getOwnRequests(request):
    user = UsersView.getUser(request._request)
    requests = RequestsModel.objects.filter(student_id=user.data["id"])
    serializer = RequestsSerializer(requests, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteRequest(request):
    user = UsersView.getUser(request._request)
    jobRequest = RequestsModel.objects.filter(
        id=request.data["id"], student_id=user.data["id"]).first()
    if not jobRequest:
        raise PermissionDenied("Request not found")
    jobRequest.delete()
    return Response({'message': True})


@api_view(["PUT"])
def updateRequest(request):
    jobRequest = RequestsModel.objects.filter(
        id=request.data["id"]).first()

    user = UsersView.getUser(request._request)
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

    RequestStatus = RequestStatusModel.objects.filter(
        name=request.data["request_status"]).first()
    if not RequestStatus:
        RequestStatus = RequestStatusModel.objects.filter(
            name="Onbekend").first()
    updatedRequest = RequestsModel(
        id=jobRequest.data["id"], description=request.data["description"], subject=subject, request_status=RequestStatus)
    updatedRequest.save()
    return Response({'message': True})
