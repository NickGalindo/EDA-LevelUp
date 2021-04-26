from typing import List, Any


class LinkedList_Array:

    def __init__(self, n: int):
        """
        Constructor
        :param n: max capacity of linked list
 
        """

        self.capacity = n
        self.size =0
        self.array = [None] * self.capacity

    
    def push_back(self, val : Any):
        """
        Push an element into the back of the array
        :param val: value to be pushed
        """
        if (self.size == self.capacity):
            raise IndexError("Capacity of LinkedList_array has been exceeded")

        self.array[self.size] = val
        self.size+=1

    
    def push_front(self, val : Any):
        """
        Push an element into the front of the array
        :param val: value to be pushed
        """

        if (self.size == self.capacity):
           raise IndexError("Capacity of LinkedList_Array has been exceeded")

        for i in range (self.size,0,-1):
            self.array[i] = self.array[i-1]
        
        self.array[0] = val
        self.size += 1

    def insert(self, val : Any, pos : int):

        """
        Insert into a certain position
        :param val: value to be inserted
        :param pos: position to insert into
        """
        
        if self.size == self.capacity:
            raise IndexError("Passed position is out of bounds for Array insertion")


        if pos > self.size or pos < 0:
            raise IndexError("Passed position is out of bounds for Array insertion")
            
        
        if pos == 0:
            self.push_front(val)
            return

        if pos == self.size:
            self.push_back(val)
            return

        for i in range(self.size,pos,-1):
            self.array[i] = self.array[i-1]
        
        self.array[pos] = val
        self.size += 1

    def pop_front(self):
        """
        Remove the first element in the array and return it's value
        """
        aux = self.array[0]
        if self.array[0] == None:
            raise IndexError("Cannot pop an empty array")
             

        for i in range(1,self.size,1):
            self.array[i-1] = self.array[i]
        
        self.size -=1
        return aux

    def pop_back(self):
        """
        Remove the last element in the array and return it's value
        """
        if self.array[0] == None:
            raise IndexError("Cannot pop an empty array")
             
        
        self.size -=1
        aux = self.array[self.size]
        
        
        return aux

    def remove(self,pos : int):
        """
        Remove the element in position from array and returns its value
        :param pos: position of element to remove
        """

        if self.array[0] == None:
            raise IndexError("Cannot pop an empty array")
            
        
        if (pos>=self.size):
            raise IndexError("Passed position is out of bounds of array")
             

        if pos == 0:
            self.pop_front()
        
        elif pos == self.size-1:
            self.pop_back()
        
        else:
            aux = self.array[pos]

            for i in range(pos+1,self.size,1):
                self.array[i-1] = self.array[i]

            self.size -= 1
            
            return aux
    
    def get(self, pos : int):
        """
        Get an element at a certain position
        :param pos: position to get
        """
        if pos >= self.size or pos < 0:
            raise IndexError("Passed position is out of bounds of the Array")

        
        return self.array[pos]

    def __str__(self):
        """
        Return string representation of the array
        """
        return (str(self.array))

    def __repr__(self):
        """
        Returns representation of linked list array
        """
        return "LinkedList_Array"+(repr(self.array))















        


        



        

