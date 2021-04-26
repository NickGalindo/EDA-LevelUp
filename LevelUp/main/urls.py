"""
URL configuration for Main app
"""

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('queue365', views.queue_365, name='queue_365'),

]
