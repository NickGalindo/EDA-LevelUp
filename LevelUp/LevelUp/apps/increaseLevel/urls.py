"""
URL configuration for IncreaseLevel app
"""

from django.contrib import admin
from django.urls import path, include
from . import views


app_name='increaseLevel'
urlpatterns = [
    path('increaseLevel', views.increase_level, name='increase_level'),
]
