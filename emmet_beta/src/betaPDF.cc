#include "betaPDF.h"
#include "math.h"
#include "assert.h"

BetaPDF::BetaPDF(double *Zmean, int ZmeanPoints, double *Zvar, int ZvarPoints)
  : Zmean_(Zmean),
    ZmeanPoints_(ZmeanPoints),
    Zvar_(Zvar),
    ZvarPoints_(ZvarPoints) {
}

BetaPDF::~BetaPDF() {
}

int BetaPDF::pdfVal(double *Z, int ZPoints, Matrix3D *pdfValM) {

  // Check dimensions of output matrix match dimensions of input arrays
  assert(pdfValM->GetNumDim1() == ZvarPoints_);
  assert(pdfValM->GetNumDim2() == ZmeanPoints_);
  assert(pdfValM->GetNumDim3() == ZPoints);

  double *temp = new double[ZPoints];
  double ZvarVal, ZmeanVal;
  double alpha, beta, factor;
  double dz, lnpdf;
  double sum;

  int i;
  for (int n = 0; n < ZvarPoints_; n++) {
    ZvarVal  = Zvar_[n];

    for (int m = 0; m < ZmeanPoints_; m++) {
      ZmeanVal = Zmean_[m];

      // resets points to 0
      for (int k = 0; k < ZPoints; k++) {
	temp[k] = 0;
      }  

      /// check for Min or Max mean
      if (ZmeanVal == 1) { // use "if (m == ZmeanPoints_-1) {" instead???
	temp[ZPoints-1] = 1;
      } else if (ZmeanVal == 0) { // use "if (m == 0) {" instead???
	temp[0] = 1;

	/// Delta PDF for zero variance
      } else if (ZvarVal == 0) {
	i = 0;
	while (Z[i] < ZmeanVal) {
	  i = i+1;
	}
	temp[i-1] = (Z[i]  - ZmeanVal)  / (Z[i] - Z[i-1]);
	temp[i]   = (ZmeanVal - Z[i-1]) / (Z[i] - Z[i-1]);

	/// Impossible cases: becomes double delta PDF
      } else if (ZvarVal >= ZmeanVal*(1-ZmeanVal)) {
	temp[0] = 1-ZmeanVal;
	temp[ZPoints-1] = ZmeanVal;

	/// BetaPDF
      } else {
	alpha = ZmeanVal * (ZmeanVal * (1 - ZmeanVal) / ZvarVal - 1);
	beta = alpha / ZmeanVal - alpha;
	factor = lgamma(alpha + beta) - lgamma(alpha) - lgamma(beta);
	
	/// Left bound: n == 0
	dz = 0.5 * (Z[1] - Z[0]);
	lnpdf = alpha * log(dz) + factor;
	temp[0] = exp(lnpdf) / alpha;
	
	/// Right bound: n == ZPts-1
	dz = 0.5 * (Z[ZPoints-1] - Z[ZPoints-2]);
	lnpdf = beta * log(dz) + factor;
	temp[ZPoints-1] = exp(lnpdf) / beta;
	  
	/// Middle points: 0 < n < ZPoints-1
	for (int n = 1; n < ZPoints-1; n++) {
	  dz = 0.5 * (Z[n+1] - Z[n-1]);
	  lnpdf = (alpha - 1) * log(Z[n]) + (beta - 1) * log(1 - Z[n]);
	  temp[n] = exp(lnpdf) * dz;
	}
      }

      /// Normalize
      sum = 0;
      for (int k = 0; k < ZPoints; k++) {
	sum = sum + temp[k];
      }

      /// Set PDF to output
      for (int k = 0; k < ZPoints; k++) {
	temp[k] = temp[k] / sum;
	pdfValM->SetVal(n, m, k, temp[k]);
      }
    }
  }

  //  delete temp;
  return 0;
}
