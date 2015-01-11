#ifndef HERMITEINTERP_H_
#define HERMITEINTERP_H_

#include "interpolator.h"
#include "interpolation.h"

class HermiteInterp : public Interpolator {
 public:
  HermiteInterp();
  ~HermiteInterp();
  int Interp(const Matrix *matin, int col, double ival, double *vecout, int cols);
};

#endif // HERMITEINTERP_H_
