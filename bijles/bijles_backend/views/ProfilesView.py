from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import Users
from ..models import Profiles
from ..models.RequestStatusses import RequestStatusses as RequestStatusModel
from ..serializers import ProfileSerializer


def addProfile(request, user):
    full_name = request.data["full_name"]
    phone_number = request.data["phone_number"]
    profile = Profiles.objects.create(
        full_name=full_name, phone_number=phone_number, user=user)
    profile.save()
    return Response(data={'message': True})


def changeProfile(request):
    pass
