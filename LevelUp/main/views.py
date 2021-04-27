from django.shortcuts import render
from generator.generate import createUsers, createSpecialUsers, specialUsersExist, usersExist
from generator.queue_365 import queue_workouts
from generator.pyramid_stack import generate_workout
from typing import List, Dict, Any
import subprocess

# Create your views here.


# login Site
def login(request: Any):
    """
    View for the login site
    :param request: The request passed in by the webview
    """

    context = {'title': 'Login', 'status':'Initial'}

    """
    if not usersExist():
        createUsers()
        context["status"] = "Success"
        """


    """if not specialUsersExist():
        createSpecialUsers()
        context["status"] = "Success"
    """


    return render(request=request, template_name='login/login.html', context=context)


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
