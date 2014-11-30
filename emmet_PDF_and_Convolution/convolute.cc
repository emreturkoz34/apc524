#include "integrator.h"
#include "convolute.h"
#include "math.h"
#include "assert.h"
#include <stdio.h>


Convolute::Convolute(const int nPoints)
  : nPoints_(nPoints)
{}

Convolute::~Convolute() {
}

int Convolute::convVal(const double *pdfValues, const double *omega,
		       double *convRet, Integrator *intgr) {


  // Calculates integrand with pdf and omega
  double *integrand = new double[nPoints_];
  for (int n = 0; n < nPoints_; n++) {
    integrand[n] = pdfValues[n] * omega[n];
    printf("integrand[%d] = %f\n", n, integrand[n]);
  }

  // Integrate: removes dependence on Z, returns scalar at Zmean,Zvar
  assert(intgr->integrate(integrand, convRet) == 0);

  // Frees memory allocated within function
  delete integrand;

  return 0;
}
