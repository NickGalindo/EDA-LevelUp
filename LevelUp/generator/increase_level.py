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

def extract_volume(volume_dict):
    suma = 0
    for exe in volume_dict:
        suma += exe["sets"]*exe["reps"]*(1 if exe["weight"] == 0 else exe["weight"])

    return suma

def extract_users(max_users = None):
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
        if max_users and len(list_volume_users) >= max_users:
            break

    #debug
    #print(list_volume_users)

    return list_volume_users


#number_promote << min_users_req
def use_structures(max_users = 10000, structure = "both", number_promote = 100, min_users_req = 1000):

    if max_users :
        users_volumes = extract_users(max_users)
        print("\nMaximo numero de usuarios manejados: ", max_users, end="")
    else:
        users_volumes = extract_users()
    list_promote_users_avl = []
    list_promote_users_heap = []

    if len(users_volumes) < number_promote or len(users_volumes) < min_users_req:
        return list_promote_users_heap

    if structure in ["avl", "both"] :

        print("\n\nAVL:\n")

        start_avl = time.perf_counter()

        start_avl_create = time.perf_counter()
        avl = AVLTree()
        end_avl_create = time.perf_counter()
        print(f"Tiempo de creacion : {end_avl_create-start_avl_create:0.5f} segundos")

        start_avl_insert = time.perf_counter()
        for i in users_volumes:
            avl.insert(i)
        end_avl_insert = time.perf_counter()
        print(f"Tiempo de insercion : {end_avl_insert-start_avl_insert:0.5f} segundos")
        start_avl_extract = time.perf_counter()
        for i in range(number_promote):
            list_promote_users_avl += avl.ExtractMaxValues()
        end_avl_extract = time.perf_counter()
        print(f"Tiempo de extraccion : {end_avl_extract-start_avl_extract:0.5f} segundos")

        end_avl = time.perf_counter()

        #avl.representation()
        #print("Los usuarios que suben de nivel son:")
        #print(list_promote_users_avl)
        print(f"Tiempo de ejecucion: {end_avl-start_avl:0.5f} segundos")
   
    if structure in ["heap", "both"]:

        print("\n\nHeap:\n")

        start_heap = time.perf_counter()

        start_heap_create = time.perf_counter()
        heap = MaxHeap(len(users_volumes))
        end_heap_create = time.perf_counter()
        print(f"Tiempo de creacion : {end_heap_create-start_heap_create:0.5f} segundos")

        start_heap_insert = time.perf_counter()
        for i in users_volumes:
            heap.insert(i)
        end_heap_insert = time.perf_counter()
        print(f"Tiempo de insercion : {end_heap_insert-start_heap_insert:0.5f} segundos")
    
        start_heap_extract = time.perf_counter()
        for i in range(number_promote):
            list_promote_users_heap += heap.ExtractMaxValues()
        end_heap_extract = time.perf_counter()
        print(f"Tiempo de extraccion : {end_heap_extract-start_heap_extract:0.5f} segundos")
        end_heap = time.perf_counter()

        #print(repr(heap))
        #print("Los usuarios que suben de nivel son:")
        #print(list_promote_users_heap)
        print(f"Tiempo de ejecucion: {end_heap-start_heap:0.5f} segundos")

    if structure == "avl":
        return list_promote_users_avl
    return list_promote_users_heap

if __name__ == "__main__":
    #Es necesario no borrar esto o explota
    use_structures()
    #print(extract_users())
    #print(len(extract_users()))
