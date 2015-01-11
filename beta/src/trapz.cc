#include "trapz.h"

/// Constructor
Trapz::Trapz() {
}

/// Destructor
Trapz::~Trapz() {
}


double Trapz::integrate(const double *integrand, const double *Z, const int ZPoints) {

  double temp = 0;
  double f, dx;

  for (int n = 0; n < ZPoints-1; n++) {
    f = 0.5 * (integrand[n+1] + integrand[n]);
    dx = Z[n+1] - Z[n];
    temp = temp + f * dx;
  }

  return temp;
}
