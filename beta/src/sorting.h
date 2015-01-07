#ifndef SORTING_H_
#define SORTING_H_

#include <stdio.h>

class sorting{

 public:
  virtual ~sorting(){};
  
  /// Virtual function to be inherited by each sorting algorithm to sort the give data
  virtual int sort_data() = 0; 
  
  /// Setting the reference column according to which the data will be sorted
  virtual void SetRefColNum(int num){};

};


#endif // SORTING_H_
