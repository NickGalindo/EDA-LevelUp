'''
Funcion increase level extraer los volumenes de todos los usuarios en un nivel y agregarlos a una estructura
'''

import time
from pymongo import MongoClient
from structures.avl import AVLTree
from structures.max_heap import MaxHeap
import random
import datetime

random_exercises = [
    "pushups",
    "pullups",
    "deadlifts",
    "squats",
    "bench press",
    "incline bench press",
    "pulldowns",
    "barbell rows",
    "overhead press",
    "lateral raises",
    "tricep pushdowns",
    "bicep curls",
    "hammer curls",
    "dips",
    "tricep extensions",
    "hip thrusts",
    "bulgarian split squats",
    "skullcrushers",
    "concentration curls",
    "chest fly",
    "flat dumbbell press",
    "incline dumbbell press",
    "rear delt fly",
    "simgle arm dumbbell rows",
    "dumbbell pullovers",
    "calve extensions",
    "leg extensions",
    "hamstring curls",
    "ez bar curls",
    "facepulls",
    "leg press",
    "t-bar rows"
]

# list_users = [[email, volumen],[],...]
def insert_volume(list_users,varcoleccion):
    #Generador de volumenes
    
    for i in list_users:
        workouts = [
            {
                "date": datetime.datetime.today(),
                "exercises": [
                    {
                        "name":random.choice(random_exercises),
                        "sets":random.randint(1,10),
                        "reps":random.randint(1,100),
                        "rpm":random.randint(1,1000)
                    }
                ]
            }
        ]
        varcoleccion.update_one({"email":i[0]},{"$set": {"workouts":workouts}})

    #for i in randint(1,10):
    #    append()
    return

def extract_volume(volume_dict):
    return volume_dict["sets"]*volume_dict["reps"] + volume_dict["rpm"]

def extract_users():
    client = MongoClient()
    db = client['EDA-Project']
    coleccion = db['user_profiles']
    users = coleccion.find()
    list_volume_users = []
    
    for i in users:
        tmp_list = []
        #Guardamos los workouts
        tmp_list.append(extract_volume(i["workouts"][0]["exercises"][0]))
        #Guardamos el email
        tmp_list.append(i["email"])
        #tmp_list.append(extract_volume( ))
        list_volume_users.append(tmp_list)

    #insert_volume(list_volume_users, coleccion)

    return list_volume_users


def use_structures(structure = "both"):

    users_volumes = extract_users()

    if structure in ["avl", "both"] :

        avl = AVLTree()

        for i in users_volumes:
            avl.insert(i)

        print("Los usuarios que suben de nivel son:")
        print(avl.ExtractMaxValues())
   
    if structure in ["heap", "both"]:

        heap = MaxHeap(10)
        for i in users_volumes:
            heap.insert(i)
    
        print("Los usuarios que suben de nivel son:")
        print(heap.ExtractMaxValues())

    return

if __name__ == "__main__":
    print(extract_users())
    print(len(extract_users()))
