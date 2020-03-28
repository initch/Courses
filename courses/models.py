from django.db import models
from boards.models import Board


class Course(models.Model):
    name = models.CharField(max_length=40, unique=True)
    num = models.CharField(max_length=10, unique=True)
    teacher = models.CharField(max_length=10)
    board = models.OneToOneField(Board, on_delete=models.SET_NULL, related_name='course', blank=True, null=True)

    def __str__(self):
        return self.name
