#ifndef DELTAPDF_H_
#define DELTAPDF_H_

#include "pdf.h"
#include "matrix3d.h"

/// Evaluates delta PDF and stores values in a Matrix3D object.
class DeltaPDF : public PDF {
 public:
  DeltaPDF(const double *Zmean, const int ZmeanPoints);
  ~DeltaPDF();
  int pdfVal(const double *Z, const int ZPoints, Matrix3D *pdfValM);

 private:
  const double *Zmean_;
  const int ZmeanPoints_;
};

#endif // DELTAPDF_H_
