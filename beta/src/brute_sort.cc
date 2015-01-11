
#include "brute_sort.h"


/*!
  This algorithm goes over the each entry (#rows times) at the selected column, finds the
  maximum entry, records its index. This is repeated #rows times until the indices of the 
  entries are obtained in order. Then each column of the matrix is reordered using these
  indices.

 */



/// Constructor
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

/// Destructor
brute_sort::~brute_sort(){
  //delete data_;
  delete datacopy_;
}

/// Set the reference column number
void brute_sort::SetRefColNum(int num){
  refColNum_ = num;
}


/// Main function that sorts the given data
/*!
  The algortihm processes the reference column and sorts it using the brute sort approach.

  \verbatim
  INPUT:

  There are no inputs. The data to be sorted is already passed via the constructor

  
  OUTPUT:

  int          flag specifying whether or not the function succeeded
                = 0: success
	       != 0: something went wrong

  \endverbatim


 */
int brute_sort::sort_data(){
  double *refColumn = new double[nrows_];
  int *indices = new int[nrows_];

  for(int i = 0; i<nrows_; i++){
    refColumn[i] = data_->GetVal(i, refColNum_);
  }

  double min_ = refColumn[0];
  int index = 0;
  for (int i = 0; i<nrows_; i++){
    for(int j = 0; j<nrows_; j++){
      
      if(refColumn[j] <= min_){
	min_ = refColumn[j];
	index = j;  
      }
    }
    refColumn[index] = 999999; // a value that is high enough
    indices[i] = index;
    min_ = refColumn[i];
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
