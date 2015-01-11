#include "glquad.h"
#include "assert.h"
#include "stdio.h"

#include "alglibinternal.h"
#include "alglibmisc.h"
#include "ap.h"
#include "dataanalysis.h"
#include "diffequations.h"
#include "fasttransforms.h"
#include "integration.h"
#include "interpolation.h"
#include "linalg.h"
#include "optimization.h"
#include "solvers.h"
#include "specialfunctions.h"
#include "statistics.h"

/// Constructor
/*!
  
  Coordinates of abcissas are calculated in this function.

  INPUTS:

  const int Nodes             number of abcissa


  OUTPUT:

  No particular output objects. Abcissas and weights are stored in x_ and w_ objects, respectively. 

*/
GLQuad::GLQuad(const int Nodes)
  : Nodes_(Nodes),
    x_(new double[Nodes]),
    w_(new double[Nodes]) {

  alglib::ae_int_t n = Nodes_;
  alglib::ae_int_t info;
  alglib::real_1d_array x;
  alglib::real_1d_array w;
  alglib::gqgenerategausslegendre(n, info, x, w);

  // NOTE: only possible values for info are 1, -1, -3, -4
  if (info == -1) {
    printf("Gauss Legendre Quadrature Failed: "
	   "Incorrect number of nodes");
  } else if (info == -3) {
    printf("Gauss Legendre Quadrature Failed: "
	   "Internal eigenproblem solver hasn't converged");
  } else if (info == -4) {
    printf("Gauss Legendre Quadrature Failed: "
	   "number of nodes is too large, try multiple precision version");
  }
  assert(info == 1);

  for (int i = 0; i < Nodes_; i++) {
    x_[i] = x[i]; // abscissa
    w_[i] = w[i]; // weights
  }
}

/// Destructor
GLQuad::~GLQuad() {
  delete x_;
  delete w_;
}


/// Integration using Gauss-Legendre quadrature. 
/*!

  Gauss-Legendre quadrature is applied to integrate a given integrand over a given double array, Z.
  Abcissas and weights are created during the execution of the constructor. 
  The default number of nodes is 20, the number of nodes for the quadrature can be modified from the input file
  
  \verbatim
  INPUTS:

  const double *integrand            array that contains function values to be integrated

  const double *Z                    array that contains the mixture fraction values which the integrand will be integrated over

  const int ZPoints                  number of values, size of the integrand and Z containers
  
  OUTPUT:

  double                             result of the integration

  \endverbatim

 */ 
double GLQuad::integrate(const double *integrand, const double *Z, const int ZPoints) {

  double xModRange;
  double *intgrNodeVals = new double[Nodes_];
  
  int i;
  for (int n = 0; n < Nodes_; n++) {
    // Converts range of x from -1,1 to Zmin,Zmax
    xModRange = (x_[n] + 1) * (Z[ZPoints-1] - Z[0]) / 2;

    i = 0;
    while (Z[i] < xModRange) {
      i = i+1;
    }

    // linear interpolation to find integrand at abscissa
    intgrNodeVals[n] = integrand[i]*(Z[i]-xModRange)/(Z[i]-Z[i-1])
      + integrand[i-1]*(xModRange-Z[i-1])/(Z[i]-Z[i-1]);
  }

  // Calculates integral
  double temp, f;
  temp = 0;
  for (int n = 0; n < Nodes_; n++) {
    f = intgrNodeVals[n] * w_[n];
    temp = temp + f;
  }

  // Scales integral to account for domain conversion: x = -1,1 to Zmin,Zmax
  temp = temp * (Z[ZPoints-1] - Z[0]) / 2;

  delete intgrNodeVals;
  return temp;
}
