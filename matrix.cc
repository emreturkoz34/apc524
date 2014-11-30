/* Matrix is a class which represents a 2D matrix of size rows x cols with a 1D array of length rows*cols.

 */
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
  delete[] matrix_;
}

/// Get the value at a specified index
double Matrix::GetVal(int i, int j) const{
  return matrix_[i*ncols_ + j];
}

/// Set the value at a specific location
void Matrix::SetVal(int i, int j, double val){
  matrix_[i*ncols_ + j] = val;
}

/// Return the number of rows
int Matrix::GetNumRows() const{
  return nrows_;
}

/// Return the number of columns
int Matrix::GetNumCols() const{
  return ncols_;
}

/// Return an array containing column j
int Matrix::GetCol(int j, double *colAry) const{
  if (colAry == NULL) {
    printf("colAry is not initialized properly.\n");
    exit(1);
  }

  for (int i=0; i<nrows_; ++i) {
    colAry[i] = GetVal(i, j);
  }
  return 0;
}



