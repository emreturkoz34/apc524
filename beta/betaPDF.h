#ifndef BETAPDF_H_
#define BETAPDF_H_

#include "pdf.h"
#include "matrix3d.h"
#include "vector.h"

class BetaPDF : public PDF {
 public:
  BetaPDF(Vector *Z, const int nPoints);
  ~BetaPDF();
  int pdfVal(Vector *Var, Vector *Mean, Matrix3D *pdfValM);

 private:
  const int nPoints_;
  Vector *Z_;
};

#endif // BETAPDF_H_
