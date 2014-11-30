#ifndef CONVOLUTE_H_
#define CONVOLUTE_H_

#include "integrator.h"

class Convolute {

 public:
  Convolute(const int nPoints);
  ~Convolute();

  /// Calculates values of a CONVOLUTE
  //virtual int pdfVal(const double Zmean, const double Zvar, double *pdfRet) = 0;
  int convVal(const double *pdfValues, const double *omega, 
	      double *convRet, Integrator *intgr);

 private:
  const int nPoints_;
};

#endif // CONVOLUTE_H_
