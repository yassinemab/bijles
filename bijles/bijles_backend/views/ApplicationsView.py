from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import PermissionDenied
from ..models import Users
from ..models.Requests import Requests as RequestsModel
from ..models.Subjects import Subjects as SubjectsModel
from ..models.Applications import Applications as ApplicationsModel
from ..models.RequestStatusses import RequestStatusses as RequestStatusModel
from ..serializers import ApplicationsSerializer, RequestsSerializer, SubjectsSerializer
from . import UsersView, MatchesView


@api_view(["POST"])
def insertApplication(request):
    user = UsersView.getUser(request._request)
    user = Users.objects.filter(id=user.data["id"]).first()
    motivation = request.data["motivation"]
    if len(motivation) > 500:
        raise PermissionDenied("Motivation too long")

    price = request.data["price"]
    jobRequest = RequestsModel.objects.filter(
        id=request.data["request_id"]).first()
    if not jobRequest:
        raise PermissionDenied("Request not found")

    requestUser = Users.objects.filter(
        id=jobRequest.student_id).first()
    if user.role_id == requestUser.role_id:
        raise PermissionDenied("Users of same type cannot interact.")

    amount_of_hits = ApplicationsModel.objects.filter(
        teacher=user, request=jobRequest).count()
    if amount_of_hits >= 1:
        raise PermissionDenied("Already inserted application.")

    application = ApplicationsModel.objects.create(
        motivation=motivation, price=price, request=jobRequest, teacher=user)
    application.save()
    MatchesView.createMatch(user, requestUser, request._request)
    return Response({"message": True})


@api_view(["GET"])
def getYourApplications(request):
    user = UsersView.getUser(request._request)
    applications = ApplicationsModel.objects.filter(teacher_id=user.data["id"])
    serializer = ApplicationsSerializer(applications, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getApplicationsByRequestId(request):
    jobRequest = RequestsModel.objects.filter(
        id=request.GET["request_id"]).first()
    if not jobRequest:
        raise PermissionDenied("Request not found")

    applications = ApplicationsModel.objects.filter(request=jobRequest)
    serializer = ApplicationsSerializer(applications, many=True)
    return Response(serializer.data)

@api_view(["DELETE"])
def deleteApplication(request):
    application = ApplicationsModel.objects.filter(id=request.data["id"]).first()
    if not application:
        raise PermissionDenied("Application not found")

    application.delete()
    return Response({"message": True})
