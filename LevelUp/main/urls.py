"""
URL configuration for Main app
"""

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('auth/login', views.login, name='login'),
    path('auth/signup', views.sign_up, name='sign up'),
    path('volume', views.volume, name='volume'),
    path('queue365', views.queue_365, name='queue_365'),
    path('pyramid', views.pyramid, name='pyramid'),
]
