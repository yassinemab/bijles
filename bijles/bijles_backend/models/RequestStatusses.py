from rest_framework.response import Response
from django.db import models

class RequestStatusses(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
