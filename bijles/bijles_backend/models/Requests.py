from rest_framework.response import Response
from django.db import models
from .Users import Users as UsersModel
from .Subjects import Subjects as SubjectsModel
from .RequestStatusses import RequestStatusses as RequestStatusModel
from .Languages import Languages as LanguagesModel
from .Levels import Levels as LevelsModel


class Requests(models.Model):
    student = models.ForeignKey(UsersModel, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)
    subject = models.ForeignKey(
        SubjectsModel, on_delete=models.SET('Onbekend'))
    language = models.ForeignKey(LanguagesModel, on_delete=models.CASCADE)
    level = models.ForeignKey(LevelsModel, on_delete=models.CASCADE)
    request_status = models.ForeignKey(
        RequestStatusModel, on_delete=models.CASCADE)
