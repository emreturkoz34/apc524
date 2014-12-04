
#include "brute_sort.h"


/*
  This sorting algortihm is built upon the base class developed at sorting.h
  
  The main sorting algorithm is executed using sort_data()
  
  This algorithm goes over the each entry (#rows times) at the selected column, finds the
  maximum entry, records its index. This is repeated #rows times until the indices of the 
  entries are obtained in order. Then each column of the matrix is reordered using these
  indices.

 */



// Constructor
brute_sort::brute_sort(Matrix* data){
  ncols_ = data->GetNumCols();
  nrows_ = data->GetNumRows();

  data_ = data; // get the pointer
  datacopy_ = new Matrix(nrows_, ncols_); // duplicate data
  
  for(int i = 0; i<nrows_; i++){
    for (int j = 0; j<ncols_; j++){
      datacopy_->SetVal(i,j,data->GetVal(i,j));
    }
  }

}

// Instructor
brute_sort::~brute_sort(){

}

// Set the reference column number
void brute_sort::SetRefColNum(int num){
  refColNum_ = num;
}


// Main sorting body
int brute_sort::sort_data(){
  double *refColumn = new double[nrows_];
  int *indices = new int[nrows_];

  for(int i = 0; i<nrows_; i++){
    refColumn[i] = data_->GetVal(i, refColNum_);
  }

  double max_ = refColumn[0];
  int index = 0;
  for (int i = 0; i<nrows_; i++){
    for(int j = 0; j<nrows_; j++){
      
      if(refColumn[j] >= max_){
	max_ = refColumn[j];
	index = j;  
      }
    }
    refColumn[index] = -1;
    indices[i] = index;
    max_ = refColumn[i];
  }
  
  for(int i = 0; i< nrows_; i++){
    for(int j = 0; j<ncols_; j++){
      data_->SetVal(i,j, datacopy_->GetVal(indices[i], j));
    }
  }

  delete [] indices;
  delete [] refColumn;  

  return 0;
}
