#ifndef BUBBLE_SORT_H
#define BUBBLE_SORT_H


#include <iostream>
#include <cstdlib>
#include "sorting.h"
#include "matrix.h"


class BubbleSort : public Sorting {

 public: 
  BubbleSort(Matrix* data);
  ~BubbleSort();

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

#endif //BUBBLE_SORT_H
