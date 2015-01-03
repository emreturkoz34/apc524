#ifndef PDF_H_
#define PDF_H_

#include "matrix3d.h"

class PDF {
 public:
  virtual ~PDF() {};
  virtual int pdfVal(const double *Z, const int ZPoints, 
		     Matrix3D *pdfValM) = 0;
};

#endif // PDF_H_
