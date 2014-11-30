#include "betaPDF.h"
#include "math.h"
#include <stdio.h>

BetaPDF::BetaPDF(const double *Z, const int nPoints)
  : Z_(Z),
    nPoints_(nPoints)
{}

BetaPDF::~BetaPDF()
{}

int BetaPDF::pdfVal(const double Zmean, const double Zvar, double *pdfRet) {
  

  //  int nPoints = len(Z);
  double alpha = Zmean * (Zmean * (1 - Zmean) / Zvar - 1);
  double beta = alpha / Zmean - alpha;
  double factor = lgamma(alpha + beta) - lgamma(alpha) - lgamma(beta);

  for (int n = 0; n < nPoints_; n++) {
    pdfRet[n] = 0;
  }

  /// delta PDF for Zvar == 0 case
  int i = 0;
  if (Zvar == 0) {
    while (Z_[i] < Zmean) {
      i = ++i;
    }
    pdfRet[i-1] = (Z_[i]  - Zmean)  / (Z_[i] - Z_[i-1]);
    pdfRet[i]   = (Zmean - Z_[i-1]) / (Z_[i] - Z_[i-1]);
    return 0;
  }

  /// max Zmean
  if (Zmean == 1) {
    pdfRet[nPoints_-1] = 1;
    return 0;
  }

  /// min Zmean
  if (Zmean == 0) {
    pdfRet[0] = 1;
    return 0;
  }

  double dz, temp;
  /// Left bound: n == 0
  dz = 0.5 * (Z_[1] - Z_[0]);
  printf("dz = %f\n", dz);
  temp = alpha * log(dz) + factor;
  pdfRet[0] = exp(temp) / alpha;

  /// Right bound: n == nPoints_-1
  dz = 0.5 * (Z_[nPoints_-1] - Z_[nPoints_-2]);
  temp = beta * log(dz) + factor;
  pdfRet[nPoints_-1] = exp(temp) / beta;

  /// Middle points: 0 < n < nPoints-1
  for (int n = 1; n < nPoints_-1; n++) {
    dz = 0.5 * (Z_[n+1] - Z_[n-1]);
    temp = (alpha - 1) * log(Z_[n]) + (beta - 1) * log(1 - Z_[n]);
    pdfRet[n] = exp(temp) * dz;
  }

  /// Normalize

  double sum = 0;
  for (int n = 1; n < nPoints_-2; n++) {
    sum = sum + pdfRet[n];
  }
  for (int n = 1; n < nPoints_-2; n++) {
    pdfRet[n] = pdfRet[n] / sum;
  }

  return 0;
}
