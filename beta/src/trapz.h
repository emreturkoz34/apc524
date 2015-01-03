#ifndef TRAPZ_H_
#define TRAPZ_H_

#include "integrator.h"

class Trapz : public Integrator {
 public:
  Trapz();
  ~Trapz();
  double integrate(const double *integrand, const double *Z, const int ZPoints);
};

#endif // TRAPZ_H_
