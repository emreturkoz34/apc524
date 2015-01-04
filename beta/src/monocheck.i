%module monocheck
%{
#define SWIG_FILE_WITH_INIT
#include "monocheck.h"
#include "matrix.h"
%}

%include "numpy.i"
%init %{
  import_array();
%}

%apply (int *IN_ARRAY1, int DIM1) {(int *monoAry, const int ncols)}

%include "monocheck.h"
%include "matrix.h"
