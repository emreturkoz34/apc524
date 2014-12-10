%module helper
%{
#include "helper.h"
#include "vector.h"
#include "matrix.h"
%}

%include "std_vector.i"
%include "vector.h"


namespace std {
  %template(Line) vector < double >;
}

void print_py(std::vector< double > pyvec);
void copy_py_to_vector(std::vector< double > pyvec, Vector *v);
void copy_py_to_matrix(std::vector< double > pyvec, Matrix *m);
void copy_matrix_to_py(Matrix *m, std::vector< double > pyvec);
