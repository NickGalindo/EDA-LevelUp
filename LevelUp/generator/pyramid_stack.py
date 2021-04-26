import json
import random
import time

from structures.stack import Stack

def generate_workout(n : int):

    pyramid = Stack()
    data_file = open("generator/data.json")
    data = json.load(data_file)

    #apilando
    start_stack = time.perf_counter()   

    for i in range(n):
        exercise = random.choice(data["random_exercises"])
        pyramid.push(exercise)

        if (i%10000==0):
            print("batch",i)
    
    end_stack = time.perf_counter()
    
    #desapilando

    start_unstack = time.perf_counter()
    while(pyramid.size>0):
        current_exercise = pyramid.pop()


        if(pyramid.size%10000 == 0):
            print("se han desapilado: ", (n-pyramid.size))

    
    end_unstack = time.perf_counter()

    
    print(f"Stack time in {end_stack-start_stack:0.4f} seconds")
    print(f"Unstack time in {end_unstack-start_unstack:0.4f} seconds")
    



    

