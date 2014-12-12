#include "integrator.h"
#include "convolute.h"
#include "math.h"
#include "assert.h"
#include <stdio.h>
#include "matrix.h"
#include "matrix3d.h"
#include "vector.h"

Convolute::Convolute(const int nPoints)
  : nPoints_(nPoints)
{}

Convolute::~Convolute() {
}

int Convolute::convVal(const Matrix3D *pdfValues, Vector *data, Matrix *postConvVal, Integrator *intgr) {



  int ZvarPts  = pdfValues->GetNumDim1();
  int ZmeanPts = pdfValues->GetNumDim2();
  int ZPts     = pdfValues->GetNumDim3();
  //  assert(ZPts == ZmeanPts && "Wrong dimensions of ZmeanPts");

  // Calculates integrand with pdf and omega
  Vector *integrand = new Vector(ZPts);
  double temp;

  // variance
  for (int n = 0; n < ZvarPts; n++) {
    // mean
    for (int m = 0; m < ZmeanPts; m++) {

      for (int k = 0; k < ZPts; k++) {
	integrand->SetVal(k, pdfValues->GetVal(n, m, k) * data->GetVal(k));
	//	printf("pdfVal = %f, dataVal = %f, integrand = %f\n", pdfValues->GetVal(n,m,k), data->GetVal(k), pdfValues->GetVal(n,m,k) * data->GetVal(k));
      }
      temp = intgr->integrate(integrand);
      postConvVal->SetVal(n, m, temp);
    }
  }
  

  // Frees memory allocated within function
  delete integrand;

  return 0;
}
