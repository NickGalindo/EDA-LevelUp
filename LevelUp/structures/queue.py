from typing import Any

#Node for queue class
class _Node:
    def __init__(self, val: Any=None, next: Any=None):
        """
        Constructor for Node class
        :param val: the value of the Node
        :param next: the next node in the list
        """
        self.val = val
        self.next = next

    def __str__(self):
        """
        return string representation of Node
        """
        return str(self.val)+((", "+str(self.next))  if self.next else "")

    def __repr__(self):
        """
        Return representation of node
        """
        return repr(self.val)+((", "+repr(self.next))  if self.next else "")

#Queue implementation for class
class Queue:
    def __init__(self):
        """
        Constructor for queue
        """
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, val: Any):
        """
        Pushes a new element into the queue
        :param val: The value to be pushed
        """
        if self.size == 0:
            self.head = _Node(val=val)
            self.tail = self.head
            self.size += 1
            return

        self.tail.next = _Node(val=val)
        self.tail = self.tail.next
        self.size += 1
        return

    def pop(self):
        """
        Remove an element from Queue and return its value
        """
        if self.size <= 0:
            raise IndexError("Queue is empty, cannot pop")
            return

        aux = self.head
        self.head = aux.next
        self.size -= 1
        return aux.val

    def front(self):
        """
        Get the first element in the queue
        """
        if self.size == 0:
            raise IndexError("Queueu is empty, cannot get front element")
        return self.head.val

    def __len__(self):
        """
        Returns the size of the current queue
        """
        return self.size

    def __str__(self):
        """
        Returns string representation of queue
        """
        return (str(self.head) if self.head else "")

    def __repr__(self):
        """
        Returns representation of queue
        """
        return "Queue<"+(repr(self.head) if self.head else "")+">"
