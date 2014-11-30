#include "deltaPDF.h"
#include "math.h"
#include <stdio.h>

DeltaPDF::DeltaPDF(const double *Z, const int nPoints)
  : Z_(Z),
    nPoints_(nPoints)
{}

DeltaPDF::~DeltaPDF() {
}

int DeltaPDF::pdfVal(const double Zmean, const double Zvar, double *pdfRet) {

  for (int n = 0; n < nPoints_; n++) {
    pdfRet[n] = 0;
  }

  /// delta PDF
  int i = 0;
  while (Z_[i] < Zmean) {
    i = ++i;
  }
  if (i == 0) {
    pdfRet[0] = 1;
  } else {
    pdfRet[i-1] = (Z_[i]  - Zmean)  / (Z_[i] - Z_[i-1]);
    pdfRet[i]   = (Zmean - Z_[i-1]) / (Z_[i] - Z_[i-1]);
  }
  return 0;
}
