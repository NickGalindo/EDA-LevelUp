"""
URL configuration for Authentication app
"""

from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "volumen"
urlpatterns = [
    path('history', views.VolumeHistory, name='VolumeHistory'),
]