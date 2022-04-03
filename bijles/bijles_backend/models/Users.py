from rest_framework.response import Response
from django.db import models
from .Roles import Roles as RolesModel

class Users(models.Model):
    email = models.EmailField(unique=True, max_length=128)
    password = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    role = models.ForeignKey(RolesModel, on_delete=models.CASCADE, default=None, blank=True, null=True)

    def getById(self, id):
        return self.objects.get(id=id)

    def __str__(self):
        return self.email
