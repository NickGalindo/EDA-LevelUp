from typing import List, Dict, Any
from django.shortcuts import render, redirect

from django.contrib.auth import logout

# Create your views here.
def home(request: Any):
    """
    Make the Home view here
    :param request: the request passed in by the webview
    """
    context = {}

    #if user is already logged in then redirect to profile
    if request.user.is_authenticated:
        logout(request)
        return redirect("userprofiles:profile")

    return render(request=request, template_name="home/home.html", context=context)
