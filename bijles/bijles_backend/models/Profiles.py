from rest_framework.response import Response
from django.db import models
from . import Locations
from .Users import Users as UsersModel

class Profiles(models.Model):
    full_name = models.CharField(max_length=255)
    biography = models.CharField(max_length=100, default=None, blank=True, null=True)
    profile_picture = models.FileField(default=None, blank=True, null=True)
    phone_number = models.CharField(max_length=20)
    private = models.BooleanField(default=True)
    online = models.BooleanField(default=True)
    physical = models.BooleanField(default=True)
    location = models.ForeignKey(Locations.Locations, on_delete=models.CASCADE, default=None, blank=True, null=True)
    user = models.ForeignKey(UsersModel, on_delete=models.CASCADE, default=None, blank=True, null=True)


    def __str__(self):
        return self.full_name