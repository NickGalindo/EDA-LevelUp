from typing import Any

#Union find - Dynamic Compressed Disjoint Set implementation
class DisjointSet:
    def __init__(self):
        """
        Constructor for disjoint set
        """
        self.parent = {}
        self.rank = {}

    def add(self, key: str):
        """
        Add a new node to the disjoint set
        :param key: the key to be stored for this node
        """
        self.parent[key] = key
        self.rank[key] = 1

    def remove(self, key: str):
        """
        Remove a node from the set
        :param key: the key to be removed
        """
        self.parent.pop(key, None)
        self.rank.pop(key, None)


    def find(self, key: str):
        """
        find what graph the key belongs to
        :param key: the node find the union set of
        """
        if self.parent[key] == key:
            return key
        self.parent[key] = self.find(self.parent[key])
        return self.parent[key]

    def merge(self, keyA: str, keyB: str):
        """
        Merge two different union sets
        :param keyA: the key of the element of the first set to be merged
        :param keyB: the key of the element of the second set to be merged
        """
        keyA = self.find(keyA)
        keyB = self.find(keyB)

        if keyA == keyB:
            return

        if self.rank[keyA] > self.rank[keyB]:
            self.parent[keyB] = keyA
            return

        self.parent[keyA] = keyB
        if self.rank[keyA] == self.rank[keyB]:
            self.rank[keyB] += 1
        return

    def mongo_serialize(self, disjoint_set_collection: Any):
        """
        Convert the disjoint set into the smallest possible map to save into mongo
        :param disjoint_set_collection: the mongo collection to load the disjoint set into
        """
        for node_id in self.parent:
            if not disjoint_set_collection.find_one({"node_id": node_id}):
                disjoint_set_collection.insert_one({
                    "node_id": node_id,
                    "parent": self.parent[node_id],
                    "rank": self.rank[node_id]
                })
                continue
            disjoint_set_collection.update_one(
                {"node_id": node_id},
                {"$set": {
                    "parent": self.parent[node_id],
                    "rank": self.rank[node_id]
                }}
            )

    def mongo_deserialize(self, disjoint_set_collection: Any):
        """
        Convert a mongo saved dict to the sturcture
        :param disjoint_set_collection: the mongo collection to load the disjoint set from
        """
        print(self.parent)
        for doc in disjoint_set_collection.find({}):
            self.parent[doc["node_id"]] = doc["parent"]
            self.rank[doc["node_id"]] = doc["rank"]

    def __str__(self):
        """
        String representation of disjoint set
        """
        return str(self.parent)

    def __repr__(self):
        """
        Representation of disjoint set
        """
        return "DisjointSet< <"+str(self.parent)+">, <"+str(self.rank)+"> >"
