%module leastnonmono
%{
#define SWIG_FILE_WITH_INIT
#include "leastnonmono.h"
#include "simplelnm.h"
%}

%include "numpy.i"
%init %{
  import_array();
%}

%apply (int *IN_ARRAY1, int DIM1) {(int *monoAry, const int ncols)}

%include "leastnonmono.h"
%include "simplelnm.h"
