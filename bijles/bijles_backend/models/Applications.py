from rest_framework.response import Response
from django.db import models

class Applications(models.Model):
    request = models.ForeignKey(Requests, on_delete=models.CASCADE)
    motivation = models.CharField(max_length=500)
    teacher = models.ForeignKey(Users, on_delete=models.CASCADE)
    price = models.FloatField(default=None, blank=True, null=True)

    def __str__(self):
        return self.motivation