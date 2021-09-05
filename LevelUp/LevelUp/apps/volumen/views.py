from django.http import request
from django.shortcuts import render

from typing import List, Any
from pymongo import MongoClient
import random
from structures.hash import HashTable


def exercises(n,user):
     mongoClient = MongoClient('localhost',27017)
     db = mongoClient['EDA-Project']['user_profiles']
     myHashExercises = HashTable(n)
     arr_workouts = db.find_one({'email': user.email})['workouts']
     total = 0
     print(arr_workouts)

     for workout in arr_workouts:
         for exercise in workout['exercises']:
             name = exercise['name']
             times = exercise['sets']*exercise['reps']
             total += times
             #print(name,times)

             if myHashExercises.hasKey(name):
                 current = myHashExercises.get(name)+times
                 myHashExercises.set(name,current)
             else:
                 myHashExercises.set(name,times)

     return (myHashExercises,total)




def VolumeHistory(request : Any):


    mongoClient = MongoClient('localhost',27017)
    db = mongoClient['EDA-Project']['auth_user']

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

    hashedExercises,total =exercises(15,request.user)
    print(hashedExercises,total)

    l = []

    context = {'title': 'Volume History', 'volumes': myHash.get(str(request.user)), 'exercises': hashedExercises, 'total': total}
    
    return render(request=request, template_name='volume/volume.html', context=context)





