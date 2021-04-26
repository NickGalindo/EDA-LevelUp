from typing import Any

class Queue_Array:
  #Queue implementada con arreglos

  def __init__(self, size: Any):
    '''
    Constructor
    :param size: max size of queue
    :param front: index of first element of the queue in the array
    :param rear: index where the next element of the queue will be insert
    :param count: amount of elements the queue
    '''
    self.size = size
    self.front = 0
    self.rear = 0
    self.count = 0
    self.arr = [None]*size

  def __str__(self):
    '''
    String representation of the queue
    '''
    out = ""
    aux = self.front
    # travel in queue with aux index, the variable out concatenate the string representation of the queue

    for i in range(0, self.count):
      out += str(self.arr[aux]) 

      #Print ", " at the end of the element if is not the last
      if i !=(self.count - 1 ):
        out += ", "
      aux = (aux + 1) % self.size

    return out

  def __len__(self):
    """
    Returns the amount of elements in the queue
    """
    return self.count

  def isEmpty(self):
    """
    Verifies if the queue is empty
    """
    return self.count <= 0


  def isFull(self):
    '''
    Return true if the queue is full
    '''
    return self.count >= self.size

  def getFront(self):
    """
      Get the first element in the queue
    """
    if self.size == 0:
      raise IndexError("Queueu is empty, cannot get front element")

    return self.arr[self.front]

  def enqueue(self, val:Any):
    '''
    Insert element at the end of the queue
    :param val: value to be insert in the queue
    '''
    if self.isFull():
      raise IndexError("Cannot enqueue in a full queue")
    else:
      self.count = self.count + 1
      self.arr[self.rear] = val
      self.rear = (self.rear+1) % self.size

  def dequeue (self):
    '''
    Remove the first element in the queue array
    '''
    if self.isEmpty():
      raise IndexError("Cannot enqueue in a full queue")
    else:
      item = self.arr[self.front]
      self.front = (self.front + 1) % self.size
      self.count -= 1
    return item
