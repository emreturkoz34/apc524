#ifndef DELTAPDF_H_
#define DELTAPDF_H_

#include "pdf.h"
#include "matrix3d.h"

class DeltaPDF : public PDF {
 public:
  DeltaPDF(double *Z, int ZPoints);
  ~DeltaPDF();
  int pdfVal(double *Zvar, int ZvarPoints, double *Zmean, int ZmeanPoints, Matrix3D *pdfValM);

 private:
  double *Z_;
  int ZPoints_;
};

#endif // DELTAPDF_H_
