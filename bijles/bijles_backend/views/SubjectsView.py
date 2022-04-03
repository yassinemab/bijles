from html5lib import serialize
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import PermissionDenied
from ..models import Users
from ..models.Requests import Requests as RequestsModel
from ..models.Subjects import Subjects as SubjectsModel
from ..models.RequestStatusses import RequestStatusses as RequestStatusModel
from ..serializers import RequestsSerializer, SubjectsSerializer


@api_view(['GET'])
def getAllSubjects(request):
    subjects = SubjectsModel.objects.all()
    serializer = SubjectsSerializer(subjects, many=True)
    return Response(serializer.data)
