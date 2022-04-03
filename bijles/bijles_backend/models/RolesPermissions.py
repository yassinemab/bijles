from rest_framework.response import Response
from django.db import models
from . import Roles, Permissions
from .Roles import Roles as RolesModel
from .Permissions import Permissions as PermissionsModel

class RolesPermissions(models.Model):
    role = models.ForeignKey(RolesModel, on_delete=models.CASCADE)
    permission = models.ForeignKey(PermissionsModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.role