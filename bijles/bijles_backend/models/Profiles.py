from rest_framework.response import Response
from django.db import models
from . import Locations

class Profiles(models.Model):
    full_name = models.CharField(max_length=255)
    biography = models.CharField(max_length=1000)
    profile_picture = models.FileField()
    phone_number = models.CharField(max_length=20)
    private = models.BooleanField()
    online = models.BooleanField()
    physical = models.BooleanField()
    location = models.ForeignKey(Locations, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name