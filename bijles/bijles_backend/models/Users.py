from rest_framework.response import Response
from django.db import models
import bcrypt
from . import Roles, Profiles

class Users(models.Model):
    email = models.EmailField(unique=True, max_length=128)
    password = models.CharField(max_length=255)
    active = models.BooleanField()
    role = models.ForeignKey(Roles, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profiles, on_delete=models.CASCADE)

    def __str__(self):
        return self.email


class UserManager(models.Model):
    def createUser(self, email, unhashed_password, profile_id, role_id):
        user = Users()
        user.email = email
        user.active = True
        user.password = bcrypt.hashpw(unhashed_password, bcrypt.gensalt())
        user.profile = profile_id
        user.role = role_id
        if user.is_valid():
            user.save(user.data)
        else:
            raise ValueError("User is incorrect")
        return Response(user.data)
