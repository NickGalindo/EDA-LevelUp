from typing import Any
import linked_list_hash



class HashTable:

    def __init__(self, n  :int):
        
        self.A =  [linked_list_hash.LinkedList_References()]*n
        

    def hashFunc(self, val : any):
        return 2

    def hasKey(self, key : any):
        l = self.A[self.hashFunc(key)]
        curr = l.head
        while curr:
            if curr.key == key:
                return True
            
            else:
                curr = curr.next
        return False
 

    def get(self, key : any):
        l = self.A[self.hashFunc(key)]
        curr = l.head
        while curr:
            if curr.key == key:
                return curr.val
            
            else:
                curr = curr.next
        
        return None


    def set(self,key,new_val):

        l = self.A[self.hashFunc(key)]
        curr = l.head
        while curr:
            if curr.key == key:
                curr.value = new_val
                return
            curr = curr.next
        l.push_back(key,new_val)


 
 
h = HashTable(3)
h.set("holaaa",500)
h.set("buenas",150)
h.set("tardes",200)

print(h.A[2])


