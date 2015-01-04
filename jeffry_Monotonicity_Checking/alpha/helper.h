#ifndef HELPER_H__
#define HELPER_H__

#include <stdio.h>
#include <vector>
#include "vector.h"
#include "matrix.h"

void print_py(std::vector< double > pyvec);
void copy_py_to_vector(std::vector< double > pyvec, Vector *v);
void copy_py_to_matrix(std::vector< double > pyvec, Matrix *m);
void copy_matrix_to_py(Matrix *m, std::vector< double > pyvec);

#endif /* HELPER_H__ */
