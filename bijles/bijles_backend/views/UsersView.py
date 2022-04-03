from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed, PermissionDenied
from ..models import Users
from ..models.Roles import Roles as RolesModel
from ..serializers import UserSerializer
import jwt


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
