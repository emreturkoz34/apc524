/* Matrix is a class which represents a 2D matrix of size rows x cols with a 1D array of length rows*cols.

 */
#include <assert.h>
#include "vector.h"

/// Constructor
Vector::Vector(int cols)
  : ncols_(cols) {
  vector_ = new double[ncols_];
  for (int i = 0; i < cols; i++) {
    vector_[i] = 0;
  }
}

/// Destructor
Vector::~Vector(){
  delete[] vector_;
}

/// Get the value at a specified index
double Vector::GetVal(int i) const{
  return vector_[i];
}

/// Set the value at a specific location
void Vector::SetVal(int i, double val){
  vector_[i] = val;
}

/// Return the number of columns
int Vector::GetNumCols() const{
  return ncols_;
}


