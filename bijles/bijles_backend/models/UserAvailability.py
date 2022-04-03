from rest_framework.response import Response
from django.db import models
from .Users import Users as UsersModel
from .Availability import Availability as AvailabilityModel


class UserAvailability(models.Model):
    user = models.ForeignKey(UsersModel, on_delete=models.CASCADE)
    availability = models.ForeignKey(
        AvailabilityModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject
