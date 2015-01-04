#ifndef VECTOR_H_
#define VECTOR_H_

#include <stdio.h>

class Vector {
 public:
  Vector(int cols);
  ~Vector();
  double GetVal(int i) const;
  void SetVal(int i, double val);
  int GetNumCols() const;

 private:
  double *vector_;
  const int ncols_;
};

#endif // VECTOR_H_
