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
