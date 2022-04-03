from rest_framework.response import Response
from django.db import models
from .Users import Users as UsersModel
from .Requests import Requests as RequestsModel


class Applications(models.Model):
    request = models.ForeignKey(RequestsModel, on_delete=models.CASCADE)
    motivation = models.CharField(max_length=500)
    teacher = models.ForeignKey(UsersModel, on_delete=models.CASCADE)
    price = models.FloatField(default=None, blank=True, null=True)
