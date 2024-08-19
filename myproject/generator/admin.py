# generator/admin.py
from django.contrib import admin
from .models import Person

admin.site.register(Person)
