from django.shortcuts import render

from typing import List, Any
from pymongo import MongoClient
import random
from structures.hash import HashTable


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

    '''for i in myHash.A:
        print(i)'''

    context = {'title': 'Volume History', 'volumes': myHash.get(str(request.user))}
    
    return render(request=request, template_name='volume/volume.html', context=context)





