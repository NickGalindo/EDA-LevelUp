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
    path('edit-profile', views.edit_profile, name='edit-profile'),
    path('view-workout', views.view_workout, name='view-workout')
]
