#ifndef BRUTE_SORT_H
#define BRUTE_SORT_H


#include <iostream>
#include "sorting.h"
#include "matrix.h"

class brute_sort : public sorting {
 public:
  brute_sort(Matrix* data);
  ~brute_sort();
  
  int sort_data();
  
  void SetRefColNum(int num);


 private:
  Matrix* data_;
  Matrix* datacopy_;
  int ncols_, nrows_;
  int refColNum_;
  

};


#endif //BRUTE_SORT_H
