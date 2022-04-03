from rest_framework.response import Response
from django.db import models
from .MatchStatusses import MatchStatusses as MatchStatusModel
from .Users import Users as UsersModel

class Matches(models.Model):
    initiator = models.ForeignKey(
        UsersModel, on_delete=models.CASCADE, related_name='initiator')
    target = models.ForeignKey(
        UsersModel, on_delete=models.CASCADE, related_name='target')
    match_status = models.ForeignKey(
        MatchStatusModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.match_status