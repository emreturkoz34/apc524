#include "trapz.h"

/// Constructor
Trapz::Trapz() {
}

/// Destructor
Trapz::~Trapz() {
}


/// Main function that integrates a given data set using Trapezoidal Rule
/*!
  Trapezoidal rule is applied to integrate a given integrand over a given double array, Z. 

  \verbatim
  INPUTS:

  const double *integrand          array that contains function values to be integrated

  const double *Z                  array that contains the mixture fraction values which the integrand will be integrated over

  const int ZPoints                number of values, size of the integrand and Z containers

  
  OUTPUT:

  double                           result of the integration
 
  \endverbatim

*/
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
