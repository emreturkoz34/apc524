#ifndef DELTAPDF_H_
#define DELTAPDF_H_

#include "pdf.h"
#include "matrix3d.h"

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
