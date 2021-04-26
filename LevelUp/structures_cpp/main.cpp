#include "include/linked_list.h"
#include "include/linked_list_array.h"
#include "include/linked_list_ref.h"
#include <stdlib.h>
#include <time.h>
#include <string>
#include <utility>
#include <iostream>

using namespace std;

LinkedList_Ref<pair<int, int> >* createVolume_ref(int load_size){
  //generate special user data for processing
  //:param load_size: The load size to be generated
  srand(time(0));

  LinkedList_Ref<pair<int, int>>* a = new LinkedList_Ref<pair<int, int>>();
  for(int i = 0; i < load_size; i++){
    a->push_back(make_pair(i, 10+rand()%200));

    if(i % 10000 == 0) printf("Batch %d\n", i);
  }
  return a;
}

LinkedList_Array<pair<int, int> >* createVolume_arr(int load_size){
  //generate special user data for processing
  //:param load_size: The load size to be generated
  srand(time(0));

  LinkedList_Array<pair<int, int>>* a = new LinkedList_Array<pair<int, int>>();
  for(int i = 0; i < load_size; i++){
    a->push_back(make_pair(i, 10+rand()%200));

    if(i % 10000 == 0) printf("Batch %d\n", i);
  }
  return a;
}

pair<int, int>* get(LinkedList<pair<int, int> >* a, int pos){
  //get an element from the linked list
  //:param a: pointer to LinkedList
  //:param pos: position to return
  pair<int, int> aux = a->get(pos);
  return new pair<int, int>(aux.first, aux.second);
}

void remove(LinkedList<pair<int, int> >* a, int pos){
  //remove an element from linked list
  //:param a: pointer to LinkedList
  //:param pos: position to remove
  a->remove(pos);
  return;
}

void insert(LinkedList<pair<int, int> >* a, pair<int, int>* val, int pos){
  //insert an element into the linked LinkedList
  //:param a: pointer to LinkedList
  //:param val: value to insert
  //:param pos: position to insert
  a->insert(*val, pos);
  return;
}

void pop_front(LinkedList<pair<int, int> >* a){
  //pop the front element
  //:param a: pointer to linked list
  a->pop_front();
  return;
}

void pop_back(LinkedList<pair<int, int> >* a){
  //pop the back element
  //:param a: pointer to linked list
  a->pop_back();
  return;
}

void push_front(LinkedList<pair<int, int> >* a, pair<int, int>* val){
  //push val into the front element
  //:param a: pointer to linked list
  //:param val: val to be pushed
  a->push_front(*val);
  return;
}

void push_back(LinkedList<pair<int, int> >* a, pair<int, int>* val){
  //push val into the back element
  //:param a: pointer to linked list
  //:param val: val to be pushed
  a->push_back(*val);
  return;
}

extern "C" {
  LinkedList_Ref<pair<int, int> >* createVolume_ref_py(int load_size){ return createVolume_ref(load_size); }
  LinkedList_Array<pair<int, int> >* createVolume_arr_py(int load_size){ return createVolume_arr(load_size); }
  pair<int, int>* get_py(LinkedList<pair<int, int> >* a, int pos){ return get(a, pos); }
  void remove_py(LinkedList<pair<int, int> >* a, int pos){ remove(a, pos); }
  void insert_py(LinkedList<pair<int, int> >* a, pair<int, int>* val, int pos){ insert(a, val, pos); }
  void pop_front_py(LinkedList<pair<int, int> >* a){ pop_front(a); }
  void pop_back_py(LinkedList<pair<int, int> >* a){ pop_back(a); }
  void push_front_py(LinkedList<pair<int, int> >* a, pair<int, int>* val){ push_front(a, val); }
  void push_back_py(LinkedList<pair<int, int> >* a, pair<int, int>* val){ push_back(a, val); }
  int decouple_pair_first(pair<int, int>* val){ return val->first; }
  int decouple_pair_second(pair<int, int>* val){ return val->second; }
  pair<int, int>* encouple_pair(int a, int b){ return new pair<int, int>(a, b); }
}

int main(){

  LinkedList<pair<int, int> >* tt = createVolume_arr(10000);
  pair<int, int> *aux = get(tt, 4);
  cout << aux->first << " " << aux->second << endl;
  push_back(tt, new pair<int, int> (44, 88));
  aux = get(tt, tt->size-1);
  cout << aux->first << " " << aux->second << endl;



  return 0;
}
