#ifndef GLQuad_H_
#define GLQuad_H_

#include "integrator.h"

/// Calculates integral using Gauss-Legendre quadrature.
/*!  GLQuad takes in an array (the integrand) and returns the integral
     of that array using Gauss-Legendre quadrature. Abscissa are
     calculated using the external library AlgLib.
 */
class GLQuad : public Integrator {
 public:
  GLQuad(int Nodes);
  ~GLQuad();
  double integrate(const double *integrand, const double *Z, const int ZPoints);

 private:
  const int Nodes_;
  double *x_;
  double *w_;
};

#endif // GLQuad_H_
