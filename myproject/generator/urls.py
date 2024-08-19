# generator/urls.py
from django.urls import path
from . import views

app_name = 'generator'

urlpatterns = [
    path('', views.generator, name='generator'),
    path('generate/<int:person_id>/', views.generate_text, name='generate_text'),
]