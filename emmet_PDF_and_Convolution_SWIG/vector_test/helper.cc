#include "helper.h"

void print_py(std::vector< double > pyvec)
{
  for (int i=0; i<11; i++)
    printf("[%d] = [%f]\n", i, pyvec[i]);
}

void copy_py_to_vector(std::vector< double > pyvec, Vector *v)
{
  int nCols;
  nCols = v->GetNumCols();
  for (int i = 0; i < nCols; i++) {
    v->SetVal(i, pyvec[i]);
  }
}

void copy_py_to_matrix(std::vector< double > pyvec, Matrix *m)
{
  int nCols, nRows;
  nCols = m->GetNumCols();
  nRows = m->GetNumRows();
  for (int i = 0; i < nRows; i++) {
    for (int j = 0; j < nCols; j++) {
      m->SetVal(i, j, pyvec[i*nCols+j]);
    }
  }
}

void copy_matrix_to_py(Matrix *m, std::vector< double > pyvec) 
{
  int nCols, nRows;
  nCols = m->GetNumCols();
  nRows = m->GetNumRows();
  for (int i = 0; i < nRows; i++) {
    for (int j = 0; j < nCols; j++) {
      pyvec[i*nCols+j] = m->GetVal(i, j);
    }
  }
}
