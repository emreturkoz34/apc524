#ifndef DELTAPDF_H_
#define DELTAPDF_H_

#include "pdf.h"
#include "matrix3d.h"

class DeltaPDF : public PDF {
 public:
  DeltaPDF(double *Zmean, int ZmeanPoints);
  ~DeltaPDF();
  int pdfVal(double *Z, int ZPoints, Matrix3D *pdfValM);

 private:
  double *Zmean_;
  int ZmeanPoints_;
};

#endif // DELTAPDF_H_
