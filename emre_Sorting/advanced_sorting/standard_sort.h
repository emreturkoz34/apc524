#ifndef STANDARD_SORT_H
#define STANDARD_SORT_H

#include <iostream>
#include <algorithm>
#include <vector>
#include "sorting.h"
#include "matrix.h"

class standard_sort : public sorting {
 public:
  standard_sort(Matrix* data);
  ~standard_sort();

  int sort_data();
  void SetRefColNum(int num);

  // unnecessary functions at sorting.h
  int extractRefCol(){return 0;}
  int generateIndexArray(){return 0;}
 
  void SetSortStartIndex(int left){};
  void SetSortEndIndex(int right){};




 private:
  Matrix *data_;
  Matrix *datacopy_;
  int ncols_, nrows_;
  int refColNum_;


};







#endif //STANDARD_SORT_H
