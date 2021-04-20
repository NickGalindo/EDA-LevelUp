from typing import List, Any

#Node class fr linked list
class _Node:
    def __init__(self, val: Any=None, next: Any=None, prev: Any=None):
        """
        Constructor
        :param val: value of node
        :param next: next node in link
        :param prev: previous node in link
        """
        self.val = val
        self.next = next
        self.prev = prev

    def build_from_list(self, build_list: List[Any], pos: int):
        """
        Build a the linked list efficiently from a list
        :param build_list: the list to be built from
        :param pos: current position in list
        """
        if pos >= len(build_list):
            return self

        self.next = _Node(val=build_list[pos], prev=self)
        return self.next.build_from_list(build_list, pos+1)

    def get_backward(self, pos: int, cur: int):
        """
        Get an element at a certain position iterating backwards
        :param pos: position to get
        :param cur: current position
        """
        if pos == cur:
            return self.val

        return self.prev.get_backward(pos, cur-1)

    def get_forward(self, pos: int, cur: int):
        """
        Get an element at a certin position iterating forward
        :param pos: position to get
        :para, cur: current position
        """
        if pos == cur:
            return self.val

        return self.next.__get_forward(pos, cur+1)

    def insert_forward(self, val: Any, pos: int, cur: int):
        """
        Insert element at certain position iterating forward
        :param val: value to be inserted
        :param pos: position to be inserted into
        :param cur: current position
        """
        if pos == cur:
            aux = _Node(val=val, next=self, prev=self.prev)
            self.prev.next = aux
            self.prev = aux
            return

        self.next.insert_forward(val, pos, cur+1)
        return

    def insert_backward(self, val: Any, pos: int, cur: int):
        """
        Insert element at certain position iterating backward
        :param val: value to be inserted
        :param pos: position to be inserted into
        :param cur: current position
        """
        if pos == cur:
            aux = _Node(val=val, next=self, prev=self.prev)
            self.prev.next = aux
            self.prev = aux
            return

        self.next.insert_backward(val, pos, cur-1)
        return

    def remove_forward(self, pos: int, cur: int):
        """
        Remove an element from linked list at specific position iterating forwards
        :param pos: position to remove from
        :param cur: currrent position in list
        """
        if pos == cur:
            self.prev.next = self.next
            self.next.prev = self.prev
            return self.val

        return self.next.remove_forward(pos, cur+1)

    def remove_backward(self, pos: int, cur: int):
        """
        Remove an element from linked list at specific positino iterating backwards
        :param pos: position to be removed
        :param cur: current position of node
        """

        if pos == cur:
            self.prev.next = self.next
            self.next.prev = self.prev
            return self.val

        return self.prev.remove_backward(pos, cur-1)

    def __str__(self):
        """
        Return string representation of linked list
        """
        return str(self.val)+((", "+str(self.next))  if self.next else "")

    def __repr__(self):
        """
        Return representation of linked list
        """
        return repr(self.val)+((", "+repr(self.next))  if self.next else "")



#doubly linked list implemented using references
class LinkedList_References:
    def __init__(self, build_list: List[Any]=None):
        """
        Constructor
        :param build_list:
        """
        self.head = None
        self.tail = None
        self.size = 0

        if build_list:
            self.build_from_list(build_list)

    def build_from_list(self, build_list: List[Any]):
        """
        Build linked list efficiently from a list
        :param build_list: The list to be built from
        """
        try:
            self.head = _Node(val=build_list[0])
            self.size = len(build_list)
        except IndexError:
            print("WARNING: Tried to build LinkedList_References from empty list!")
            return

        self.tail = self.head.build_from_list(build_list, 1)

    def push_back(self, val: Any):
        """
        Push an element into the back of the linked list
        :param val: value to be pushed
        """
        self.size += 1
        self.tail = _Node(val=val, prev=self.tail)
        if self.size > 1:
            self.tail.prev.next = self.tail
        else:
            self.head = self.tail

    def push_front(self, val: Any):
        """
        Push an element into the front of the linked list
        :param val: value to be pushed
        """
        self.size += 1
        self.head = _Node(val=val, next=self.head)
        if self.size > 1:
            self.head.next.prev = self.head
        else:
            self.tail = self.head

    def insert(self, val: Any, pos: int):
        """
        Insert into a certain position
        :param val: value to be inserted
        :param pos: position to insert into
        """
        if pos > self.size or pos < 0:
            raise IndexError("Passed position is out of bounds for LinkedList insertion")
            return

        if pos == 0:
            self.push_front(val)
            return

        if pos == self.size:
            self.push_back(val)
            return

        if pos > self.size//2:
            self.tail.insert_backward(val, pos, self.size-1)
            self.size += 1
            return

        self.head.insert_forward(val, pos, 0)
        self.size += 1

    def pop_front(self):
        """
        Remove the first element in the linked list and return it's value
        """
        if self.size <= 0:
            raise IndexError("Cannot pop an empty linked list")
            return

        self.size -= 1
        aux = self.head
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        if self.size == 0:
            self.tail = None

        return aux.val

    def pop_back(self):
        """
        Remove the tail element in the linked list and return it's value
        """
        if self.size <= 0:
            raise IndexError("Cannot pop an empty linked list")
            return

        self.size -= 1
        aux = self.tail
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        if self.size == 0:
            self.head = None

        return aux.val

    def remove(self, pos):
        """
        Remove the element in position from linked list and returns its value
        :param pos: position of element to remove
        """
        if self.size <= 0:
            raise IndexError("Cannot pop an empty linked list")
            return
        if pos >= self.size or pos < 0:
            raise IndexError("Passed position is out of bounds of LinkedList")
            return

        if pos == 0:
            return self.pop_front()

        if pos == self.size-1:
            return self.pop_back()

        if pos > self.size//2:
            self.size -= 1
            return self.tail.remove_backward(pos, self.size)

        self.size -= 1
        return self.head.remove_forward(pos, 0)


    def get(self, pos: int):
        """
        Get an element at a certain position
        :param pos: position to get
        """
        if pos >= self.size or pos < 0:
            raise IndexError("Passed position is out of bounds of LinkedList")
            return

        if pos > self.size//2:
            return self.tail.get_backward(pos, self.size-1)

        return self.head.get_forward(pos, 0)

    def __len__(self):
        """
        Return size of linked list
        """
        return self.size

    def __str__(self):
        """
        Return string representation of linked list
        """
        return (str(self.head) if self.head else "")

    def __repr__(self):
        """
        Returns representation of linked list
        """
        return "LinkedList_References<"+(repr(self.head) if self.head else "")+">"
