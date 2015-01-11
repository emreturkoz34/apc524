#ifndef FITTOGRID_H_
#define FITTOGRID_H_

#include "matrix.h"
#include "matrix3d.h"
#include "matrix4d.h"
#include "interpolator.h"
#include "standard_sort.h"
#include <omp.h>

int fittogrid(const Matrix4D *datain, const double *cgrid, Interpolator *interp, Matrix3D *dataout, int nthreads);

#endif // FITTOGRID_H_
