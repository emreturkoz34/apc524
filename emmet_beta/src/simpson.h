#ifndef SIMPSON_H_
#define SIMPSON_H_

#include "integrator.h"

class Simpson : public Integrator {
 public:
  Simpson();
  ~Simpson();
  double integrate(double *integrand, double *Z, int ZPoints);
};

#endif // SIMPSON_H_
