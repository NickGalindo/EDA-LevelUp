from typing import List, Dict, Any

from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth

from . import forms

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
