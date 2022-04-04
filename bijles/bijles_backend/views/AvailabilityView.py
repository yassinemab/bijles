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
from ..models.Availability import Availability as AvailabilityModel
from ..models.UserAvailability import UserAvailability as UserAvailabilityModel
from ..serializers import AvailabilitySerializer


@api_view(["GET"])
def getAllAvailabilities(request):
    availabilities = AvailabilityModel.objects.all()
    serializer = AvailabilitySerializer(availabilities, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addAvailabilityToUser(request):
    availability = request.data["availability"]
    user = UsersView.getUser(request._request)

    availability = AvailabilityModel.objects.filter(name=availability).first()
    if not availability:
        raise PermissionDenied("Availability not found")

    user_availability_exists = UserAvailabilityModel.objects.filter(
        availability=availability, user_id=user.data["id"]).exists()
    if user_availability_exists:
        raise PermissionDenied("Already has connection")

    user_availability = UserAvailabilityModel.objects.create(
        user_id=user.data["id"], availability=availability)
    user_availability.save()
    return Response({"message": True})


@api_view(["DELETE"])
def deleteAvailabilityFromUser(request):
    availability = request.data["availability"]
    user = UsersView.getUser(request._request)

    availability = AvailabilityModel.objects.filter(name=availability).first()
    if not availability:
        raise PermissionDenied("Availability not found")

    user_availability = UserAvailabilityModel.objects.filter(
        availability=availability, user_id=user.data["id"])
    if not user_availability:
        raise PermissionDenied("There is no connection to delete")

    user_availability.delete()
    return Response({"message": True})