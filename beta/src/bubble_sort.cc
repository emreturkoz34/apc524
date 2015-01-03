
#include "bubble_sort.h"

// Constructor
bubble_sort::bubble_sort(Matrix *data){
  nrows_ = data->GetNumRows();
  ncols_ = data->GetNumCols();

  data_ = data;
  datacopy_ = new Matrix(nrows_, ncols_); // duplicate data

  for(int i = 0; i<nrows_; i++){
    for(int j = 0; j<ncols_; j++){
      datacopy_ -> SetVal(i,j, data->GetVal(i,j));
    }
  }

}

// Destructor
bubble_sort::~bubble_sort(){
  delete datacopy_;
}

// Set the reference column number
void bubble_sort::SetRefColNum(int num){
  refColNum_ = num;
}


/// Generate the index array
int bubble_sort::generateIndexArray(){
  indices_ = new int[nrows_];
  
  for(int i = 0; i<nrows_; i++){
    indices_[i] = i;
  }

  return 0;

}

/// Extract the reference column
int bubble_sort::extractRefCol(){
  refColumn_ = new double[nrows_];
  
  for(int i = 0; i<nrows_; i++){
    refColumn_[i] = data_->GetVal(i, refColNum_);
  }

  return 0;
}


// Main sorting body
int bubble_sort::sort_data(){
  bool swapped = true;
  int j = 0;
  double tmp;
  int tmpid;

  while(swapped){
    swapped = false;
    j++;
    for(int i=0; i< nrows_- j; i++){
      if (refColumn_[i] > refColumn_[i+1]){
	tmp = refColumn_[i];
	refColumn_[i] = refColumn_[i+1];
	refColumn_[i+1] = tmp;
	swapped = true;

	tmpid = indices_[i];
	indices_[i] = indices_[i+1];
	indices_[i+1] = tmpid;
      }
    }
  }

  
  for (int i = 0; i < nrows_; i++){
    for(int j = 0; j < ncols_; j++){
      data_ -> SetVal(i,j, datacopy_->GetVal(indices_[i], j));
    }
  }
  

  return 0;

}
