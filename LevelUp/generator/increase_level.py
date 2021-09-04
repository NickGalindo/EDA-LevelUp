'''
Funcion increase level extraer los volumenes de todos los usuarios
en un nivel y agregarlos a una estructura
'''

import time
import random
import datetime
from pymongo import MongoClient
from structures.avl import AVLTree
from structures.max_heap import MaxHeap

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
def insert_volume():
    '''
    Esta funcion genera volumenes para todos los usuarios de forma aleatoria
    '''
    client = MongoClient()
    db = client['EDA-Project']
    coleccion = db['user_profiles']
    users = coleccion.find()

    for i in users:
        exercises_list = []
        name_list = []
        for j in range(random.randint(2,10)):
            name = random.choice(random_exercises)
            while name in name_list:
                name = random.choice(random_exercises)
            name_list.append(name)

            exercises_list.append({
                        "name": name,
                        "sets": random.randint(1,10),
                        "reps": random.randint(1,200),
                        "weight": random.randint(1,250)
                })

        workouts = [
            {
                "date": datetime.datetime.today(),
                "exercises":  exercises_list
            }
        ]
        coleccion.update_one({"email":i["email"]},{"$set": {"workouts":workouts}})

def extract_volume(volume_dict):
    suma = 0
    for exe in volume_dict:
        suma += exe["sets"]*exe["reps"]*(1 if exe["weight"] == 0 else exe["weight"])

    return suma

def extract_users():
    client = MongoClient()
    db = client['EDA-Project']
    coleccion = db['user_profiles']
    users = coleccion.find()
    list_volume_users = []
    
    for i in users:
        tmp_list = []
        #Guardamos el email
        if len(i["workouts"]) == 0:
            continue
        if extract_volume(i["workouts"][0]["exercises"]) == 0:
            continue
        last = len(i["workouts"]) - 1
        tmp_list.append(extract_volume(i["workouts"][last]["exercises"]))
        tmp_list.append(i["email"])
        #tmp_list.append(i["workouts"])
        #Guardamos los workouts
        list_volume_users.append(tmp_list)

    #debug
    #print(list_volume_users)

    return list_volume_users


#number_promote << min_users_req
def use_structures(structure = "both", number_promote = 3, min_users_req = 3):

    users_volumes = extract_users()
    list_promote_users_avl = []
    list_promote_users_heap = []

    if len(users_volumes) < number_promote or len(users_volumes) < min_users_req:
        return list_promote_users_heap

    if structure in ["avl", "both"] :

        start_avl = time.perf_counter()

        avl = AVLTree()

        for i in users_volumes:
            avl.insert(i)
        
        for i in range(number_promote):
            list_promote_users_avl.append(avl.ExtractMaxValues())
        end_avl = time.perf_counter()

        print("\n\nAVL:\n")
        #avl.representation()
        print("Los usuarios que suben de nivel son:")
        print(list_promote_users_avl)
        print(f"Tiempo de ejecucion: {end_avl-start_avl:0.5f} segundos")
   
    if structure in ["heap", "both"]:

        start_heap = time.perf_counter()
        heap = MaxHeap(10)
        for i in users_volumes:
            heap.insert(i)
    
        for i in range(number_promote):
            list_promote_users_heap.append(heap.ExtractMaxValues())
        end_heap = time.perf_counter()

        print("\n\nHeap:\n")
        #print(repr(heap))
        print("Los usuarios que suben de nivel son:")
        print(list_promote_users_heap)
        print(f"Tiempo de ejecucion: {end_heap-start_heap:0.5f} segundos")

    if structure == "avl":
        return list_promote_users_avl
    return list_promote_users_heap

if __name__ == "__main__":
    #insert_volume()
    use_structures()
    #print(extract_users())
    #print(len(extract_users()))
