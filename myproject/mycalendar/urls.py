# mycalendar/urls.py
from django.urls import path
from . import views

app_name = 'mycalendar'

urlpatterns = [
    path('', views.calendar_view, name='calendar'),
    path('event-add/', views.event_create_view, name='event_add'),
    path('event-delete/<int:pk>/', views.event_delete_view, name='event_delete'),
    path('event-edit/<int:pk>/', views.event_update_view, name='event_edit'),
]
