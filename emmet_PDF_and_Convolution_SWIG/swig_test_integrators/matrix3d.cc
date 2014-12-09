



#include <assert.h>
#include "matrix3d.h"

/// Constructor
Matrix3D::Matrix3D(int dim1, int dim2, int dim3)
  : dim1_(dim1),
    dim2_(dim2),
    dim3_(dim3) {
  matrix_ = new double[dim1_*dim2_*dim3_];
}

/// Destructor
Matrix3D::~Matrix3D(){
  delete [] matrix_;
}

/// Get the value at a specified index
double Matrix3D::GetVal(int i, int j, int k) const{
  return matrix_[i*dim3_*dim2_ + j*dim3_ + k];
}

/// Set the value at a specified index
void Matrix3D::SetVal(int i, int j, int k, double val){
  matrix_[i*dim3_*dim2_ + j*dim3_ + k] = val;
}

/// Return dim1
int Matrix3D::GetNumDim1() const{
  return dim1_;
}

/// Return dim2
int Matrix3D::GetNumDim2() const{
  return dim2_;
}

/// Return dim3
int Matrix3D::GetNumDim3() const{
  return dim3_;
}
