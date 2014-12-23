#ifndef BETAPDF_H_
#define BETAPDF_H_

#include "pdf.h"
#include "matrix3d.h"

class BetaPDF : public PDF {
 public:
  BetaPDF(double *Zmean, int ZmeanPoints, double *Zvar, int ZvarPoints);
  ~BetaPDF();
  int pdfVal(double *Z, int ZPoints, Matrix3D *pdfValM);

 private:
  double *Zmean_;
  int ZmeanPoints_;
  double *Zvar_;
  int ZvarPoints_;
};

#endif // BETAPDF_H_
