#include "pdf.h"
#include "betaPDF.h"
#include "math.h"
#include "assert.h"

BetaPDF::BetaPDF(double *Z, int ZPoints)
  : Z_(Z),
    ZPoints_(ZPoints)
{}

BetaPDF::~BetaPDF()
{}

int BetaPDF::pdfVal(double *Zvar, int ZvarPoints, double *Zmean, int ZmeanPoints, Matrix3D *pdfValM) {

  // Check dimensions of output matrix match dimensions of input arrays
  assert(ZvarPoints  == pdfValM->GetNumDim1());
  assert(ZmeanPoints == pdfValM->GetNumDim2());
  assert(ZPoints_    == pdfValM->GetNumDim3());

  double *temp = new double[ZPoints_];
  double ZvarVal, ZmeanVal;
  double alpha, beta, factor;
  double dz, lnpdf;
  double sum;

  /*
  double *Z = new double[ZPoints_];
  for (int k = 0; k < ZPts; k++) {
    Z[k] = Z_->GetVal(k);
  }
  */

  int i;
  for (int n = 0; n < ZvarPoints; n++) {
    ZvarVal  = Zvar[n];

    for (int m = 0; m < ZmeanPoints; m++) {
      ZmeanVal = Zmean[m];

      // resets points to 0
      for (int k = 0; k < ZPoints_; k++) {
	temp[k] = 0;
      }  

      /// delta PDF for Zvar == 0 case
      /// max Zmean
      if (ZmeanVal == 1) {
	temp[ZPoints_-1] = 1;
      } else if (ZmeanVal == 0) {
	/// min Zmean
	temp[0] = 1;
      } else if (ZvarVal == 0) {
	i = 0;
	while (Z_[i] < ZmeanVal) {
	  i = i+1;
	}
	temp[i-1] = (Z_[i]  - ZmeanVal)  / (Z_[i] - Z_[i-1]);
	temp[i]   = (ZmeanVal - Z_[i-1]) / (Z_[i] - Z_[i-1]);
      } else if (ZvarVal >= ZmeanVal*(1-ZmeanVal)) {
	temp[0] = 1-ZmeanVal;
	temp[ZPoints_-1] = ZmeanVal;
      } else {

	alpha = ZmeanVal * (ZmeanVal * (1 - ZmeanVal) / ZvarVal - 1);
	beta = alpha / ZmeanVal - alpha;
	factor = lgamma(alpha + beta) - lgamma(alpha) - lgamma(beta);
	
	/// Left bound: n == 0
	dz = 0.5 * (Z_[1] - Z_[0]);

	lnpdf = alpha * log(dz) + factor;
	temp[0] = exp(lnpdf) / alpha;
	
	/// Right bound: n == ZPts-1
	dz = 0.5 * (Z_[ZPoints_-1] - Z_[ZPoints_-2]);
	lnpdf = beta * log(dz) + factor;
	temp[ZPoints_-1] = exp(lnpdf) / beta;
	  
	/// Middle points: 0 < n < ZPoints_-1
	for (int n = 1; n < ZPoints_-1; n++) {
	  dz = 0.5 * (Z_[n+1] - Z_[n-1]);
	  lnpdf = (alpha - 1) * log(Z_[n]) + (beta - 1) * log(1 - Z_[n]);
	  temp[n] = exp(lnpdf) * dz;
	  //	  temp[n] = dz * (pow(Z[n], alpha-1) * pow(1-Z[n], beta-1));
	}
      }

      /// Normalize
      sum = 0;
      for (int k = 0; k < ZPoints_; k++) {
	sum = sum + temp[k];
      }

      /// Set PDF to output
      for (int k = 0; k < ZPoints_; k++) {
	temp[k] = temp[k] / sum;
	pdfValM->SetVal(n, m, k, temp[k]);
      }
    }
  }

  //  delete temp;
  return 0;
}
