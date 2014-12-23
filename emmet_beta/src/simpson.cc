#include "simpson.h"
#include "assert.h"

Simpson::Simpson()
{}

Simpson::~Simpson() {
}

double Simpson::integrate(double *integrand, double *Z, int ZPoints) {

  assert((ZPoints-1)%2 == 0);

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
