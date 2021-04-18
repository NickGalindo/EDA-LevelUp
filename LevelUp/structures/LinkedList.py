from typing import List, Any

#Node class fr linked list
class _Node:
    def __init__(self, val: Any=None, next: Any=None):
        """
        Constructor
        :param val: value of node
        :param next: next node in link
        """
        self.val = val
        self.next = next

    def build_from_list(self, build_list: List[Any], pos: int):
        """
        Build a the linked list efficiently from a list
        :param build_list: the list to be built from
        :param pos: current position in list
        """
        if pos >= len(build_list):
            return self

        self.next = _Node(val=build_list[pos])
        return self.next.build_from_list(build_list, pos+1)

    def __str__(self):
        """
        Return string representation of linked list
        """
        return str(self.val)+((", "+str(self.next))  if self.next else "")

#linked list implemented using references
class LinkedList_References:
    def __init__(self, build_list: List[Any]=None):
        """
        Constructor
        :param build_list:
        """
        self.head = None
        self.last = None
        self.size = 0

        if build_list:
            self.build_from_list(build_list)
            self.size = len(build_list)

    def build_from_list(self, build_list: List[Any]):
        """
        Build linked list efficiently from a list
        :param build_list: The list to be built from
        """
        try:
            self.head = _Node(val=build_list[0])
        except IndexError:
            print("WARNING: Tried to build LinkedList_Reference from empty list!")
            return

        self.last = self.head.build_from_list(build_list, 1)

    def push_back(self, val: Any):
        """
        Push an element into the back of the linked list
        :param val: value to be pushed
        """
        aux = self.last
        aux.next = _Node(val=val)
        self.last = aux.next

    def push_front(self, val: Any):
        """
        Push an element into the front of the linked list
        :param val: value to be pushed
        """
        aux = self.head
        self.head = _Node(val=val)
        self.head.next = aux

    def __str__(self):
        """
        Return string representation of linked list
        """
        return "LinkedList_References<"+str(self.head)+">"
