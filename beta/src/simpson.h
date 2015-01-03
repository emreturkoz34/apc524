#ifndef SIMPSON_H_
#define SIMPSON_H_

#include "integrator.h"

class Simpson : public Integrator {
 public:
  Simpson();
  ~Simpson();
  double integrate(const double *integrand, const double *Z, const int ZPoints);
};

#endif // SIMPSON_H_
