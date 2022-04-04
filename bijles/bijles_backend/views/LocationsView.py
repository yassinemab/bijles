from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import PermissionDenied
from ..models import Users
from ..models.Requests import Requests as RequestsModel
from ..models.Subjects import Subjects as SubjectsModel
from ..models.Applications import Applications as ApplicationsModel
from ..models.Profiles import Profiles as ProfilesModel
from ..models.RequestStatusses import RequestStatusses as RequestStatusModel
from ..serializers import ApplicationsSerializer, RequestsSerializer, SubjectsSerializer, LocationsSerializer
from . import UsersView, MatchesView
from ..models.Locations import Locations as LocationsModel


@api_view(["GET"])
def getAllLocations(request):
    locations = LocationsModel.objects.all()
    serializer = LocationsSerializer(locations, many=True)
    return Response(serializer.data)


def addLocationToUser(request):
    location = LocationsModel.objects.filter(
        name=request.data["location"]).first()
    if not location:
        raise PermissionDenied("Location not found")

    user = UsersView.getUser(request._request)
    profile = ProfilesModel.objects.filter(user_id=user.data["id"]).first()
    if not profile:
        raise PermissionDenied("Profile not found")

    profile.location = location
    profile.save()
    return Response({"message": True})


def deleteLocationFromUser(request):
    user = UsersView.getUser(request._request)
    profile = ProfilesModel.objects.filter(user_id=user.data["id"]).first()
    if not profile:
        raise PermissionDenied("Profile not found")
    location = LocationsModel.objects.filter(name="Onbekend").first()
    profile.location = location
    profile.save()
    return Response({"message": True})
