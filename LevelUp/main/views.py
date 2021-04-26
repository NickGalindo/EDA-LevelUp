from django.shortcuts import render
from generator.generate import createUsers, createSpecialUsers, specialUsersExist, usersExist
from typing import List, Dict, Any

from generator.generate_stack import generate_stack

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
