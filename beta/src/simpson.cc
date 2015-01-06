#include "simpson.h"
#include "assert.h"

Simpson::Simpson()
{}

Simpson::~Simpson() {
}

double Simpson::integrate(const double *integrand, const double *Z, const int ZPoints) {

  // Assert that inputs arrays are of the correct length
  //  assert((ZPoints-1)%2 == 0);

  // Calculates integral
  double temp = 0;
  double f, dx;
  for (int n = 1; n < (ZPoints+1)/2; n++) {
    f = integrand[2*n] + 4 * integrand[2*n-1] + integrand[2*n-2];
    dx = Z[n+1] - Z[n];
    temp = temp + f * dx;
  }
  temp = temp / 3;

  return temp;
}
