# progression/urls.py
from django.urls import path
from . import views

app_name = 'progression'

urlpatterns = [
    path('', views.direction_list, name='direction_list'),
    path('<slug:direction_slug>/', views.subject_list, name='subject_list'),
    path('<slug:direction_slug>/<slug:subject_slug>/', views.subject_detail, name='subject_detail'),
    path('<slug:direction_slug>/<slug:subject_slug>/update/', views.update_progress, name='update_progress'),
]
