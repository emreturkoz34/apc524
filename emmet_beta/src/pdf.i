%module pdf
%{
#define SWIG_FILE_WITH_INIT
#include "pdf.h"
#include "deltaPDF.h"
#include "betaPDF.h"
%}

%include "numpy.i"
%init %{
  import_array();
%}

%apply (double *IN_ARRAY1, int DIM1) {(double *Z, int ZPoints)}
%apply (double *IN_ARRAY1, int DIM1) {(double *Zvar, int ZvarPoints),(double *Zmean, int ZmeanPoints)}

%include "pdf.h"
%include "deltaPDF.h"
%include "betaPDF.h"
%include "matrix3d.h"
