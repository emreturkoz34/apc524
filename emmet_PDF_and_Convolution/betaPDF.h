#ifndef BETAPDF_H_
#define BETAPDF_H_

#include "pdf.h"

class BetaPDF : public PDF {
 public:
  BetaPDF(const double *Z, const int nPoints);
  ~BetaPDF();
  int pdfVal(const double Zmean, const double Zvar, double *pdfRet);

 private:
  const int nPoints_;
  const double *Z_;
};

#endif // BETAPDF_H_
