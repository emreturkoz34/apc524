#ifndef DELTAPDF_H_
#define DELTAPDF_H_

#include "pdf.h"

class DeltaPDF : public PDF {
 public:
  DeltaPDF(const double *Z, const int nPoints);
  ~DeltaPDF();
  int pdfVal(const double Zmean, const double Zvar, double *pdfRet);

 private:
  const int nPoints_;
  const double *Z_;
};

#endif // DELTAPDF_H_
