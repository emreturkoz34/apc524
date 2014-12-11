#include "trapz.h"
#include "math.h"
#include <stdio.h>

#include "vector.h"

Trapz::Trapz(Vector *Z, const int nPoints)
  : Z_(Z),
    nPoints_(nPoints)
{}

Trapz::~Trapz() {
}

double Trapz::integrate(Vector *integrand) {

  double temp = 0;
  double f, dx;

  // Calculates integral
  for (int n = 0; n < nPoints_-1; n++) {
    f = 0.5 * (integrand->GetVal(n+1) + integrand->GetVal(n));
    //    dx = Z_[n+1] - Z_[n];
    temp = temp + f;// * dx;
  }
  // Returns integral result
  return temp;

  return 0;
}
