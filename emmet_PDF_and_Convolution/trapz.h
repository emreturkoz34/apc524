#ifndef TRAPZ_H_
#define TRAPZ_H_

#include "integrator.h"

class Trapz : public Integrator {
 public:
  Trapz(const double *Z, const int nPoints);
  ~Trapz();
  int integrate(const double *integrand, double *convRet);

 private:
  const int nPoints_;
  const double *Z_;
};

#endif // TRAPZ_H_
