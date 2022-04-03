from rest_framework.response import Response
from django.db import models
from .Users import Users as UsersModel
from .Subjects import Subjects as SubjectsModel


class UserSubjects(models.Model):
    user = models.ForeignKey(UsersModel, on_delete=models.CASCADE)
    subject = models.ForeignKey(SubjectsModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject
