#ifndef LINKED_LIST_H
#define LINKED_LIST_H

//Abstract linked_list implementation
template <typename T>
class LinkedList{
public:
  int size;
  virtual void push_back(T v) = 0;
  virtual void push_front(T v) = 0;
  virtual void pop_back() = 0;
  virtual void pop_front() = 0;
  virtual void insert(T v, int pos) = 0;
  virtual void remove(int pos) = 0;
  virtual T get(int pos) = 0;
};

#endif
