%module test
%{
#include "test.h"
%}

%include "std_vector.i"

namespace std {
  %template(Line) vector < double >;
 }

%include "test.h"
