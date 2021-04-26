from django.shortcuts import render
from generator.generate import createUsers, createSpecialUsers, specialUsersExist, usersExist
from generator.pyramid_stack import generate_workout
from typing import List, Dict, Any

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


    if not specialUsersExist():
        createSpecialUsers()
        context["status"] = "Success"


    return render(request=request, template_name='login/login.html', context=context)



def pyramid(request :Any):

    context = {'title': 'pyramidWorkout', 'status':'Initial'}

    n = int(input("how many exercices?"))
    generate_workout(n)



    return render(request=request, template_name='basetemplate.html', context=context)








