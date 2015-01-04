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
  double dz, lnpdf, pdf1, pdf2, f;
  double sum;

  // For refining Z to reduce errors
  int ModNum = 10001;
  double *LowMod = new double[ModNum];
  double *UppMod = new double[ModNum];


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
      if (ZmeanVal == 1) {
	temp[ZPoints-1] = 1;
      } else if (ZmeanVal == 0) {
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

	// fill LowMod and UppMod
	for (int k = 0; k < ModNum; k++) {
	  LowMod[k] = double(k) / double(ModNum) / ZPoints;
	  UppMod[ModNum-1-k] = Z[ZPoints-1] - LowMod[k];
	}

	alpha = ZmeanVal * (ZmeanVal * (1 - ZmeanVal) / ZvarVal - 1);
	beta = alpha / ZmeanVal - alpha;
	factor = lgamma(alpha + beta) - lgamma(alpha) - lgamma(beta);

	/// Middle points: 0 < n < ZPoints-1
	for (int n = 1; n < ZPoints-1; n++) {
	  lnpdf = factor + (alpha - 1) * log(Z[n]) + (beta - 1) * log(1 - Z[n]);
	  temp[n] = exp(lnpdf);
	}
	
	/// Calculate integral at ends
	sum = 0;
	dz = LowMod[1] - LowMod[0];
	for (int k = 1; k < ModNum-1; k++) {
	  pdf1 = exp(factor + (alpha - 1) * log(LowMod[k]) + (beta - 1) * log(1 - LowMod[k]));
	  pdf2 = exp(factor + (alpha - 1) * log(LowMod[k+1]) + (beta - 1) * log(1 - LowMod[k+1]));
	  f = 0.5 * (pdf1 + pdf2);
	  sum = sum + f * dz;
	  if (k == 1) {
	    temp[0] = pdf1;
	  }

	  pdf1 = exp(factor + (alpha - 1) * log(UppMod[ModNum-k-2]) + (beta - 1) * log(1 - UppMod[ModNum-k-2]));
	  pdf2 = exp(factor + (alpha - 1) * log(UppMod[ModNum-k-1]) + (beta - 1) * log(1 - UppMod[ModNum-k-1]));
	  f = 0.5 * (pdf1 + pdf2);
	  sum = sum + f * dz;
	  if (k == ModNum-2) {
	    temp[ZPoints-1] = pdf1;
	  }
	}

	for (int n = 1; n < ZPoints-1; n++) {
	  f = 0.5 * (temp[n+1] + temp[n]);
	  dz = Z[n+1] - Z[n];
	  sum = sum + f * dz;
	}

	for (int k = 0; k < ZPoints; k++) {
	  temp[k] = temp[k] / sum;
	}
      }

      /// Set PDF to output
      for (int k = 0; k < ZPoints; k++) {
	pdfValM->SetVal(n, m, k, temp[k]);
      }
    }
  }

  delete temp;
  delete LowMod;
  delete UppMod;
  return 0;
}
