#include "simpson.h"
#include "assert.h"
#include "stdio.h"

Simpson::Simpson()
{}

Simpson::~Simpson() {
}

double Simpson::integrate(const double *integrand, const double *Z, const int ZPoints) {

  // Assert that inputs arrays are of the correct length
  assert((ZPoints-1)%2 == 0);
  const double h = Z[1] - Z[0];
  for (int n = 1; n < ZPoints-1; n++) {
    if (h - (Z[n+1]-Z[n]) > h/1000) {
      printf("ERROR: Nonuniform mesh used with Simpson's Rule\n");
      assert(h - (Z[n+1]-Z[n]) < h/1000);
    }
  }

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
