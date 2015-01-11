#ifndef TRAPZ_H_
#define TRAPZ_H_

#include "integrator.h"

/// Calculates integral using the trapezoidal method.
/*!  Trapz takes in an array (the integrand) and returns the integral
     of that array using the trapezoidal method.
 */
class Trapz : public Integrator {
 public:
  Trapz();
  ~Trapz();
  double integrate(const double *integrand, const double *Z, const int ZPoints);
};

#endif // TRAPZ_H_
