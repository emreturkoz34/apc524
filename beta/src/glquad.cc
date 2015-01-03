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

GLQuad::~GLQuad() {
  delete x_;
  delete w_;
}

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
