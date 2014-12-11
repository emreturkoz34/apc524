#include "deltaPDF.h"
#include "math.h"
#include <stdio.h>
#include <assert.h>
#include "matrix3d.h"
#include <vector>

DeltaPDF::DeltaPDF(std::vector< double > Zvec, const int nPoints)
  : Zvec_(Zvec),
    nPoints_(nPoints) {
  for (int i = 0; i < nPoints; i++) {
    Z_[i] = Zvec[i];
  }
}

DeltaPDF::~DeltaPDF() {
}

int DeltaPDF::pdfVal(const double *Mean, const double *Var, Matrix3D *pdfValM) {

  int ZvarPts  = pdfValM->GetNumDim1();
  int ZmeanPts = pdfValM->GetNumDim2();
  int ZPts     = pdfValM->GetNumDim3();
  assert(ZvarPts == 1);

  double Zmean, Zvar;
  double *temp = new double[ZmeanPts];
  int i;

  for (int m = 0; m < ZmeanPts; m++) {
    Zmean = Mean[m];
    i = 0;

    while (Z_[i] < Zmean) {
      i = i+1;
    }
    if (i == 0) {
      temp[0] = 1;
    } else {
      temp[i-1] = (Z_[i]  - Zmean)  / (Z_[i] - Z_[i-1]);
      temp[i]   = (Zmean - Z_[i-1]) / (Z_[i] - Z_[i-1]);
    }

    for (int k = 0; k < ZPts; k++) {
      pdfValM->SetVal(0, m, k, temp[k]);
    }
  }

  delete[] temp;
  return 0;
}
