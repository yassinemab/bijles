from rest_framework.response import Response
from django.db import models

class Permissions(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name