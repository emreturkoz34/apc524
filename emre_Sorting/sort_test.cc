
// Standard C includes
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <assert.h>

// User defined library includes
#include "matrix.h"
#include "brute_sort.h"




/*
  Test routine for sorting algorithms. This file includes three functions:

  1. GenerateMatrix : This is a hard-coded (n x 2) matrix generator. 
  The first column of data is generated using -x(x-#rows) to have a sample data set to be sorted
  The second column is integers starting from 0 to #nrows-1 to check whether the sorting is performed
  as it should be.

  2. WriteMatrixToFile : A routine to write the initial and final matrices to files for testing

  3. main : The main routine for test. The program generates a simple matrix through generate matrix
  and it is sorted by the brute_sort algorithm.

 */





int GenerateMatrix(Matrix* mat){
  
  double val = 0.0;
  int j;
  

  j = 0;
  for(int i = 0; i< mat->GetNumRows(); i++){
    val = i*(i-(mat->GetNumRows()-1));
    mat->SetVal(i,j, -val);
  }

  j = 1;
  for (int i = 0 ; i< mat->GetNumRows(); i++){
    val = i;
    mat->SetVal(i,j, val);
  }

  return 0;

}

int WriteMatrixToFile(Matrix* mat, std::string path){

  std::ofstream output;
  output.open(path.c_str());
  
  for(int i = 0; i < mat->GetNumRows(); i++){
    for (int j = 0; j < mat->GetNumCols(); j++){
      output<<mat->GetVal(i,j)<<" ";
    }
    output<<std::endl;
  }
  
  return 0;

}




int main(){
  

  Matrix* data = new Matrix(9,2);

  assert(GenerateMatrix(data) == 0);
  WriteMatrixToFile(data, (std::string)"sorting_initialMatrix.txt");
  

  sorting* sort_alg = new brute_sort(data); 
  sort_alg -> SetRefColNum(0);
  sort_alg -> sort_data();

  assert(WriteMatrixToFile(data, (std::string)"sorting_finalMatrix.txt") == 0);

  std::cout<<"The unsorted matrix is written to: sorting_initialMatrix.txt"<<std::endl
	   <<"The sorted matrix is written to: sorting_finalMatrix.txt"<<std::endl;

  return 0;
}
