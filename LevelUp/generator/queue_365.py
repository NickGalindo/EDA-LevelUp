import json
import random
import time

from structures.queue_array import Queue_Array
from structures.queue import Queue


def queue_workouts(option : int, n : int = 0):
    """
    blabla
    """

    data_file = open("generator/data.json")
    data = json.load(data_file)

    start =  time.perf_counter()

    if option: #queue_array
        queue = Queue_Array(n)

        for i in range(n):
            exercise = random.choice(data["random_exercises"])

            queue.push(exercise)

            if(i%10000 == 0):
                print("batch",i)



    else: #queue_references
        queue = Queue()

        for i in range(n):
            exercise = random.choice(data["random_exercises"])

            queue.push(exercise)

            if(i%10000 == 0):
                print("batch",i)

    end = time.perf_counter()

    print(f"Push {n} elements took {end-start:0.4f} seconds")

    print()

    while True:
        b = input(" \n Have you exercised?: yes/no \n")

        if(b=="yes"):
            try:
                n = days = int(input("How many days?\n"))
            except ValueError as e:
                print("Invalid Data")
                continue

            start =  time.perf_counter()

            while(days):
                try:
                    queue.pop()
                except IndexError as e:
                    print("All of queue popped, queue now empty!")
                    break
                days -=1

            end = time.perf_counter()
            print(f"Pop {n-days} elements took {end-start:0.4f} seconds \n")

        elif b=="no":
            exit = input("Exit ? yes/no \n")
            if exit =="yes":
                break
            if exit != "no":
                print("Invalid data")
        else:
            print("Invalid data")
