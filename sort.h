
#include <iostream>
#include "matrix.h"


class sorting{

 public:
  sorting(Matrix* data);
  ~sorting();
  
  void sortData(int colNum);
  
 private:
  Matrix* data_;
  Matrix* datacopy_;
  int ncols_, nrows_;


};
