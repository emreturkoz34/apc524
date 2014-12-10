#include "deltaPDF.h"
#include "math.h"
#include <stdio.h>
#include <assert.h>
#include "matrix3d.h"
#include "vector.h"

DeltaPDF::DeltaPDF(Vector *Z, const int nPoints)
  : Z_(Z),
    nPoints_(nPoints)
{}

DeltaPDF::~DeltaPDF() {
}

int DeltaPDF::pdfVal(Vector *Var, Vector *Mean, Matrix3D *pdfValM) {

  int ZvarPts  = pdfValM->GetNumDim1();
  int ZmeanPts = pdfValM->GetNumDim2();
  int ZPts     = pdfValM->GetNumDim3();
  assert(ZvarPts == 1);

  /*
  printf("\n");
  printf("Zmean vector:\n");
  for (int k = 0; k < ZmeanPts; k++) {
    printf("Zmean[%d] = %f\n", k, Mean->GetVal(k));
  }
  */

  double Zmean, Zvar;
  double *temp = new double[ZmeanPts];
  double *Z = new double[ZmeanPts];
  for (int k = 0; k < ZmeanPts; k++) {
    Z[k] = Z_->GetVal(k);
  }

  int i;
  for (int m = 0; m < ZmeanPts; m++) {
    Zmean = Mean->GetVal(m);

    for (int k = 0; k < ZmeanPts; k++) {
      temp[k] = 0;
      /*
      printf("temp[%d] = %f\n", k, temp[k]);
      */
    }

    i = 0;
    /*
    printf("Z[%d] = %f\n", 0, Z[0]);
    printf("Zmean[%d] = %f\n", m, Zmean);
    */
    while (Z[i] < Zmean) {
      i = i+1;
    }

    
    if (i == 0) {
      temp[0] = 1;
    } else {
      temp[i-1] = (Z[i]  - Zmean)  / (Z[i] - Z[i-1]);
      temp[i]   = (Zmean - Z[i-1]) / (Z[i] - Z[i-1]);
    }

    for (int k = 0; k < ZPts; k++) {
      pdfValM->SetVal(0, m, k, temp[k]);
    }

  }

  delete[] temp;
  delete[] Z;

  return 0;
}
