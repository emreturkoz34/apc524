#ifndef SORTING_H_
#define SORTING_H_

#include <stdio.h>

class sorting{

 public:
  virtual ~sorting(){};
  
  virtual int sort_data() = 0; 
  virtual void SetRefColNum(int num){};
  
  virtual int extractRefCol() = 0;
  virtual int generateIndexArray() = 0;
  virtual void SetSortStartIndex(int left){};
  virtual void SetSortEndIndex(int right){};

 

};


#endif // SORTING_H_
