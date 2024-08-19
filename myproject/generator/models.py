# generator/models.py
from django.db import models


class Person(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    greeting = models.CharField(max_length=200)
    mail = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.name
