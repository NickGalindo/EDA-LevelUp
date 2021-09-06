from typing import List
from pymongo import MongoClient
import random
from hash import HashTable

def obtenerUsuariosVolumen(arregloVacio: List):

    ''' 
    Para obtener en un arreglo los nombres de los usuarios registrados para almacenarlos en una
    2-tupla junto con el volumen diario en la cantidad de días que se diga
    :param arregloVacio: para guardar ahí todas las 2-tuplas
    '''

    mongoClient = MongoClient('localhost',27017)

    db = mongoClient['EDA-Project']['auth_user']

    for x in db.find({},{'username':1}):

        arregloVolumen = [None]*10 #Se elige 100 dias como maximo, se pone 10 como prueba

        for i in range(len(arregloVolumen)):
            arregloVolumen[i] = random.randrange(100) #Se elige 100 como valor máximo de rango de Volumen

        arregloVacio.append((x['username'],arregloVolumen))


def insertarTablaHash(arregloLleno: List, tablaHash : HashTable):

    '''
    Para insertar en la tabla hash los usuarios registrados
    :param arregloLleno: arreglo de 2-tuplas compuesto por el nombre de usuario y el 
    arreglo de volumen
    :param tablaHash: tabla hash donde se guardarn todos los nombres de los usuarios y el 
    arreglo de volumen 
    '''

    for i in arregloLleno:
        tablaHash.set(i[0],i[1])

"""
arr = []
obtenerUsuariosVolumen(arregloVacio = arr)
print(arr)

h = HashTable(10)
insertarTablaHash(arregloLleno = arr, tablaHash = h)

for x in h.A:
    print(x)
"""  
