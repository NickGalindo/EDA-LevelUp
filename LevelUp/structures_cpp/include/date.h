#ifndef DATE_H
#define DATE_H

#include <string>
using namespace std;
//date class to use
class Date{
public:
  int year, month, day;
  Date(int yy, int mm, int dd){
    //normal date constructor
    year = yy;
    month = mm;
    day = dd;
  }

  string toString(){
    //return string representation of date
    return (to_string(year)+"-"+to_string(month)+"-"+to_string(day));
  }
};


#endif
