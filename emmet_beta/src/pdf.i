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
%apply (double *IN_ARRAY1, int DIM1) {
  (double *Zmean, int ZmeanPoints),(double *Zvar, int ZvarPoints)}

%include "pdf.h"
%include "deltaPDF.h"
%include "betaPDF.h"