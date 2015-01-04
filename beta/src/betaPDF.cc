#include "betaPDF.h"
#include "math.h"
#include "assert.h"

BetaPDF::BetaPDF(const double *Zmean, const int ZmeanPoints, const double *Zvar, const int ZvarPoints)
  : Zmean_(Zmean),
    ZmeanPoints_(ZmeanPoints),
    Zvar_(Zvar),
    ZvarPoints_(ZvarPoints) {
}

BetaPDF::~BetaPDF() {
}

int BetaPDF::pdfVal(const double *Z, const int ZPoints, Matrix3D *pdfValM) {

  // Check dimensions of output matrix match dimensions of input arrays
  assert(pdfValM->GetNumDim1() == ZvarPoints_);
  assert(pdfValM->GetNumDim2() == ZmeanPoints_);
  assert(pdfValM->GetNumDim3() == ZPoints);

  double *temp = new double[ZPoints];
  double ZvarVal, ZmeanVal;
  double alpha, beta, factor;
  double dz, lnpdf, f;
  double sum;

  // For refining Z to reduce errors
  int ModNum = 10000;
  int ZModLen = (ZPoints-1) * ModNum + 1;
  double *RMod = new double[ZModLen];
  double *ZMod = new double[ZModLen];

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

	// fill ZMod
	for (int k = 0; k < ZModLen; k++) {
	  ZMod[k] = double(k) / double((ZModLen - 1));
	}

	alpha = ZmeanVal * (ZmeanVal * (1 - ZmeanVal) / ZvarVal - 1);
	beta = alpha / ZmeanVal - alpha;
	factor = lgamma(alpha + beta) - lgamma(alpha) - lgamma(beta);

	/// Middle points: 0 < n < ZPoints-1
	for (int n = 0; n < ZModLen; n++) {
	  lnpdf = factor + (alpha - 1) * log(ZMod[n]) + (beta - 1) * log(1 - ZMod[n]);
	  RMod[n] = exp(lnpdf);
	}
	RMod[0] = RMod[1];
	RMod[ZModLen-1] = RMod[ZModLen-2];

	sum = 0;
	for (int n = 0; n < ZModLen-1; n++) {
	  f = 0.5 * (RMod[n+1] + RMod[n]);
	  dz = ZMod[n+1] - ZMod[n];
	  sum = sum + f * dz;
	}

	for (int k = 1; k < ZPoints-1; k++) {
	  temp[k] = RMod[k*ModNum] / sum;
	}
      }

      /// Set PDF to output
      for (int k = 0; k < ZPoints; k++) {
	pdfValM->SetVal(n, m, k, temp[k]);
      }
    }
  }

  delete temp;
  delete ZMod;
  delete RMod;
  return 0;
}
