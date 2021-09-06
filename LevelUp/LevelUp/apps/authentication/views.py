from typing import List, Dict, Any

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

from pymongo import MongoClient
from structures.disjoint_set import DisjointSet
from structures.adjacency_list import AdjacencyList
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

    #If user is already logged in then redirect to the users profile page
    if request.user.is_authenticated:
        return redirect("userprofiles:profile")

    #if form was filled out then proceed to verify and sign user up
    if request.method == 'POST':
        form = forms.signup_form(request.POST, error_class=forms.CustomError) #obtain the signup form data

        #Validate the form and clean the data
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(data["username"], data["email"], data["password"]) #create the user object
            user.save()
            auth.login(request, user) #login the user
            #Add the user to the mongo database profile with default data
            client =  MongoClient()
            user_collection = client["EDA-Project"]["user_profiles"]
            disjoint_set_collection = client["EDA-Project"]["disjoint_set"]
            # adjacency_list_collection = client["EDA-Project"]["adjacency_list"]
            user_graph_collection = client["EDA-Project"]["user_graph"]

            user_collection.insert_one({
                "email": data["email"],
                "username": data["username"],
                "first_name": "",
                "last_name": "",
                "profile_image": None,
                "workouts": []
            })

            # adj_list = AdjacencyList()
            # adj_list.mongo_deserialize(adjacency_list_collection)
            dj_set = DisjointSet()
            dj_set.mongo_deserialize(disjoint_set_collection)
            user_graph = AdjacencyList()
            user_graph.mongo_deserialize(user_graph_collection)

            dj_set.add(data["username"])
            dj_set.merge(data["username"], "Beginner")

            user_graph.add_node(data["email"])
            user_graph.connect(data["email"], "Beginner")

            dj_set.mongo_serialize(disjoint_set_collection)
            user_graph.mongo_serialize(user_graph_collection)

            client.close()
            return redirect("userprofiles:profile")
    else:
        #If the form isn't valid then fill form with errors
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

    #If user is already logged in then redirect to the users profile page
    if request.user.is_authenticated:
        return redirect("userprofiles:profile")

    #If the form was filled out
    if request.method == 'POST':
        form = forms.login_form(request.POST)

        #Verify if the form is valid
        if form.is_valid():
            data = form.cleaned_data
            user = auth.authenticate(request, username=data["username"], password=data["password"]) #authenticate the user

            if user is not None:
                auth.login(request, user) #log the user in if the authentication is valid

                return redirect("userprofiles:profile")
            else:
                status = 'LoginFail' #If authentication not valid the set the status to failed
    else:
        form = forms.signup_form()

    context['status'] = status
    context['form'] = form
    return render(request=request, template_name='authentication/login.html', context=context)

#logout site
def logout(request: Any):
    """
    View to log user oout
    :param request: The request passed in by the webview
    """

    if request.user.is_authenticated:
        auth.logout(request)

    return redirect("home")
