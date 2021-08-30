from typing import List,Any
import  linked_list



class NodeHash(linked_list._Node):
    def __init__(self, key : Any=None, val: Any=None, next: Any=None, prev: Any=None):
        self.val = val
        self.next = next
        self.prev = prev
        self.key = key
    
    def __str__(self):
        """
        Return string representation of linked list
        """
        return str(self.key)+((", "+str(self.next))  if self.next else "")



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
            self.head = NodeHash(val=build_list[0])
            self.size = len(build_list)
        except IndexError:
            print("WARNING: Tried to build LinkedList_References from empty list!")
            return

        self.tail = self.head.build_from_list(build_list, 1)

    def push_back(self,key : Any, val: Any):
        """
        Push an element into the back of the linked list
        :param val: value to be pushed
        """
        self.size += 1
        self.tail =NodeHash(key = key ,val=val, prev=self.tail)
        if self.size > 1:
            self.tail.prev.next = self.tail
        else:
            self.head = self.tail

    def push_front(self, key,val: Any):
        """
        Push an element into the front of the linked list
        :param val: value to be pushed
        """
        self.size += 1
        self.head = NodeHash(key = key, val=val, next=self.head)
        if self.size > 1:
            self.head.next.prev = self.head
        else:
            self.tail = self.head

    def insert(self, key,val: Any, pos: int):
        """
        Insert into a certain position
        :param val: value to be inserted
        :param pos: position to insert into
        """
        if pos > self.size or pos < 0:
            raise IndexError("Passed position is out of bounds for LinkedList insertion")
            return

        if pos == 0:
            self.push_front(key,val)
            return

        if pos == self.size:
            self.push_back(key,val)
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

    def remove(self, pos: int):
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

