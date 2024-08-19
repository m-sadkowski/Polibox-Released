# mycalendar/models.py
from django.db import models


class Event(models.Model):
    objects = None
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date = models.DateField()

    def __str__(self):
        return self.title
