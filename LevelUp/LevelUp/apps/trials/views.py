from typing import List, Dict, Any
import subprocess
from django.shortcuts import render, redirect

from generator.generate_old import createUsers, createSpecialUsers, specialUsersExist, usersExist
from generator.queue_365 import queue_workouts
from generator.pyramid_stack import generate_workout

# Create your views here.
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

    try:
        option = int(input(" \n 0. Array implementation \n 1. References implementation \n"))
        n = int(input("How many days?: "))
    except ValueError as e:
        print("Invalid data")
        return redirect("/trials/queue365")

    if ( option not in [1,0] or n<=0):
        print("Please, check the data!")
    else:
        queue_workouts(option, n)

    return render(request=request, template_name='basetemplate.html', context=context)


def pyramid(request :Any):

    context = {'title': 'pyramidWorkout', 'status':'Initial'}

    try:
        n = int(input("how many exercices?"))
    except ValueError as e:
        print("Invalid input")
        return redirect("/trials/pyramid")

    generate_workout(n)

    return render(request=request, template_name='basetemplate.html', context=context)
