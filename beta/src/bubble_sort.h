#ifndef BUBBLE_SORT_H
#define BUBBLE_SORT_H


#include <iostream>
#include <cstdlib>
#include "sorting.h"
#include "matrix.h"


class bubble_sort : public sorting {

 public: 
  bubble_sort(Matrix* data);
  ~bubble_sort();

  int sort_data();
  void SetRefColNum(int num);

  int extractRefCol();
  int generateIndexArray();


  // unnecessary functions sorting.h
  void SetSortStartIndex(int left){};
  void SetSortEndIndex(int right){};

 private:
  Matrix* data_;
  Matrix* datacopy_;
  int ncols_, nrows_;
  int refColNum_;

  int* indices_;
  double* refColumn_;

};

#endif //BUBBLE_SORT_H
