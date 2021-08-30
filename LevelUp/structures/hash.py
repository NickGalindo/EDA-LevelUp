from typing import Any
import linked_list_hash



class HashTable:

    def __init__(self, n  :int):
        self.n = n
        self.A =  [None]*self.n
        for i in range (n):
            self.A[i] = linked_list_hash.LinkedList_References()
        

    def PolyHash(self, val : any, x : int=1234, p : int=9973,a : int=9456, b :int=7689):
        hash =0
        for i in range(len(val)-1,0,-1):
            hash = (hash*x + ord(val[i])) % p

        hash = ((a*hash + b)%p)%self.n
        
        return hash 
        


    def hasKey(self, key : any):
        l = self.A[self.PolyHash(key)]
        curr = l.head
        while curr:
            if curr.key == key:
                return True
            
            else:
                curr = curr.next
        return False
 

    def get(self, key : any):
        l = self.A[self.PolyHash(key)]
        curr = l.head
        while curr:
            if curr.key == key:
                return curr.val
            
            else:
                curr = curr.next
        
        return None


    def set(self,key,new_val):

        l = self.A[self.PolyHash(key)]
        curr = l.head
        while curr:
            if curr.key == key:
                curr.val = new_val
                return
            curr = curr.next
        l.push_front(key,new_val)


 
 






