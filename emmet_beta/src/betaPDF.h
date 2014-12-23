#ifndef BETAPDF_H_
#define BETAPDF_H_

#include "pdf.h"
#include "matrix3d.h"

class BetaPDF : public PDF {
 public:
  BetaPDF(double *Z,int ZPoints);
  ~BetaPDF();
  int pdfVal(double *Zvar, int ZvarPoints, double *Zmean, int ZmeanPoints, Matrix3D *pdfValM);

 private:
  double *Z_;
  int ZPoints_;
};

#endif // BETAPDF_H_
