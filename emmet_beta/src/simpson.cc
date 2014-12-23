#include "integrator.h"
#include "simpson.h"
#include "math.h"
#include "assert.h"
#include "stdio.h"

Simpson::Simpson()
{}

Simpson::~Simpson() {
}

double Simpson::integrate(double *integrand, double *Z, int ZPoints) {

  double temp = 0;
  double f, dx;

  assert((ZPoints-1)%2 == 0);
  // Calculates integral
  for (int n = 1; n < (ZPoints+1)/2; n++) {
    f = integrand[2*n] + 4 * integrand[2*n-1] + integrand[2*n-2];
    dx = Z[n+1] - Z[n];
    temp = temp + f * dx;
  }
  temp = temp / 3;// * (Z[ZPoints-1] - Z[0]) / (ZPoints - 1) / 3;

  // Returns integral result
  return temp;
}
