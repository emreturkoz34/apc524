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

    // resets points to 0
    for (int k = 0; k < ZmeanPts; k++) {
      temp[k] = 0;
    }

    // finds location of Zmean in Z
    i = 0;
    while (Z[i] < Zmean) {
      i = i+1;
    }

    // calculates PDF
    if (i == 0) {
      temp[0] = 1;
    } else {
      temp[i-1] = (Z[i]  - Zmean)  / (Z[i] - Z[i-1]);
      temp[i]   = (Zmean - Z[i-1]) / (Z[i] - Z[i-1]);
    }

    // outputs PDF values into PDFValM
    for (int k = 0; k < ZPts; k++) {
      pdfValM->SetVal(0, m, k, temp[k]);
    }

  }

  delete[] temp;
  delete[] Z;

  return 0;
}
