from rest_framework.response import Response
from django.db import models
from .Users import Users as UsersModel
from .Subjects import Subjects as SubjectsModel

class UserSubjects(models.Model):
    user = models.ForeignKey(UsersModel, on_delete=models.CASCADE)
    subject = models.ForeignKey(SubjectsModel, on_delete=models.CASCADE)

    def getByUserId(self, id):
        return self.objects.get(user_id=id)

    def getBySubjectId(self, id):
        return self.objects.get(subject_id=id)

    def __str__(self):
        return self.subject