from difflib import Match
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import PermissionDenied
from ..models import Users
from ..models.Requests import Requests as RequestsModel
from ..models.Subjects import Subjects as SubjectsModel
from ..models.MatchStatusses import MatchStatusses as MatchStatusModel
from ..models.Matches import Matches as MatchesModel
from ..models.Applications import Applications as ApplicationsModel
from ..models.RequestStatusses import RequestStatusses as RequestStatusModel
from ..serializers import ApplicationsSerializer, MatchesSerializer, RequestsSerializer, SubjectsSerializer
from . import UsersView


def createMatch(target, initiator, request):
    user = UsersView.getUser(request)

    if target == initiator:
        raise PermissionDenied("Cannot create match with self")

    match_status = MatchStatusModel.objects.filter(name="Pending").first()
    match = MatchesModel.objects.create(
        initiator=initiator, target=target, match_status=match_status)
    match.save()

    # See if the other person already sent a match request
    reverse_match = MatchesModel.objects.filter(
        initiator=target, target=initiator).first()
    if reverse_match.match_status == "Pending":
        reverse_match.delete()
        match_status = MatchStatusModel.objects.filter(name="Accepted").first()
        match.match_status = match_status
        match.save()
    elif reverse_match.match_status == "Accepted":
        match.delete()
    return Response({"message": True})


@api_view(["POST"])
def handleMatch(request):
    target = Users.objects.filter(id=request.data["target_id"]).first()
    if not target:
        raise PermissionDenied("Target not found")

    initiator = Users.objects.filter(id=request.data["initiator_id"]).first()
    if not initiator:
        raise PermissionDenied("Initiator not found")

    match_status = MatchStatusModel.objects.filter(
        name=request.data["status"]).first()
    if not match_status:
        raise PermissionDenied(
            "Match status not found. Only 'Accepted', 'Rejected' or 'Pending' will be accepted")

    match = MatchesModel.objects.filter(
        target=target, initiator=initiator).first()

    if not match:
        raise PermissionDenied("There is no match")

    match.match_status = match_status
    match.save()
    return Response({"message": True})


@api_view(["GET"])
def getOwnMatches(request):
    user = UsersView.getUser(request._request)
    match_status = MatchStatusModel.objects.filter(name="Accepted").first()
    matches = MatchesModel.objects.filter(target_id=user.data["id"], match_status=match_status) | MatchesModel.objects.filter(
        initiator_id=user.data["id"], match_status=match_status)
    serializer = MatchesSerializer(matches, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getIncomingMatches(request):
    user = UsersView.getUser(request._request)
    match_status = MatchStatusModel.objects.filter(name="Pending").first()
    matches = MatchesModel.objects.filter(
        target_id=user.data["id"], match_status=match_status)
    serializer = MatchesSerializer(matches, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getOutgoingMatches(request):
    user = UsersView.getUser(request._request)
    match_status = MatchStatusModel.objects.filter(name="Pending").first()
    matches = MatchesModel.objects.filter(
        initiator_id=user.data["id"], match_status=match_status)
    serializer = MatchesSerializer(matches, many=True)
    return Response(serializer.data)
