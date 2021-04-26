#ifndef LINKED_LIST_REF_H
#define LINKED_LIST_REF_H

#include <stdexcept>
#include "linked_list.h"

//Node function for linked list implementation
template <typename T>
class Node{
public:
  Node<T> *next, *prev;
  T val;

  Node(T v){
    //Node consturctor
    //:param v: value of node
    val = v;
    next = prev = 0;
    return;
  }

  void insert(T v){
    //insert into linked_list
    //:param v: value to be inserted
    prev = prev->next = new Node<T>(v);
    return;
  }

  void remove(){
    //remove from linked_list
    prev->next = next;
    next->prev = prev;
    delete this;
    return;
  }
};


//linked_list_references implementation
template <typename T>
class LinkedList_Ref : public LinkedList<T>{
public:
  Node<T> *head, *tail;

  LinkedList_Ref(){
    //Linked list constructor normal
    this->size = 0;
  }

  void push_back(T v){
    //push back a value into the linked list
    //:param v: value to be pushed
    if(this->size == 0){
      this->size++;
      tail = head = new Node<T>(v);
      return;
    }

    this->size++;
    tail->next = new Node<T>(v);
    tail->next->prev = tail;
    tail = tail->next;
    return;
  }
  void push_front(T v){
    //push front a value into the linked list
    //:param v: value to be pushed
    if(this->size == 0){
      this->size++;
      tail = head = new Node<T>(v);
      return;
    }

    this->size++;
    head->prev = new Node<T>(v);
    head->prev->next = head;
    head = head->prev;
    return;
  }
  void pop_back(){
    //pop the last element in linked list
    if(this->size == 0) throw std::invalid_argument("Cannot pop empty LinkedList!");

    if(tail->prev == 0){
      this->size = 0;
      delete tail;
      tail = head = 0;
      return;
    }

    this->size--;
    tail=tail->prev;
    delete tail->next;
    tail->next = 0;
    return;
  }
  void pop_front(){
    //pop the first element in linked list
    if(this->size == 0) throw std::invalid_argument("Cannot pop empty LinkedList!");

    if(head->next == 0){
      this->size = 0;
      delete head;
      tail = head = 0;
      return;
    }

    this->size--;
    head = head->next;
    delete head->prev;
    head->prev=0;
    return;
  }
  void insert(T v, int pos){
    //insert into the linked list at certain point
    //:param v: value to be inserted
    //:param pos: position to be inserted into
    if(pos < 0 || pos > this->size) throw std::invalid_argument("Cannot insert outside of LinkedList range");

    if(pos == 0){
      this->push_front(v);
      return;
    }
    if(pos == this->size){
      this->push_back(v);
      return;
    }

    Node<T> *tmp = this->head;
    int cur = 0;
    while(tmp){
      if(cur == pos) break;
      tmp = tmp->next;
      cur++;
    }

    tmp->insert(v);
    this->size++;
    return;
  }
  void remove(int pos){
    //remove from linked list
    //:param pos: psoition to be removed
    if(pos < 0 || pos >= this->size) throw std::invalid_argument("Cannot remove outside of linked list range");

    if(pos == 0){
      this->pop_front();
      return;
    }
    if(pos == this->size-1){
      this->pop_back();
      return;
    }

    Node<T> *tmp = this->head;
    int cur = 0;
    while(tmp){
      if(cur == pos) break;
      tmp = tmp->next;
      cur++;
    }

    tmp->remove();
    this->size--;
    return;
  }
  T get(int pos){
    //get an element from linked list
    //:param pos: the position to get
    if(pos < 0 || pos >= this->size) throw std::invalid_argument("Cannot get outside of linked list range");

    Node<T> *tmp = this->head;
    int cur = 0;
    while(tmp){
      if(cur == pos) break;
      tmp = tmp->next;
      cur++;
    }

    return tmp->val;
  }
};

#endif
