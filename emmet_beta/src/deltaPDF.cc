#include "pdf.h"
#include "deltaPDF.h"
#include "math.h"
#include "assert.h"

DeltaPDF::DeltaPDF(double *Z, int ZPoints)
  : Z_(Z),
    ZPoints_(ZPoints)
{}

DeltaPDF::~DeltaPDF() {
}

int DeltaPDF::pdfVal(double *Zvar, int ZvarPoints, double *Zmean, int ZmeanPoints, Matrix3D *pdfValM) {

  // Check dimensions of output matrix match dimensions of input arrays
  assert(ZvarPoints  == 1);
  assert(ZvarPoints  == pdfValM->GetNumDim1());
  assert(ZmeanPoints == pdfValM->GetNumDim2());
  assert(ZPoints_    == pdfValM->GetNumDim3());

  double ZmeanVal;
  double *temp = new double[ZPoints_];

  /*
  double *Z = new double[ZmeanPts];
  for (int k = 0; k < ZmeanPts; k++) {
    Z[k] = Z_[k];
  }
  */

  int i;
  for (int m = 0; m < ZmeanPoints; m++) {
    ZmeanVal = Zmean[m];

    // resets points to 0
    for (int k = 0; k < ZPoints_; k++) {
      temp[k] = 0;
    }

    if (ZmeanVal == 1) {
      temp[ZPoints_-1] = 1;
    } else if (ZmeanVal == 0) {
      temp[0] = 1;
    } else {
      // finds location of ZmeanVal in Z
      i = 0;
      while (Z_[i] < ZmeanVal) {
	i = i+1;
      }

      // calculates PDF
      if (i == 0) {
	temp[0] = 1;
      } else {
	temp[i-1] = (Z_[i]  - ZmeanVal)  / (Z_[i] - Z_[i-1]);
	temp[i]   = (ZmeanVal - Z_[i-1]) / (Z_[i] - Z_[i-1]);
      }
    }

    // outputs PDF values into PDFValM
    for (int k = 0; k < ZPoints_; k++) {
      pdfValM->SetVal(0, m, k, temp[k]);
    }
  }

  //  delete[] temp;
  //  delete[] Z;

  return 0;
}
