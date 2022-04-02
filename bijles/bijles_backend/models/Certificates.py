from rest_framework.response import Response
from django.db import models

class Certificates(models.Model):
    picture = models.FileField()
    caption = models.CharField(
        max_length=255, default=None, blank=True, null=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return self.picture