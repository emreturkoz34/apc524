#ifndef CONVOLUTE_H_
#define CONVOLUTE_H_

#include "matrix.h"
#include "matrix3d.h"
#include "integrator.h"

int convVal(double *Z, double *data, Matrix3D *pdfValM, Matrix *postConvVal, Integrator *intgr);

#endif // CONVOLUTE_H_
