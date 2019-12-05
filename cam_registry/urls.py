from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('insert/', views.register_cam, name='cam_registry_insert'),
    path('list/', views.list_cam, name='cam_registry_list'),
]
