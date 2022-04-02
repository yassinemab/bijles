from rest_framework.response import Response
from django.db import models

class RolesPermissions(models.Model):
    role = models.ForeignKey(Roles, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permissions, on_delete=models.CASCADE)

    def __str__(self):
        return self.role