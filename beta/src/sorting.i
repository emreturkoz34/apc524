%module sorting
%{
#define SWIF_FILE_WITH_INIT
#include "sorting.h"
#include "bubble_sort.h"
#include "quick_sort.h"
%}

/*
%include "numpy.i"
%init %{
  import_array();
%}
*/

%apply (double *IN_ARRAY1, int DIM1) {(const double *Z, const int ZPoints)}
%apply (double *IN_ARRAY1, int DIM1) {
  (const double *Zmean, const int ZmeanPoints),(const double *Zvar, const int ZvarPoints)}

%include "sorting.h"
%include "bubble_sort.h"
%include "quick_sort.h"
