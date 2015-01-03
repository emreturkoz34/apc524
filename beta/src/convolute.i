%module convolute
%{
#define SWIG_FILE_WITH_INIT
#include "integrator.h"
#include "convolute.h"
%}

%include "numpy.i"
%init %{
  import_array();
%}

%apply (double *IN_ARRAY1, int DIM1) {(double *Z, int ZPoints),(double *data, int dataPoints)}

%inline %{
  int convVal_func(double *Z, int ZPoints, double *data, int dataPoints, Matrix3D *pdfValM, Matrix *postConvVal, Integrator *intgr) {
    return convVal(Z, data, pdfValM, postConvVal, intgr);
  }
%}
