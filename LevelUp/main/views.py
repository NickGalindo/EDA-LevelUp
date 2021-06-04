from typing import List, Dict, Any
import subprocess
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth

from generator.generate import createUsers, createSpecialUsers, specialUsersExist, usersExist
from generator.queue_365 import queue_workouts
from generator.pyramid_stack import generate_workout

from . import forms
# Create your views here.

#registration site
def sign_up(request: Any):
    """
    View for sign up site
    :param request: The request passed in by the webview
    """
    context = {'title': 'Sign Up'}
    status = 'InitRegistration'
    form = None

    if request.method == 'POST':
        form = forms.signup_form(request.POST, error_class=forms.CustomError)

        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(data["username"], data["email"], data["password"])
            user.save()
            auth.login(request, user)
    else:
        form = forms.signup_form(error_class=forms.CustomError)

    context['form'] = form
    context['status'] = status
    return render(request=request, template_name='authentication/signup.html', context=context)


# login Site
def login(request: Any):
    """
    View for the login site
    :param request: The request passed in by the webview
    """

    context = {'title': 'Login'}
    status = 'InitLogin'
    form = None

    if request.method == 'POST':
        form = forms.login_form(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = auth.authenticate(request, username=data["username"], password=data["password"])

            if user is not None:
                auth.login(request, user)
            else:
                status = 'LoginFail'
    else:
        form = forms.signup_form()

    context['status'] = status
    context['form'] = form
    return render(request=request, template_name='authentication/login.html', context=context)


def volume(request: Any):
    """
    Trial the volume functionalty
    :param request: the rquest passed in by the webview
    """

    context = {'title': 'Volume', 'status': 'Success'}

    subprocess.call("python generator/generate_volume_cpp.py", shell=True)

    return render(request=request, template_name='volume/volume.html', context=context)

def queue_365(request : Any):

    context = {'title': 'queue_365', 'status':'Initial'}


    option = int(input(" \n 0. Array implementation \n 1. References implementation \n"))
    n = int(input("How many days?: "))

    if ( option not in [1,0] or n<=0):
        print("Please, check the data!")

    else:
        queue_workouts(option, n)

    return render(request=request, template_name='basetemplate.html', context=context)


def pyramid(request :Any):

    context = {'title': 'pyramidWorkout', 'status':'Initial'}

    n = int(input("how many exercices?"))
    generate_workout(n)

    return render(request=request, template_name='basetemplate.html', context=context)
