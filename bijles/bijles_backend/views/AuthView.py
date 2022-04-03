@api_view(['POST'])
def register(request):
    email = request.data["email"]
    password = request.data["password"].encode('utf-8')
    password = bcrypt.hashpw(password, bcrypt.gensalt())
    role_name = 'Teacher' if request.data["is_teacher"] else 'Student'
    role = RolesModel.objects.get(name=role_name)
    user = Users.objects.create(
        email=email, password=password, role=role)
    user.save()
    addProfile(request, user)
    return Response(data={'message': True})


@api_view(['POST'])
def login(request):
    email = request.data["email"]
    user = Users.objects.filter(email=email).first()
    if not user:
        return Response({'message': False})
    password = request.data["password"].encode("utf-8")
    user_password = user.password[2: -1:].encode("utf-8")
    if not bcrypt.checkpw(password, user_password):
        return Response({'message': False})
    # Insert cookie into db and return the cookie
    payload = {
        'id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=100),
        'iat': datetime.datetime.utcnow()
    }

    token = jwt.encode(payload, ' $2a$12$Cyk/3gU.ErvVuhlzv16ULOFFEPytP934bMPWHMkH2J0pt0piZ0lMm ',
                       algorithm='HS256').decode('utf-8')

    response = Response()
    response.set_cookie(key='jwt', value=token, httponly=True)
    response.data = {
        'jwt': token
    }
    return response


@api_view(['POST'])
def logout(request):
    response = Response()
    print(response)
    response.delete_cookie('jwt')
    return Response({"message": True})
