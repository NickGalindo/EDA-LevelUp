from typing import Any, Dict

#Dynamic adjacency list
class AdjacencyList:
    def __init__(self):
        """
        Constructor for the AdjacencyList
        """
        self.dynamic_list = {}

    def add_node(self, key: Any):
        """
        The node to add
        :param key: to add the node in
        """
        self.dynamic_list[key] = set()

    def connect(self, keyA: Any, keyB: Any):
        """
        connect two nodes by two keys
        :param keyA: the key of the first node
        :param keyB: the key of the second node
        """
        self.dynamic_list[keyA].add(keyB)
        self.dynamic_list[keyB].add(keyA)

    def delete_connection(self, keyA: Any, keyB: Any):
        """
        delete a connection between two nodes
        :param keyA: the key of the first node
        :param keyB: the key of the second node
        """
        if keyA in self.dynamic_list[keyB]:
            self.dynamic_list[keyB].remove(keyA)
        if keyB in self.dynamic_list[keyA]:
            self.dynamic_list[keyA].remove(keyB)

    def delete_node(self, key: Any):
        """
        delete a node in the dynamic list
        :param key: the key of the node to remove
        """
        for k in self.dynamic_list:
            if k == key:
                continue
            self.delete_connection(key, k)

        del self.dynamic_list[key]

    def get_adjacent(self, key: Any):
        """
        get all adjacent nodes to the node in a key
        :param key: the key of the node
        """
        return self.dynamic_list[key]

    def get_list(self):
        """
        get the list of all nodes in the adjacency list
        """
        return self.dynamic_list.keys()

    def mongo_serialize(self, adjacency_list_collection: Any):
        """
        Convert the adjacency list and save into mongo
        :param adjacency_list_collection: the collection to save the list into
        """
        for node in self.dynamic_list:
            if not adjacency_list_collection.find_one({"node": node}):
                adjacency_list_collection.insert_one({
                    "node": node,
                    "adjacents": list(self.dynamic_list[node])
                })
                continue
            adjacency_list_collection.update_one(
                {"node": node},
                {"$set": {
                    "adjacents": list(self.dynamic_list[node])
                }}
            )

    def mongo_deserialize(self, adjacency_list_collection: Any):
        """
        Convert the mongo data into an adjacency list
        :param adjacency_list_collection: the collection to load the list from
        """
        for doc in adjacency_list_collection.find({}):
            self.dynamic_list[doc["node"]] = set(doc["adjacents"])
