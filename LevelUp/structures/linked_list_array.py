from typing import List, Any


class LinkedList_Array:

    def __init__(self, n: int):

        self.capacity = n
        self.size =0
        self.array = [None] * self.capacity

    
    def push_back(self, val : Any):
        """
        Push an element into the back of the array
        :param val: value to be pushed
        """
        try:
            self.array[self.size] = val
            self.size+=1

        except IndexError:
            print("WARNING: Full array")
            return
    
    def push_front(self, val : Any):
        """
        Push an element into the front of the array
        :param val: value to be pushed
        """

        if (self.size == self.capacity):
            print("WARNING: Full array")
            return

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
            raise Exception('full array')

        if pos >= self.size or pos < 0:
            raise IndexError("Passed position is out of bounds for LinkedList insertion")
            return
        
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
            return 

        for i in range(1,self.size,1):
            self.array[i-1] = self.array[i]
        
        self.size -=1
        self.array[self.size] = None
        return aux

    def pop_back(self):
        """
        Remove the last element in the array and return it's value
        """
        if self.array[0] == None:
            raise IndexError("Cannot pop an empty array")
            return 
        
        self.size -=1
        aux = self.array[self.size]
        self.array[self.size] = None
        
        return aux

    def remove(self,pos : int):
        """
        Remove the element in position from array and returns its value
        :param pos: position of element to remove
        """

        if self.array[0] == None:
            raise IndexError("Cannot pop an empty array")
            return 
        
        if (pos>=self.size):
            raise IndexError("Passed position is out of bounds of array")
            return  

        if pos == 0:
            self.pop_front()
        
        if pos == self.size-1:
            self.pop_back()
        
        else:
            aux = self.array[pos]

            for i in range(pos+1,self.size,1):
                self.array[i-1] = self.array[i]

            self.size -= 1
            self.array[self.size] = None
            return aux
    
    def get(self, pos : int):
        """
        Get an element at a certain position
        :param pos: position to get
        """
        if pos >= self.size or pos < 0:
            raise IndexError("Passed position is out of bounds of the Array")
            return
        
        return self.array[pos]

    def __str__(self):
        """
        Return string representation of the array
        """
        return (str(self.array))
















        


        



        

