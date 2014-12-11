%module test
%{
#include "test.h"
%}

%include "std_vector.i"

namespace std {
  %template(Line) vector < double >;
   %template(Array) vector < vector < double> >;
 }

void print_array(std::vector< std::vector < double > > myarray);
