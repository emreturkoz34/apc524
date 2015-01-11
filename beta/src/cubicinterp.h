#ifndef CUBICINTERP_H_
#define CUBICINTERP_H_

#include "interpolator.h"

class CubicInterp : public Interpolator {
 public:
  CubicInterp();
  ~CubicInterp();
  int Interp(const Matrix *matin, int col, double ival, double *vecout, int cols);
};

#endif // CUBICINTERP_H_
