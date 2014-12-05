#ifndef SORTING_H_
#define SORTING_H_

#include <stdio.h>

class sorting{

 public:
  virtual ~sorting(){};
  
  virtual int sort_data() = 0; 
  virtual void SetRefColNum(int num){};

};


#endif // SORTING_H_
