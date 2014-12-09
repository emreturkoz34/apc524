#include "trapz.h"
#include "math.h"
#include <stdio.h>

Trapz::Trapz(const double *Z, const int nPoints)
  : Z_(Z),
    nPoints_(nPoints)
{}

Trapz::~Trapz() {
}

double Trapz::integrate(const double *integrand) {

  double temp = 0;
  double f, dx;

  // Calculates integral
  for (int n = 0; n < nPoints_-1; n++) {
    f = 0.5 * (integrand[n+1] + integrand[n]);
    //    dx = Z_[n+1] - Z_[n];
    temp = temp + f;// * dx;
  }
  // Returns integral result
  return temp;
}
