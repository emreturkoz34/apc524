#include "simpson.h"
#include "math.h"
#include "assert.h"
#include <stdio.h>

Simpson::Simpson(const double *Z, const int nPoints)
  : Z_(Z),
    nPoints_(nPoints)
{}

Simpson::~Simpson() {
}

double Simpson::integrate(const double *integrand) {

  double temp = 0;
  double f, dx;

  assert((nPoints_-1)%2 == 0);
  // Calculates integral
  for (int n = 0; n < (nPoints_-1)/2; n++) {
    f = integrand[2*n] + 4 * integrand[2*n-1] + integrand[2*n-2];
    temp = temp + f;
  }
  temp = temp / 3;// * (Z_[nPoints_-1] - Z_[0]) / (nPoints_ - 1) / 3;
  // Returns integral result
  return temp;
}
