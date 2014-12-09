/* Matrix is a class which represents a 2D matrix of size rows x cols with a 1D array of length rows*cols.

 */
#include <assert.h>
#include "vector.h"

/// Constructor
Vector::Vector(int rows, int cols)
  : nrows_(rows),
    ncols_(cols) {
  vector_ = new double[nrows_*ncols_];
}

/// Destructor
Vector::~Vector(){
  delete[] vector_;
}

/// Get the value at a specified index
double Vector::GetVal(int i, int j) const{
  return vector_[i*ncols_ + j];
}

/// Set the value at a specific location
void Vector::SetVal(int i, int j, double val){
  vector_[i*ncols_ + j] = val;
}

/// Return the number of rows
int Vector::GetNumRows() const{
  return nrows_;
}

/// Return the number of columns
int Vector::GetNumCols() const{
  return ncols_;
}


