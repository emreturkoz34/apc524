#ifndef SIMPSON_H_
#define SIMPSON_H_

#include "integrator.h"

/// Calculates integral using Simpson's rule.
/*!  Simpson takes in an array (the integrand) and returns the
     integral of that array using Simpson's rule.
 */
class Simpson : public Integrator {
 public:
  Simpson();
  ~Simpson();
  double integrate(const double *integrand, const double *Z, const int ZPoints);
};

#endif // SIMPSON_H_
