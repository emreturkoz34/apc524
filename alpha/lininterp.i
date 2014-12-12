
%module lininterp

%{
#define SWIG_FILE_WITH_INIT
#include "interpolator.h"
#include "lininterp.h"
%}

%include "numpy.i"

%init %{
  import_array();
%}

%apply (double* INPLACE_ARRAY1, int DIM1) {(double* vecout, int cols)};

%include "interpolator.h"
%include "lininterp.h"
