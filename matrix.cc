#include <assert.h>
#include "matrix.h"

/// Constructor
Matrix::Matrix(int rows, int cols)
  : nrows_(rows),
    ncols_(cols) {
  matrix_ = new double[nrows_*ncols_];
}

/// Destructor
Matrix::~Matrix(){
  delete matrix_ [];
}

/// Get the value at a specified index
double Matrix::GetVal(int i, int j){
  return matrix_[i*ncols_ + j];
}

/// Set the value at a specific location
void Matrix::SetVal(int i, int j, double val){
  matrix_[i*ncols_ + j] = val;
}


