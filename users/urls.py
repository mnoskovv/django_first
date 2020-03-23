"""Определяет схемы url для пользователей"""
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

urlpatterns = [
    # login page
    path('login/', LoginView.as_view(template_name="users/login.html"), name="login"),
    # logout page
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", views.register, name="register"),
]