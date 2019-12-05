from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='LoginUrl'),
    path('logout/', views.user_logout, name='LogoutUrl'),
]
