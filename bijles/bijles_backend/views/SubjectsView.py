from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import PermissionDenied
from ..models import Users
from ..models.Requests import Requests as RequestsModel
from ..models.Subjects import Subjects as SubjectsModel
from ..models.RequestStatusses import RequestStatusses as RequestStatusModel
from ..serializers import RequestsSerializer, SubjectsSerializer
from . import UsersView
from ..models.UserSubjects import UserSubjects as UserSubjectsModels


@api_view(['GET'])
def getAllSubjects(request):
    subjects = SubjectsModel.objects.all()
    serializer = SubjectsSerializer(subjects, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def addSubjectToUser(request):
    subject = SubjectsModel.objects.filter(
        name=request.data["subject"]).first()
    if not subject:
        raise PermissionDenied("Subject not found")

    user = UsersView.getUser(request._request)
    user_subject_exists = UserSubjectsModels.objects.filter(
        user_id=user.data["id"], subject=subject).exists()
    if user_subject_exists:
        raise PermissionDenied("User already has connection to the subject")

    user_subject = UserSubjectsModels.objects.create(
        user_id=user.data["id"], subject=subject)
    user_subject.save()
    return Response({"message": True})


@api_view(["DELETE"])
def deleteSubjectFromUser(request):
    subject = SubjectsModel.objects.filter(
        name=request.data["subject"]).first()
    if not subject:
        raise PermissionDenied("Subject not found")

    user = UsersView.getUser(request._request)
    user_subject = UserSubjectsModels.objects.filter(
        user_id=user.data["id"], subject=subject).first()
    if not user_subject:
        raise PermissionDenied("User does not have a connection with the subject")

    user_subject.delete()
    return Response({"message": True})
