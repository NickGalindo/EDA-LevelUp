"""
URL configuration for Userprofiles app
"""

from django.contrib import admin
from django.urls import path, include
from . import views


app_name='userprofiles'
urlpatterns = [
    path('profile', views.profile, name='profile'),
    path('new-workout', views.new_workout, name='new-workout'),
    path('add-exercises', views.add_exercises, name='add-exercises'),
    path('generate', views.generate, name='generate')
]
