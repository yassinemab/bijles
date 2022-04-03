from rest_framework.response import Response
from django.db import models
from .Users import Users as UsersModel

class Certificates(models.Model):
    picture = models.FileField()
    caption = models.CharField(
        max_length=255, default=None, blank=True, null=True)
    user = models.ForeignKey(UsersModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.picture