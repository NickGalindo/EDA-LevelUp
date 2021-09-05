from django.http import request
from django.shortcuts import render

from typing import List, Any
from pymongo import MongoClient
import random
import json
from structures.hash import HashTable


def exercises(n,user):
     mongoClient = MongoClient('localhost',27017)
     db = mongoClient['EDA-Project']['user_profiles']
     myHashExercises = HashTable(n)
     arr_workouts = db.find_one({'username': user})['workouts']
     total = 0
     print(arr_workouts)

     for workout in arr_workouts:
         for exercise in workout['exercises']:
             name = exercise['name']
             times = exercise['sets']*exercise['reps']
             total += times
             

             if myHashExercises.hasKey(name):
                 current = myHashExercises.get(name)+times
                 myHashExercises.set(name,current)
             else:
                 myHashExercises.set(name,times)
         for i in myHashExercises.A:
             print(i)

     return (myHashExercises,total)


def cantidadEjercicios(data, hashedExercises,total):
    #lista de tuplas de ejercicio y su procentaje de veces
    l = []

    for exercise in data:
        if hashedExercises.hasKey(exercise):
            porcentaje = round( hashedExercises.get(exercise)/total*100, 2)
            l.append( (exercise,porcentaje) )
    
    return l





def VolumeHistory(request : Any):


    mongoClient = MongoClient('localhost',27017)
    db = mongoClient['EDA-Project']['auth_user']

    data_file = open("generator/data.json",)
    data = json.load(data_file)

    #arreglo con tuplas (nombre usuario, volúmenenes)
    key_values = []
    #Tabla hash de tamaño n que almacenará las llave/valor 
    myHash = HashTable(30)

    for user_info in db.find({},{'username':1}):

        # arreglo de los volúmenes generados 
        volumes = [random.randrange(100)+50 for i in range(10)]

        key_values.append( (user_info['username'],volumes) )
    
    #llenar la tabla hash
    for user in key_values:
        myHash.set(user[0],user[1])

    #hashedExercises,total =exercises(15,request.user)
    hashedExercises,total =exercises(15,"dave herrera")
    
    #print(hashedExercises,total)

    list_exercices  = cantidadEjercicios(data['random_exercises'],hashedExercises,total)

    print(list_exercices)
    context = {'title': 'Volume History', 'volumes': myHash.get(str(request.user)), 'exercises': list_exercices, 'total': total}
    
    return render(request=request, template_name='volume/volume.html', context=context)





