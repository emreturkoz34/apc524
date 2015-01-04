%module maxslope
%{
#define SWIG_FILE_WITH_INIT
#include "maxslope.h"
#include "endpointslope.h"
#include "linregression.h"
%}

%include "numpy.i"
%init %{
  import_array();
%}

%apply (int *IN_ARRAY1, int DIM1) {(int *monoAry, const int ncols)}

#include "maxslope.h"
#include "endpointslope.h"
#include "linregression.h"
