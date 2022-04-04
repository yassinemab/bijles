from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import Users
from ..models import Profiles
from ..models.RequestStatusses import RequestStatusses as RequestStatusModel
from ..serializers import ProfileSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import PermissionDenied
from ..models import Users
from ..models.Locations import Locations as LocationsModel
from ..models.Profiles import Profiles as ProfilesModel
from ..models.RequestStatusses import RequestStatusses as RequestStatusModel
from ..serializers import ApplicationsSerializer, RequestsSerializer, ReviewsSerializer, SubjectsSerializer
from . import UsersView, MatchesView


def addProfile(request, user):
    full_name = request.data["full_name"]
    phone_number = request.data["phone_number"]
    profile = Profiles.objects.create(
        full_name=full_name, phone_number=phone_number, user=user)
    profile.save()
    return Response(data={'message': True})


@api_view(["PUT"])
def changeProfile(request):
    user = UsersView.getUser(request._request)
    full_name = request.data["full_name"]
    biography = request.data["biography"]
    if len(biography) > 300:
        raise PermissionDenied("Biography too long")

    phone_number = request.data["phone_number"]
    private = request.data["private"]
    online = request.data["online"]
    physical = request.data["physical"]
    location = request.data["location"]
    gender = request.data["gender"]
    location = LocationsModel.objects.filter(name=location).first()
    profile = ProfilesModel.objects.filter(user_id=user.data["id"]).first()
    if not profile:
        raise PermissionDenied("Profile not found.")

    profile.full_name = full_name
    profile.biography = biography
    profile.phone_number = phone_number
    profile.private = private
    profile.online = online
    profile.gender = gender
    profile.physical = physical
    profile.location = location

    profile.save()
    return Response({"message": True})

    # Profile picture
