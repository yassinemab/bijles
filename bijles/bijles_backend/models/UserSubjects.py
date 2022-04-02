from rest_framework.response import Response
from django.db import models

class UserSubjects(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject