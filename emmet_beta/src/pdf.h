#ifndef PDF_H_
#define PDF_H_

#include "matrix3d.h"

class PDF {
 public:
  virtual ~PDF() {};
  virtual int pdfVal(double *Z, int ZPoints, 
		     Matrix3D *pdfValM) = 0;
};

#endif // PDF_H_
