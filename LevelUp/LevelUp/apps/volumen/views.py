from django.http import request
from django.shortcuts import render

from typing import List, Any
from pymongo import MongoClient
import random
import json
from structures.hash import HashTable

def obtenerVolumen(user :Any):
    '''
    funcion para obtener Todos lo volúmenes
    '''
    mongoClient = MongoClient('localhost',27017)
    db = mongoClient['EDA-Project']['user_profiles']
    arr_workouts = db.find_one({'username': user})['workouts']
    volumes = []

    for work in arr_workouts:
        current_vol =0
        exercises = work["exercises"]
        
        for ex in exercises:
            current_vol += ex['sets'] *ex['reps']*ex['weight']

        volumes.append(current_vol)

    return volumes
def exercises(n,user):
     '''
        funcion para hashear los ejercicios donde llave es el nombre 
        y valor es el número de veces 
     '''

     mongoClient = MongoClient('localhost',27017)
     db = mongoClient['EDA-Project']['user_profiles']
     arr_workouts = db.find_one({'username': user})['workouts']

     myHashExercises = HashTable(n)
     total = 0

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

     return (myHashExercises,total)

def cantidadEjercicios(data, hashedExercises,total):
    '''funcion que retorna lista de tuplas (nombre ejercicio, porcentaje de veces con respecto al total)
        lista de tuplas de ejercicio y su procentaje de veces
    '''
    l = []

    for exercise in data:
        if hashedExercises.hasKey(exercise):
            porcentaje = round( hashedExercises.get(exercise)/total*100, 2) 
            l.append( (exercise, porcentaje) )
    
    return l


def VolumeHistory(request : Any):

    mongoClient = MongoClient('localhost',27017)
    db = mongoClient['EDA-Project']['auth_user']

    data_file = open("generator/data.json",)
    data = json.load(data_file)
    #arreglo con tuplas (nombre usuario, volúmenenes[] )
    key_values = []
    #Tabla hash de tamaño n que almacenará las llave/valor 
    myHash = HashTable(2000)


    #este ciclo calcula los volumenes de los usuarios 
    for user_info in db.find({"username" : str(request.user)},{'username':1}):
        
        volumen_ususario = obtenerVolumen(user_info['username'])
        key_values.append( (user_info['username'], volumen_ususario) )
    
    #Tabla hash que hashea a todos los usuarios de la bd
    for user in key_values:
        myHash.set(user[0],user[1])

    '''
        segunda implementación de tabla hash
        almacena en una tabla hash las llaves que son los nombres de los ejercicios
        y los valores son los números de veces que los ha hecho
    '''

    hashedExercises,total =exercises(15,str(request.user))
    
    #lsita de tuplas (nombre ejercicio, porcentaje veces con respecto al total)
    list_exercices  = cantidadEjercicios(data['random_exercises'],hashedExercises,total)


    context = {'title': 'Volume History', 'volumes': myHash.get(str(request.user)), 'exercises': list_exercices, 'total': total}
    
    return render(request=request, template_name='volume/volume.html', context=context)





