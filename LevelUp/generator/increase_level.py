'''
Funcion increase level extraer los volumenes de todos los usuarios en un nivel y agregarlos a una estructura
'''

import time
from structures.avl import AVLTree
from structures.max_heap import MaxHeap

def extract_users():
    list_volume_users = []




    return list_volume_users

def use_structures(structure = "both"):

    #users_volumes = extract_users()

    if structure in ["avl", "both"] :

        avl = AVLTree()

        for i in users_volumes:
            avl.insert(i)

        print("Los usuarios que suben de nivel son:")
    
    if structure in ["heap", "both"]:

        heap = MaxHeap()
        for i in users_volumes:
            heap.insert(i)
    
        print("Los usuarios que suben de nivel son:")

    return