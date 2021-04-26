from django.shortcuts import render
from generator.generate import createUsers, createSpecialUsers, specialUsersExist, usersExist
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


    if not specialUsersExist():
        createSpecialUsers()
        context["status"] = "Success"


    return render(request=request, template_name='login/login.html', context=context)


def volume(request: Any):
    """
    Trial the volume functionalty
    :param request: the rquest passed in by the webview
    """

    context = {'title': 'Volume', 'status': 'Success'}

    subprocess.call("python generator/generate_volume_cpp.py", shell=True)

    return render(request=request, template_name='volume/volume.html', context=context)
