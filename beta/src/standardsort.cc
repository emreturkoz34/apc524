
#include "standardsort.h"

typedef std::vector<size_t> index_vec_t;



/// Sequence generator for the standard sorting algorithm
class SequenceGen {
public:
  SequenceGen (int start = 0) : current(start) { }
  int operator() () {return current++;}
private:
  int current;
};



/// Comparator for the standard sorting algorithm
class CompVec{
  double * arr_;
public:
  CompVec(double* arr) : arr_(arr) {}
  bool operator()(size_t i, size_t j){
    return arr_[i] < arr_[j];
  }

};



/// Constructor
/*!
  The data to be sorted is passed to the constructor. A duplicate of the data is produced to be later at this stage
 */
StandardSort::StandardSort(Matrix* data){
  ncols_ = data->GetNumCols();
  nrows_ = data->GetNumRows();

  data_ = data; // get the pointer
  datacopy_ = new Matrix(nrows_, ncols_);

  for (int i = 0 ; i<nrows_; i++){
    for (int j = 0; j<ncols_; j++){
      datacopy_ -> SetVal(i,j, data->GetVal(i,j));
    }
  }

}

/// Destructor
StandardSort::~StandardSort(){
  delete datacopy_;
}


/// Set the reference column number
void StandardSort::SetRefColNum(int num){
  refColNum_ = num;
}

/// Main function that sorts the given data
/*!
  The algorithm sends the reference column to the standard sorting operator that is embedded into the C++ standard library

\verbatim
  INPUT 

  There are no inputs. The data to be sorted is already passed via the constructor

  OUTPUT:

  int       flag specifying whether or not the function succeeded
             = 0: success
	    != 0: something went wrong

\endverbatim
  
 */
int StandardSort::sort_data(){

  index_vec_t indices(nrows_);
  std::generate(indices.begin(), indices.end(), SequenceGen(0));

  double *refColumn = new double[nrows_];
  
  for(int i = 0; i<nrows_; i++){
    refColumn[i] = data_->GetVal(i, refColNum_);
  }

  std::sort(indices.begin(), indices.end(), CompVec(refColumn));
  

  for(int i = 0; i < nrows_; i++){
    for(int j = 0; j < ncols_; j++){
      data_->SetVal(i,j, datacopy_->GetVal(indices[i], j));
    }
  }

  
  delete [] refColumn;

  return 0;
}

