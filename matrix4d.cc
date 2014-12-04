#include <assert.h>
#include "matrix4d.h"


/// Constructor
Matrix4D::Matrix4D(int dim1, int dim2, int dim3, int dim4)
  : dim1_(dim1),
    dim2_(dim2),
    dim3_(dim3),
    dim4_(dim4) {
  
  matrix_ = new double[dim1_*dim2_*dim3_*dim4_];
}

/// Destructor
Matrix4D::~Matrix4D(){
  delete [] matrix_;
}

/// Get the value at a specified index
double Matrix4D::GetVal(int i, int j, int k){
  return matrix_[i*dim4_*dim3_*dim2_ + j*dim4_*dim3_ + k*dim4_ + l];
}

/// Set the value at a specified index
void Matrix4D::SetVal(int i, int j, int k, int l, double val){
  matrix_[i*dim4_*dim3_*dim2_ + j*dim4_*dim3_ + k*dim4_ + l] = val;
}

/// Return dim1
int Matrix4D::GetNumDim1(){
  return dim1_;
}

/// Return dim2
int Matrix4D::GetNumDim2(){
  return dim2_;
}

/// Return dim3
int Matrix4D::GetNumDim3(){
  return dim3_;
}

/// Return dim4
int Matrix4D::GetNumDim4(){
  return dim4_;
}
