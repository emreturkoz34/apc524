#include "deltaPDF.h"
#include "assert.h"

DeltaPDF::DeltaPDF(const double *Zmean, const int ZmeanPoints)
  : Zmean_(Zmean),
    ZmeanPoints_(ZmeanPoints) {
}

DeltaPDF::~DeltaPDF() {
}

int DeltaPDF::pdfVal(const double *Z, const int ZPoints, Matrix3D *pdfValM) {

  // Check dimensions of output matrix match dimensions of input arrays
  assert(pdfValM->GetNumDim1() == 1);
  assert(pdfValM->GetNumDim2() == ZmeanPoints_);
  assert(pdfValM->GetNumDim3() == ZPoints);

  double ZmeanVal;
  double *temp = new double[ZPoints];

  int i;
  for (int m = 0; m < ZmeanPoints_; m++) {
    ZmeanVal = Zmean_[m];

    // resets points to 0
    for (int k = 0; k < ZPoints; k++) {
      temp[k] = 0;
    }

    if (ZmeanVal == 1) {
      temp[ZPoints-1] = 1;
    } else if (ZmeanVal == 0) {
      temp[0] = 1;
    } else {
      // finds location of ZmeanVal in Z
      i = 0;
      while (Z[i] < ZmeanVal) {
	i = i+1;
      }

      // calculates PDF
      if (i == 0) {
	temp[0] = 1;
      } else {
	temp[i-1] = (Z[i]  - ZmeanVal)  / (Z[i] - Z[i-1]);
	temp[i]   = (ZmeanVal - Z[i-1]) / (Z[i] - Z[i-1]);
      }
    }

    // outputs PDF values into PDFValM
    for (int k = 0; k < ZPoints; k++) {
      pdfValM->SetVal(0, m, k, temp[k]);
    }
  }

  delete[] temp;
  return 0;
}
