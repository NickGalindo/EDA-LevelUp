from typing import List, Dict, Any
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def increase_level(request: Any):
    """
    view increse_level funtion
    """
    current_user = request.user
    print (current_user.email)

    return redirect("userprofiles:profile")
