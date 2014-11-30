#ifndef SIMPSON_H_
#define SIMPSON_H_

#include "integrator.h"

class Simpson : public Integrator {
 public:
  Simpson(const double *Z, const int nPoints);
  ~Simpson();
  int integrate(const double *integrand, double *convRet);

 private:
  const int nPoints_;
  const double *Z_;
};

#endif // SIMPSON_H_
