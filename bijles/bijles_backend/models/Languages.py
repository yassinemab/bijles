from rest_framework.response import Response
from django.db import models

class Languages(models.Model):
    name = models.CharField(max_length=128, default=None, blank=True, null=True)

    def __str__(self):
        return self.name
