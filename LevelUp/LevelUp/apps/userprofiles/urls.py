"""
URL configuration for Userprofiles app
"""

from django.contrib import admin
from django.urls import path, include
from . import views


app_name='userprofiles'
urlpatterns = [
    path('profile', views.profile, name='profile'),
]
