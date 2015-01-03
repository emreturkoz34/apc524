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

%apply (double *IN_ARRAY1, int DIM1) {(const double *Z, const int ZPoints)}
%apply (double *IN_ARRAY1, int DIM1) {
  (const double *Zmean, const int ZmeanPoints),(const double *Zvar, const int ZvarPoints)}

%include "pdf.h"
%include "deltaPDF.h"
%include "betaPDF.h"
