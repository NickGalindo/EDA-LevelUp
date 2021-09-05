from django.contrib.auth.models import User
import json
import random
from pymongo import MongoClient
from typing import List
import datetime
import pymongo

def generate_users():
    '''
    Genera usuarios al azar y sin repetir con volumen
    '''
    usuario = " "
    email = usuario + "@gmail.com"
    username = usuario
    password = usuario + "123"
    user = User.objects.create_user(username, email, password) #create the user object
    user.save()
    client = MongoClient()
    user_collection = client["EDA-Project"]["user_profiles"]
    user_collection.insert_one({
    "email": email,
    "username": username,
    "profile_image": None,
    "workouts": create_workout()
    })
    client.close()

def prueba_user():
    # username email password
    usuario = " "
    email = usuario + "@gmail.com"
    username = usuario
    password = usuario + "123"
    user = User.objects.create_user(username, email, password) #create the user object
    user.save()
    client = MongoClient()
    user_collection = client["EDA-Project"]["user_profiles"]
    user_collection.insert_one({
    "email": email,
    "username": username,
    "profile_image": None,
    "workouts": create_workout()
    })
    client.close()

def create_workout():
    '''
    Crea una lista con el contenido de workouts
    '''
    data_file = open("generator/data.json",)
    data = json.load(data_file)
    exercises_list = []
    name_list = []
    for j in range(random.randint(1,10)):
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
def createUsers():
    """
    Create the users and add them into djangoooo
    """
    data_file = open("generator/data.json",)
    data = json.load(data_file)

    users = set()
    bulk_insert = []

    print("Creando usuarios unicos...")
    for i in range(100000000):
        name = _generateUsername(data["random_words"], 3)
        while name in users:
            name = _generateUsername(data["random_words"], 3)

        users.add(name)

        if i%10000 == 0:
            print("Batch de usuarios creados: "+str(i))

    """
    mongo_client = pymongo.MongoClient('localhost', 27017)
    db = mongo_client["EDA-Project"]
    app_data = db["app_data"]
    col = db["user_data"]

    print("Insertando usuarios e info a base de datos... porfavor esperar")
    col.insert_many(bulk_insert)
    print("Insercion terminada... proceso terminado")

    app_data.insert({
        "users_created": True
    })
    print("Se crearon "+str(len(bulk_insert))+" usuarios")
    """
    return users

def usersExist():
    """
    Verify if the users have been created
    :returns: returns true if the users exist, false otherwise
    """
    mongo_client = pymongo.MongoClient('localhost', 27017)
    db = mongo_client["EDA-Project"]
    app_data = db["app_data"]
    query = app_data.find_one({"users_created": {'$exists': 1}})

    if query:
        if query["users_created"]:
            print("Usuarios ya fueron creados")
            return True

    return False

def specialUsersExist():
    """
    Verify if the special users have been created
    :returns: returns true if special users exist false otherwise
    """
    mongo_client = pymongo.MongoClient('localhost', 27017)
    db = mongo_client["EDA-Project"]
    app_data = db["app_data"]
    query = app_data.find_one({"special_users_created": {'$exists': 1}})

    if query:
        if query["special_users_created"]:
            print("Usuarios especiales ya fueron creados")
            return True

    return False

def createSpecialUsers():
    """
    Make special users big_daddy and big_momma with a lot of data
    """
    data_file = open("generator/data.json",)
    data = json.load(data_file)

    #big_daddy = User.objects.create_user(username="big_daddy", password="default_123")
    #big_momma = User.objects.create_user(username="big_momma", password="default_123")

    big_daddy_data = {
        #"_id": big_daddy.id,
        "username": "big_daddy",
        "workouts": []
    }
    big_momma_data = {
        #"_id": big_momma.id,
        "username": "big_momma",
        "workouts": []
    }

    start_date = datetime.date(1900, 1, 1)
    end_date = datetime.date(2021, 4, 24)
    date_diff = (end_date-start_date).days

    for i in range(1000000):
        temp_daddy_data = {"date": start_date+datetime.timedelta(days=random.randrange(date_diff)), "exercises": []}
        temp_momma_data = {"date": start_date+datetime.timedelta(days=random.randrange(date_diff)), "exercises": []}

        for j in range(random.randint(1, 10)):
            aux = {
                "name": random.choice(data["random_exercises"]),
                "sets": random.randint(1, 10),
                "reps": random.randint(1, 20),
                "rpm": random.randint(1, 10)
            }
            temp_daddy_data["exercises"].append(aux)

        for j in range(random.randint(1, 10)):
            aux = {
                "name": random.choice(data["random_exercises"]),
                "sets": random.randint(1, 10),
                "reps": random.randint(1, 20),
                "rpm": random.randint(1, 10)
            }
            temp_momma_data["exercises"].append(aux)

        big_daddy_data["workouts"].append(temp_daddy_data)
        big_momma_data["workouts"].append(temp_momma_data)

        if i%10000:
            print("batch", i)

    return {"big_daddy_data": big_daddy_data, "big_momma_data":big_momma_data}

    """
    mongo_client = pymongo.MongoClient('localhost', 27017)
    db = mongo_client["EDA-Project"]
    app_data = db["app_data"]
    col = db["user_data"]

    print("Insertando usuarios e info a base de datos... porfavor esperar")
    col.insert_many([big_daddy_data, big_momma_data])

    app_data.insert({
        "special_users_created": True
    })
    print("Insercion terminada... proceso terminado")
    """

# Run if run as main
if __name__ == "__main__":
    #createUsers()
    insert_volume()
