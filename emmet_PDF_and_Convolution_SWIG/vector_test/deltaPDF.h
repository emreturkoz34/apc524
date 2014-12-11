#ifndef DELTAPDF_H_
#define DELTAPDF_H_

#include "pdf.h"
#include "matrix3d.h"
#include "vector.h"

class DeltaPDF : public PDF {
 public:
  DeltaPDF(Vector *Z, const int nPoints);
  ~DeltaPDF();
  int pdfVal(Vector *Mean, Vector *Var, Matrix3D *pdfValM);

 private:
  const int nPoints_;
  Vector *Z_;
};

#endif // DELTAPDF_H_
