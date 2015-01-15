#ifndef BRUTE_SORT_H
#define BRUTE_SORT_H


#include <iostream>
#include "sorting.h"
#include "matrix.h"


class BruteSort : public Sorting {
 public:
  BruteSort(Matrix* data);
  ~BruteSort();
  
  int sort_data();
  void SetRefColNum(int num);


 private:
  Matrix* data_;
  Matrix* datacopy_;
  int ncols_, nrows_;
  int refColNum_;

  int* indices_;
  double* refColumn_;
  

};


#endif //BRUTE_SORT_H
