from rest_framework.response import Response
from django.db import models

class Matches(models.Model):
    student = models.ForeignKey(
        Users, on_delete=models.CASCADE, related_name='students')
    teacher = models.ForeignKey(
        Users, on_delete=models.CASCADE, related_name='teachers')
    match_status = models.ForeignKey(
        MatchStatusses, on_delete=models.CASCADE)

    def __str__(self):
        return self.match_status