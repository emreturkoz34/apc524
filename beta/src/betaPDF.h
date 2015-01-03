#ifndef BETAPDF_H_
#define BETAPDF_H_

#include "pdf.h"
#include "matrix3d.h"

class BetaPDF : public PDF {
 public:
  BetaPDF(const double *Zmean, const int ZmeanPoints, const double *Zvar, const int ZvarPoints);
  ~BetaPDF();
  int pdfVal(const double *Z, const int ZPoints, Matrix3D *pdfValM);

 private:
  const double *Zmean_;
  const int ZmeanPoints_;
  const double *Zvar_;
  const int ZvarPoints_;
};

#endif // BETAPDF_H_
