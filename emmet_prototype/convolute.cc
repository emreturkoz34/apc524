#include "integrator.h"
#include "convolute.h"
#include "math.h"
#include "assert.h"
#include <stdio.h>
#include "matrix.h"
#include "matrix3d.h"


Convolute::Convolute(const int nPoints)
  : nPoints_(nPoints)
{}

Convolute::~Convolute() {
}

int Convolute::convVal(const Matrix3D *pdfValues, const double *rxnRate, const double *progVar, Matrix **postConvVal, Integrator *intgr) {

  // Calculates integrand with pdf and omega
  double *integrand = new double[nPoints_];
  double temp;

  int ZvarPts  = pdfValues->GetNumDim1();
  int ZmeanPts = pdfValues->GetNumDim2();
  int ZPts     = nPoints_;
  assert(ZPts == ZmeanPts && "Wrong dimensions of ZmeanPts");

  Matrix *vars = new Matrix(2, ZPts);
  for (int n = 0; n < ZPts; n++) {
    vars->SetVal(0, n, rxnRate[n]);
    vars->SetVal(1, n, progVar[n]);
  }


  // variance
  for (int n = 0; n < ZvarPts; n++) {
    // mean
    for (int m = 0; m < ZmeanPts; m++) {
      // data col (variables)
      for (int j = 0; j < 2; j++) {
	// data row (variable values)
	for (int k = 0; k < ZPts; k++) {
	  integrand[k] = pdfValues->GetVal(n, m, k) * vars->GetVal(j, k);
	}
	temp = intgr->integrate(integrand);
	postConvVal[j]->SetVal(n, m, temp);
      }
    }
  }
  

  // Frees memory allocated within function
  delete integrand;

  return 0;
}
