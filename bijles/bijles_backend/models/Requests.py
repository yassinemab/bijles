from rest_framework.response import Response
from django.db import models

class Requests(models.Model):
    student = models.ForeignKey(Users, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)
    subject = models.ForeignKey(Subjects, on_delete=models.SET('Onbekend'))
    request_status = models.ForeignKey(
        RequestStatusses, on_delete=models.CASCADE)

    def __str__(self):
        return self.description