from typing import List, Dict, Any
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory
from generator.generate import generate_users
from pymongo import MongoClient
import datetime
import time
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
    usr_email = request.user.email
    usr = user_collection.find_one({"email": usr_email})

    workouts = []
    for workout in usr["workouts"]:

        total_volume = 0
        for exe in workout["exercises"]:
            total_volume += exe["sets"]*exe["reps"]*(1 if exe["weight"] == 0 else exe["weight"])

        workouts.append({
            "date": workout["date"].strftime("%B %d, %Y"),
            "total_volume": total_volume,
            "exercises": workout["exercises"]
        })

    context["workouts"] = workouts

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
def generate(request: Any):
    '''
    Funcion generadora de usuarios
    '''
    generate_users()
    print("Usuarios generados :)")

    return redirect("userprofiles:profile")
