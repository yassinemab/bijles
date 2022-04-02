from rest_framework.response import Response
from django.db import models

class Locations(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name
