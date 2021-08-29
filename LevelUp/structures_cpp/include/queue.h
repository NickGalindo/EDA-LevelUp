#ifndef QUEUE_H
#define QUEUE_H

#include <stdexcept>

//Node function for queue implementation
template <typename T>
class Node{
public:
  Node<T> *next;
  T val;

  Node(T v){
    //Node consturctor
    //:param v: value of node
    val = v;
    return;
  }
};

//Queue implementation
template <typename T>
class Queue{
public:
  Node<T> *head, *tail;
  int size;

  Queue(){
    //Normal queue constructor
    size = 0;
  }

  void push(T v){
    //Push an element into the queue
    //:param v: value to be pushed in
    if(size == 0){
      head = new Node<T>(v);
      tail = head;
      size++;
      return;
    }

    tail->next = new Node<T>(v);
    tail = tail->next;
    size++;
    return;
  }

  void pop(){
    //Pop the front element from queue
    if(size == 0) throw std::invalid_argument("Cannot pop empty Queue!");

    if(head->next == 0){
      delete head;
      tail = 0;
      head = 0;
      size--;
      return;
    }

    Node<T> *nxt = head->next;
    delete head;
    head = nxt;
    size--;
    return;
  }

  T front(){
    //Get the front element from queue
    if(size == 0) throw std::invalid_argument("Cannot get element from empty Queue!");

    return head->val;
  }
};


#endif
