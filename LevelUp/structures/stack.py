from typing import Any

#Node class for stack
class _Node():
    def __init__(self, val: Any=None, next:Any=None):
        """
        Constructor for Node class
        :param val: value to be stored in node
        :param next: next node in list
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


#Stack class implementation
class Stack():
    def __init__(self):
        """
        Constructor for Stack
        """
        self.head = None
        self.size = 0

    def push(self, val: Any):
        """
        push a value into the stack
        :param val: value to be pushed
        """
        aux = _Node(val=val, next=self.head)
        self.head = aux
        self.size += 1

    def pop(self):
        """
        Pop the first element in stack
        """
        if self.size <= 0:
            raise IndexError("Stack is empty, cannot pop")
            return

        aux = self.head
        self.head = aux.next
        self.size -= 1
        return aux.val

    def top(self):
        """
        returns top element from stack
        """
        if self.size <= 0:
            raise IndexError("Stack is empty, nothing at top")
            return
        return self.head.val

    def __len__(self):
        """
        returns size of stack
        """
        return self.size

    def __str__(self):
        """
        returns string representation of stack
        """
        return (str(self.head) if self.head else "")

    def __repr__(self):
        """
        returns representation of stack
        """
        return "Stack<"+(repr(self.head) if self.head else "")+">"
