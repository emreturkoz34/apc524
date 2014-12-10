#ifndef PDF_H_
#define PDF_H_
#include <stdio.h>
#include "matrix3d.h"
#include "vector.h"

class PDF {

 public:
  virtual ~PDF() {};
  
  /// Calculates values of a PDF
  //  virtual int pdfVal(const Statistics *stats, double *pdfRet) == 0;
  virtual int pdfVal(Vector *Mean, Vector *Var, Matrix3D *pdfValM) = 0;

};

#endif // PDF_H_
