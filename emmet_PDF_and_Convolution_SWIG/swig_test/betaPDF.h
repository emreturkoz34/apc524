#ifndef BETAPDF_H_
#define BETAPDF_H_

#include "pdf.h"
#include "matrix3d.h"

class BetaPDF : public PDF {
 public:
  BetaPDF(const double *Z, const int nPoints);
  ~BetaPDF();
  int pdfVal(const double *Mean, const double *Var, Matrix3D *pdfValM);

 private:
  const int nPoints_;
  const double *Z_;
};

#endif // BETAPDF_H_
