from typing import List, Dict, Any
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def profile(request: Any):
    """
    User profile views
    :param request: the request passed in by the webview
    """
    context = {}

    return render(request=request, template_name="userprofiles/profile.html", context=context)
