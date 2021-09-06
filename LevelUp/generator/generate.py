from django.contrib.auth.models import User
import json
import random
from pymongo import MongoClient
from typing import List
import datetime
import pymongo
import uuid

def generate_users():
    '''
    Genera usuarios con volumen. username al azar y sin repetirse
    '''
    users = createUsers(100000)
    client = MongoClient()
    user_collection = client["EDA-Project"]["user_profiles"]
    count = 0
    for usuario in users:
        count += 1
        #creacion de usuario en django
        email = usuario + "@gmail.com"
        username = usuario
        password = usuario + "123"
        user = User.objects.create_user(username, email, password) #create the user object
        user.save()
        #insercion de usuario en mongodb en coleccion user_profiles
        user_collection.insert_one({
            "email": email,
            "username": username,
            "first_name": "",
            "last_name": "",
            "profile_image": None,
            "workouts": create_workout()
        })
        if count%1000 == 0:
            print("Batch de usuarios creados: "+str(count))
    client.close()

def create_workout():
    '''
    Crea una lista con el contenido de workouts
    '''
    data_file = open("generator/data.json",)
    data = json.load(data_file)
    workouts = []
    for i in range(15):
        exercises_list = []
        name_list = []
        for j in range(random.randint(5,10)):
            name = random.choice(data["random_exercises"])
            while name in name_list:
                name = random.choice(data["random_exercises"])
            name_list.append(name)

            exercises_list.append({
                        "name": name,
                        "sets": random.randint(1,10),
                        "reps": random.randint(1,50),
                        "weight": random.randint(1,100)
                })

        workouts.append({
                "id": str(uuid.uuid4()).replace("-", ""),
                "date": datetime.datetime.today(),
                "exercises": exercises_list
            })

    return workouts

# list_users = [[email, volumen],[],...]
def insert_volume():
    '''
    Esta funcion genera volumenes para todos los usuarios de forma aleatoria
    '''
    data_file = open("generator/data.json",)
    data = json.load(data_file)
    client = MongoClient()
    db = client['EDA-Project']
    coleccion = db['user_profiles']
    users = coleccion.find()

    for i in users:
        exercises_list = []
        name_list = []
        for j in range(random.randint(2,10)):
            name = random.choice(data["random_exercises"])
            while name in name_list:
                name = random.choice(data["random_exercises"])
            name_list.append(name)

            exercises_list.append({
                        "name": name,
                        "sets": random.randint(1,10),
                        "reps": random.randint(1,50),
                        "weight": random.randint(1,100)
                })

        workouts = [
            {
                "date": datetime.datetime.today(),
                "exercises":  exercises_list
            }
        ]
        coleccion.update_one({"email":i["email"]},{"$set": {"workouts":workouts}})
    client.close()

# Generate Uniques
def _generateUsername(words: List[str], size: int, cnt: int=1):
    """
    generate unique username recursively
    :param words: list of words to be picked from
    :param cnt: count of words added
    :param size: size of username
    """
    return random.choice(words) + ("_"+_generateUsername(words, size, cnt=cnt+1) if cnt != size else "")

# Generate multiple users with some data for them
def createUsers(numberofusers = 10000):
    """
    Create the users and add them into djangoooo
    """
    data_file = open("generator/data.json",)
    data = json.load(data_file)

    users = set()

    print("Creando usuarios unicos...")
    for i in range(numberofusers):
        name = _generateUsername(data["random_words"], 3)
        while name in users and usersExist(name):
            name = _generateUsername(data["random_words"], 3)
        users.add(name)

    return users

def usersExist(user_name):
    """
    Verify if the users have been created
    :returns: returns true if the users exist, false otherwise
    """
    mongo_client = pymongo.MongoClient('localhost', 27017)
    db = mongo_client["EDA-Project"]
    user_data = db["user_profiles"]
    query = user_data.count_documents({"username":user_name})
    mongo_client.close()
    if query:
        return True
        #print("Usuarios ya fueron creados")
    return False
