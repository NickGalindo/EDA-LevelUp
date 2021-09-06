from typing import List, Dict, Any
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory

import uuid
from pymongo import MongoClient
from structures.linked_list import LinkedList_References
from structures.disjoint_set import DisjointSet
from structures.adjacency_list import AdjacencyList
import datetime
from . import forms

# Create your views here.
@login_required
def profile(request: Any):
    """
    User profile views
    :param request: the request passed in by the webview
    """
    context = {}

    client = MongoClient()
    user_collection = client["EDA-Project"]["user_profiles"]
    user_graph_collection = client["EDA-Project"]["user_graph"]

    usr_email = request.user.email
    usr = user_collection.find_one({"email": usr_email})

    if 'rmw' in request.GET and 'id' in request.GET:
        ll_list = LinkedList_References(usr["workouts"])
        if int(request.GET['rmw']) < len(ll_list):
            if ll_list.get(int(request.GET['rmw']))['id'] == request.GET['id']:
                ll_list.remove(int(request.GET['rmw']))
                usr["workouts"] = ll_list.to_list()
                user_collection.update_one({"email": usr_email}, {"$set": {"workouts": usr["workouts"]}})

    user_graph = AdjacencyList()
    user_graph.mongo_deserialize(user_graph_collection)

    connections = 0
    for node in user_graph.get_adjacent(usr_email):
        aux = len(user_graph.get_adjacent(node))
        if aux:
            connections += aux-1

    context["nodes"] = len(user_graph.get_adjacent(usr_email))
    context["connections"] = connections

    client.close()

    workouts = []
    for workout in usr["workouts"]:

        total_volume = 0
        for exe in workout["exercises"]:
            total_volume += exe["sets"]*exe["reps"]*(1 if exe["weight"] == 0 else exe["weight"])

        workouts.append({
            "id": workout["id"],
            "date": workout["date"].strftime("%B %d, %Y"),
            "total_volume": total_volume,
            "exercises": workout["exercises"]
        })

    context["workouts"] = workouts
    context["first_name"] = usr["first_name"]
    context["last_name"] = usr["last_name"]

    return render(request=request, template_name="userprofiles/profile.html", context=context)


@login_required
def new_workout(request: Any):
    """
    Add new workout to a user profile
    :param request: the request passed in by the webview
    """
    context = {}

    if request.method == "POST":
        form = forms.workout_form(request.POST, error_class=forms.CustomError)

        if form.is_valid():
            data = form.cleaned_data

            request.session['new_workout_date'] = str(data['date'])
            request.session['new_workout_num_exercises'] = data['num_exercises']

            return redirect("userprofiles:add-exercises")
    else:
        form = forms.workout_form(error_class=forms.CustomError)

    context['form'] = form

    return render(request=request, template_name="userprofiles/new_workout.html", context=context)

@login_required
def add_exercises(request: Any):
    """
    Add a exercises to a workout
    """
    context = {}

    workout_date = datetime.datetime.strptime(request.session['new_workout_date'], "%Y-%m-%d")
    num_exercises = request.session['new_workout_num_exercises']
    add_exercises_formset_factory = formset_factory(forms.exercise_form, extra=num_exercises)

    if request.method == "POST":
        add_exercises_formset = add_exercises_formset_factory(request.POST)
        if add_exercises_formset.is_valid():
            new_workout = {
                "id": str(uuid.uuid4()).replace("-", ""),
                "date": workout_date,
                "exercises": []
            }
            for form in add_exercises_formset:
                data = form.cleaned_data

                new_exercise = {
                    "name": data["name"],
                    "sets": data["sets"],
                    "reps": data["reps"],
                    "weight": data["weight"]
                }

                new_workout["exercises"].append(new_exercise)

            client = MongoClient()
            user_collection = client["EDA-Project"]["user_profiles"]
            usr_email = request.user.email
            user_collection.update_one(
                {"email": usr_email},
                {"$push": {"workouts": new_workout}}
            )
            client.close()

            return redirect("userprofiles:profile")
    else:
        add_exercises_formset = add_exercises_formset_factory()

    context["formset"] = add_exercises_formset
    context["workout_date"] = workout_date.strftime("%B %d, %Y")

    return render(request=request, template_name="userprofiles/add_exercises.html", context=context)


@login_required
def edit_profile(request: Any):
    """
    Edit the profile of the current user
    """
    context = {}

    client = MongoClient()
    user_collection = client["EDA-Project"]["user_profiles"]
    usr_email = request.user.email
    usr = user_collection.find_one({"email": usr_email})

    if request.method == 'POST':
        form = forms.edit_profile_form(data=request.POST, username_placeholder=usr["username"], first_name_placeholder=usr["first_name"], last_name_placeholder=usr["last_name"], error_class=forms.CustomError)

        if form.is_valid():
            data = form.cleaned_data
            data["username"] = data["username"].strip()
            data["first_name"] = data["first_name"].strip()
            data["last_name"] = data["last_name"].strip()

            if data["username"] != "":
                user_collection.update_one(
                    {"email": usr_email},
                    {"$set": {"username": data["username"]}}
                )
                request.user.username = data["username"]
                request.user.save()
            if data["first_name"] != "":
                user_collection.update_one(
                    {"email": usr_email},
                    {"$set": {"first_name": data["first_name"]}}
                )
            if data["last_name"] != "":
                user_collection.update_one(
                    {"email": usr_email},
                    {"$set": {"last_name": data["last_name"]}}
                )

            client.close()

            return redirect("userprofiles:profile")
    else:
        form = forms.edit_profile_form(username_placeholder=usr["username"], first_name_placeholder=usr["first_name"], last_name_placeholder=usr["last_name"], error_class=forms.CustomError)

    context["form"] = form

    client.close()

    return render(request=request, template_name="userprofiles/edit_profile.html", context=context)


@login_required
def view_workout(request: Any):
    """
    View a specific usr workout
    """
    context = {}

    client = MongoClient()
    user_collection = client["EDA-Project"]["user_profiles"]
    usr_email = request.user.email
    usr = user_collection.find_one({"email": usr_email})
    client.close()

    if 'id' not in request.GET:
        return redirect("userprofiles:profile")

    rendr_workout = None
    for workout in usr['workouts']:
        if workout['id'] == request.GET['id']:
            print(workout)
            rendr_workout = {
                "date": workout["date"].strftime("%B %d, %Y"),
                "exercises": workout["exercises"],
            }
            break

    if not rendr_workout:
        return redirect("userprofiles:profile")

    context["workout"] = rendr_workout

    return render(request=request, template_name="userprofiles/view_workout.html", context=context)
