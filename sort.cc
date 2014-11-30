
#include "sort.h"


// Constructor
sorting::sorting(Matrix* data){
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
sorting::~sorting(){

}

// Main sorting body
void sorting::sortData(int colNum){
  double *refColumn = new double[nrows_];
  int *indices = new int[nrows_];

  for(int i = 0; i<nrows_; i++){
    refColumn[i] = data_->GetVal(i, colNum);
  }

  double max_ = refColumn[0];
  int index;
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

  // delete indices
  // delete refColumn
  
}
