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


 private:
  Matrix *data_;
  Matrix *datacopy_;
  int ncols_, nrows_;
  int refColNum_;


};







#endif //STANDARD_SORT_H
