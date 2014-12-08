#ifndef QUICK_SORT_H
#define QUICK_SORT_H


#include <iostream>
#include "sorting.h"
#include "matrix.h"

class quick_sort : public sorting {
 public:
  quick_sort(Matrix* data);
  ~quick_sort();
  
  int sort_data();
  
  void SetRefColNum(int num);

  int extractRefCol();
  int generateIndexArray();

  void SetSortStartIndex(int left);
  void SetSortEndIndex(int right);
  
 private:
  Matrix* data_;
  Matrix* datacopy_;
  int ncols_, nrows_;
  int refColNum_;
  int left_, right_;

  double* refColumn_;
  int* indices_;

};


#endif // QUICK_SORT_H
