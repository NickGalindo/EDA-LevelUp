#ifndef USER_H
#define USER_H

#include <string>
using namespace std;
//Exercise object to be used
class Exercise{
public:
  string name;
  int sets;
  int reps;
  int rpm;

  Exercise(string nm, int st, int rps, int rp){
    //Exercise constructor
    //:param nm: name of exercise
    //:param st: sets in exercise
    //:param rps: reps in exercise
    //:param rp: rpm in exercise
    name = nm;
    sets = st;
    reps = rps;
    rpm = rp;
  }

  Exercise(){}
};

//Workout object to be used
class Workout{
public:
  string date;
  Exercise *exer;

  Workout(string dt, Exercise *e){
    // Workout constructor
    //:param dt: the date of workout
    //:param e: the exercises in the workout
    date = dt;
    exer = e;
  }
  Workout(){}
};

//User object to be used
class User{
public:
  int id;
  string username;
  Workout *work;

  User(int i, string u, Workout *w){
    // User constructor
    //:param i: id of the user
    //:param u: username of the user
    //:param w: workouts for the user
    id = i;
    username = u;
    work = w;
  }
  User(){}
};

#endif
