#ifndef DELTAPDF_H_
#define DELTAPDF_H_

#include "pdf.h"
#include "matrix3d.h"
#include <vector>

class DeltaPDF : public PDF {
 public:
  DeltaPDF(std::vector< double > Zvec, const int nPoints);
  ~DeltaPDF();
  int pdfVal(const double *Mean, const double *Var, Matrix3D *pdfValM);

 private:
  const int nPoints_;
  std::vector< double > Zvec_;
  double *Z_;
};



#endif // DELTAPDF_H_
