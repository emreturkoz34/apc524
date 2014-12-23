#include "integrator.h"
#include "trapz.h"
#include "math.h"
#include "assert.h"

Trapz::Trapz()
{}

Trapz::~Trapz() {
}

double Trapz::integrate(double *integrand, double *Z, int ZPoints) {

  double temp = 0;
  double f, dx;

  // Calculates integral
  for (int n = 0; n < ZPoints-1; n++) {
    f = 0.5 * (integrand[n+1] + integrand[n]);
    dx = Z[n+1] - Z[n];
    temp = temp + f * dx;
  }

  // Returns integral result
  return temp;
}
