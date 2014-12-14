#include "betaPDF.h"
#include "math.h"
#include <stdio.h>
#include "matrix3d.h"
#include "vector.h"
#include "assert.h"

BetaPDF::BetaPDF(Vector *Z, const int nPoints)
  : Z_(Z),
    nPoints_(nPoints)
{}

BetaPDF::~BetaPDF()
{}

int BetaPDF::pdfVal(Vector *Var, Vector *Mean, Matrix3D *pdfValM) {

  int ZvarPts  = pdfValM->GetNumDim1();
  int ZmeanPts = pdfValM->GetNumDim2();
  int ZPts     = pdfValM->GetNumDim3();

  double *temp = new double[ZPts];
  double Zvar, Zmean;
  double alpha, beta, factor;
  double dz, lnpdf;
  double sum;

  double *Z = new double[ZPts];
  for (int k = 0; k < ZPts; k++) {
    Z[k] = Z_->GetVal(k);
  }

  int i;
  for (int n = 0; n < ZvarPts; n++) {
    Zvar  = Var->GetVal(n);

    for (int m = 0; m < ZmeanPts; m++) {
      Zmean = Mean->GetVal(m);

      // resets points to 0
      for (int k = 0; k < ZPts; k++) {
	temp[k] = 0;
      }  

      /// delta PDF for Zvar == 0 case
      /// max Zmean
      if (Zmean == 1) {
	temp[ZPts-1] = 1;
      } else if (Zmean == 0) {
	/// min Zmean
	temp[0] = 1;
      } else if (Zvar == 0) {
	i = 0;
	while (Z[i] < Zmean) {
	  i = i+1;
	}
	temp[i-1] = (Z[i]  - Zmean)  / (Z[i] - Z[i-1]);
	temp[i]   = (Zmean - Z[i-1]) / (Z[i] - Z[i-1]);
      } else if (Zvar >= Zmean*(1-Zmean)) {
	temp[0] = 1-Zmean;
	temp[ZmeanPts-1] = Zmean;
      } else {

	alpha = Zmean * (Zmean * (1 - Zmean) / Zvar - 1);
	beta = alpha / Zmean - alpha;
	factor = lgamma(alpha + beta) - lgamma(alpha) - lgamma(beta);
	
	/// Left bound: n == 0
	dz = 0.5 * (Z[1] - Z[0]);

	lnpdf = alpha * log(dz) + factor;
	temp[0] = exp(lnpdf) / alpha;
	
	/// Right bound: n == ZPts-1
	dz = 0.5 * (Z[ZPts-1] - Z[ZPts-2]);
	lnpdf = beta * log(dz) + factor;
	temp[ZPts-1] = exp(lnpdf) / beta;
	  
	/// Middle points: 0 < n < nPoints-1
	for (int n = 1; n < ZPts-1; n++) {
	  dz = 0.5 * (Z[n+1] - Z[n-1]);
	  //    temp = (alpha - 1) * log(Z[n]) + (beta - 1) * log(1 - Z[n]);
	  //    temp[n] = exp(temp) * dz;
	  temp[n] = dz * (pow(Z[n], alpha-1) * pow(1-Z[n], beta-1));
	}
      }

      /// Normalize
      sum = 0;
      for (int k = 0; k < ZPts; k++) {
	sum = sum + temp[k];
      }
      for (int k = 0; k < ZPts; k++) {
	temp[k] = temp[k] / sum;
	pdfValM->SetVal(n, m, k, temp[k]);
      }

    }
  }

  delete temp;
  return 0;
}
