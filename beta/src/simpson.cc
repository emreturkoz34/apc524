#include "simpson.h"
#include "assert.h"

/// Constructor
Simpson::Simpson()
{}

/// Destructor
Simpson::~Simpson() {
}

/// Main function that integrates a given data set using Simpson's Rule
/*!
  Simpson's rule is applied to integrate a given integrand over a given double array, Z.

  \verbatim
  INPUTS: 

  const double *integrand           array that contains function values to be integrated

  const double *Z                   array that contains the mixture fraction values which the integrand will be integrated over

  const int ZPoints                 number of values, size of the integrand and Z arrays


  OUTPUT:

  double                            result of the integration

  \endverbatim

 */
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
