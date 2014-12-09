#ifndef DELTAPDF_H_
#define DELTAPDF_H_

#include "pdf.h"
#include "matrix3d.h"

class DeltaPDF : public PDF {
 public:
  DeltaPDF(const double *Z, const int nPoints);
  ~DeltaPDF();
  int pdfVal(const double *Mean, const double *Var, Matrix3D *pdfValM);

 private:
  const int nPoints_;
  const double *Z_;
};

#endif // DELTAPDF_H_
