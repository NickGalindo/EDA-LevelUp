from pymongo import MongoClient
from structures.adjacency_list import AdjacencyList
from structures.disjoint_set import DisjointSet

nodes = [
    "Beginner",
    "Intermediate",
    "Advanced",
    "Legs Beginner",
    "Legs Intermediate",
    "Legs Advanced",
    "Pull Beginner",
    "Pull Intermediate",
    "Pull Advanced",
    "Push Beginner",
    "Push Intermediate",
    "Push Advanced",
    "Arms Beginner",
    "Arms Intermediate",
    "Arms Advanced",
    "Back and Chest Beginner",
    "Back and Chest Intermediate",
    "Back and Chest Advanced",
    "Upper Body Beginner",
    "Upper Body Intermediate",
    "Upper Body Advanced",
    "Lower Body Beginner",
    "Lower Body Intermediate",
    "Lower Body Advanced",
    "5x5 Beginner",
    "5x5 Intermediate",
    "5x5 Advanced",
    "Smolov Squats",
    "Smolov Bench",
    "Smolov Deadlfits"
]

if __name__ == "__main__":
    adl = AdjacencyList()

    for node in nodes:
        adl.add_node(node)

    for nodeA in nodes:
        for nodeB in nodes:
            if "Beginner" in nodeA and "Beginner" in nodeB:
                adl.connect(nodeA, nodeB)
                continue
            if "Intermediate" in nodeA and "Intermediate" in nodeB:
                adl.connect(nodeA, nodeB)
                continue
            if "Advanced" in nodeA and "Advanced" in nodeB:
                adl.connect(nodeA, nodeB)
                continue

    cnt = 0
    prev = ""
    for node in nodes:
        if cnt == 2:
            cnt = 0
            prev = node
            continue
        if prev == "":
            prev = node
            continue
        adl.connect(prev, node)
        cnt += 1
        prev = node

    adl.connect("Advanced", "Smolov Squats")
    adl.connect("Advanced", "Smolov Deadlfits")
    adl.connect("Advanced", "Smolov Bench")

    dj_set = DisjointSet()
    for node in nodes:
        dj_set.add(node)

    user_graph = AdjacencyList()
    for node in nodes:
        user_graph.add_node(node)

    client = MongoClient()
    adjacency_list_collection = client["EDA-Project"]["adjacency_list"]
    disjoint_set_collection = client["EDA-Project"]["disjoint_set"]
    user_graph_collection = client["EDA-Project"]["user_graph"]

    adl.mongo_serialize(adjacency_list_collection)
    dj_set.mongo_serialize(disjoint_set_collection)
    user_graph.mongo_serialize(user_graph_collection)

    client.close()
