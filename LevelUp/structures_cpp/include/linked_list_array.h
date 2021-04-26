#ifndef LINKED_LIST_ARRAY_H
#define LINKED_LIST_ARRAY_H

#include <stdexcept>
#include "linked_list.h"

//implementation of linked list using arrays
template <typename T>
class LinkedList_Array : public LinkedList<T>{
public:
  T* array;
  int max_size;

  LinkedList_Array(int msize=100000000){
    //normal constructor
    //:param msize: max size of the linked list
    this->size = 0;
    array = new T[msize];
    max_size = msize;
  }

  void push_back(T v){
    //insert element at end of linked list
    //:param v: value to be inserted
    if(this->size == max_size) throw std::invalid_argument("Linked list full cannot push");
    array[this->size] = v;
    this->size++;
    return;
  }
  void push_front(T v){
    //insert element at beginning of linked list
    //:param v: element to be inserted
    if(this->size == max_size) throw std::invalid_argument("Linked list full cannot push");

    for(int i = this->size; i > 0; i--){
      array[i] = array[i-1];
    }
    array[0] = v;
    this->size++;
    return;
  }
  void pop_back(){
    //pop the last element in the linked list
    if(this->size == 0) throw std::invalid_argument("Cannot pop empty linked list");
    this->size--;
    return;
  }
  void pop_front(){
    //pop the first element in the linked list
    if(this->size == 0) throw std::invalid_argument("Cannot pop empty linked list");
    for(int i = 0; i < this->size-1; i++){
      array[i] = array[i+1];
    }
    this->size--;
    return;
  }
  void insert(T v, int pos){
    //insert element at specific position
    //:param v: element to be inserted
    //:param pos: position to be inserted into
    if(pos > this->size || pos < 0) throw std::invalid_argument("Pos argument out of bounds");
    if(this->size == max_size) throw std::invalid_argument("Linked list full, cannot insert");

    this->size++;
    for(int i = this->size; i > pos; i--){
      array[i]= array[i-1];
    }
    array[pos] = v;
    return;
  }
  void remove(int pos){
    //remove an element from linked list
    //:param pos: position to be removed
    if(pos >= this->size || pos < 0) throw std::invalid_argument("Pos argument out of bounds");

    for(int i = pos; i < this->size; i++){
      array[i] = array[i+1];
    }
    this->size--;
    return;
  }
  T get(int pos){
    //get element at certain position
    //:param pos: position of element to be gotten
    if(pos >= this->size || pos < 0) throw std::invalid_argument("Pos argument out of bounds");
    return array[pos];
  }
};
#endif
