#ifndef INTERPOLATOR_H_
#define INTERPOLATOR_H_

#include "matrix.h"

class Interpolator {
 public: 
  virtual ~Interpolator() {}
  /// Virtual function to be inherited by each interpolation algorithm to interpolate the given data.
  virtual int Interp(const Matrix *matin, int col, double ival, double *vecout, int cols) = 0;
};

#endif // INTERPOLATOR_H_
