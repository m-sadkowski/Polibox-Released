# materials/urls.py
from django.urls import path
from . import views

app_name = 'materials'

urlpatterns = [
    path('', views.materials_list, name="list"),
    path('new-material/', views.material_new, name="new-material"),
    path('<slug:slug>/', views.material_page, name="page"),
    path('update-material/<slug:slug>/', views.material_update, name="update-material"),
    path('delete-file/<int:file_id>/', views.delete_file, name="delete-file"),
    path('delete-material/<slug:slug>/', views.delete_material, name="delete-material"),
]
