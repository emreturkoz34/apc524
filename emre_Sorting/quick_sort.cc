
#include "quick_sort.h"


/// Constructor
quick_sort::quick_sort(Matrix* data){
  ncols_ = data->GetNumCols();
  nrows_ = data->GetNumRows();

  data_ = data; // get the pointer
  datacopy_ = new Matrix(nrows_, ncols_);
  
  for (int i = 0; i<nrows_; i++){
    for(int j = 0; j<ncols_; j++){
      
      datacopy_->SetVal(i,j, data->GetVal(i,j));

    }
    
  }
  
}

/// Destructor
quick_sort::~quick_sort(){
  delete datacopy_;
}


/// Set the reference column number
void quick_sort::SetRefColNum(int num){
  refColNum_ = num;
}

/// Setting the sort start index
void quick_sort::SetSortStartIndex(int left){
  left_ = left;
}

/// Setting the sort end index
void quick_sort::SetSortEndIndex(int right){
  right_ = right;
}


/// Generate the index array
int quick_sort::generateIndexArray(){
  
  /*
  if (nrows_ == NULL){
    std::cout<<"Fatal error: Size of the data is not given as input!"<<std::endl;
    }*/

  indices_ = new int[nrows_];

  for (int i =0; i<nrows_; i++){
    indices_[i] = i;
  }
 

  return 0;
}

/// Extract the reference column
int quick_sort::extractRefCol(){

  /*
  if ( (nrows_ == NULL) || (refColNum_ == NULL)){
    std::cout<<"Fatal error: #rows of reference col. # not set"<<std::endl;
    exit(1);
    }*/

  refColumn_ = new double[nrows_];

  for(int i = 0; i<nrows_; i++){
    refColumn_[i] = data_->GetVal(i, refColNum_);
  }
  
  

  return 0;
}




/// Main sorting body
int quick_sort::sort_data(){

  int i = left_, j = right_;
  double tmp; int idtmp;
  int pivot = refColumn_[(left_ + right_) / 2];

  
  /* partition */
  while (i <= j) {
    while (refColumn_[i] < pivot)
      i++;
    while (refColumn_[j] > pivot)
      j--;
    if (i <= j) {
      tmp = refColumn_[i];
      refColumn_[i] = refColumn_[j];
      refColumn_[j] = tmp;

      idtmp = indices_[i];
      indices_[i] = indices_[j];
      indices_[j] = idtmp;
      i++;
      j--;
    }
  };
 
  /* recursion */
  if (left_ < j){
    right_ = j;
    sort_data();
  }
  if (i < right_){
    left_ = i;
    sort_data();
  }
  
  for (int i = 0; i < nrows_; i++){
    for(int j = 0; j < ncols_; j++){
      data_ -> SetVal(i,j, datacopy_->GetVal(indices_[i], j));
    }
  }



  return 0;
}
