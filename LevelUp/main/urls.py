"""
URL configuration for Main app
"""

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('volume', views.volume, name='volume')
    path('queue365', views.queue_365, name='queue_365'),
    path('pyramid', views.pyramid, name='pyramid'),
]
