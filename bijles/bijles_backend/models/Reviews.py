from rest_framework.response import Response
from django.db import models

class Reviews(models.Model):
    student = models.ForeignKey(
        Users, on_delete=models.CASCADE, related_name='hallo')
    teacher = models.ForeignKey(
        Users, on_delete=models.CASCADE, related_name='jemama')
    content = models.CharField(max_length=500)
    rating = models.IntegerField(default=1)

    def __str__(self):
        return self.content
