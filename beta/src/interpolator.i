
%module interpolator

%{
#ifndef SWIG_FILE_WITH_INIT
#define SWIG_FILE_WITH_INIT
#include "interpolator.h"
#include "lininterp.h"
#include "cubicinterp.h"
#include "hermiteinterp.h"
#endif
%}

%include "numpy.i"

%init %{
  import_array();
%}

%apply (double* INPLACE_ARRAY1, int DIM1) {(double* vecout, int cols)};


%include "interpolator.h"
%include "lininterp.h"
%include "cubicinterp.h"
%include "hermiteinterp.h"