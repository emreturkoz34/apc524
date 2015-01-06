
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
#include "standard_sort.h"
#include "quick_sort.h"
#include "bubble_sort.h"


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

/*
void bubble_sort(int* arr, int n, int* indices){
  bool swapped = true;
  int j = 0;
  int tmp;
  
  int tmpid;
  
  while(swapped){
    swapped = false;
    j++;
    for (int i = 0; i < n - j; i++){
      if(arr[i] > arr[i+1]){
	tmp = arr[i];
	arr[i] = arr[i+1];
	arr[i+1] = tmp;
	swapped = true;

	tmpid = indices[i];
	indices[i] = indices[i+1];
	indices[i+1] = tmpid;	     
      }
    }
  }

}
*/

int main(){

  
  int arr[] = {1, 3, 5, 7, 6, 4, 8, 8, 9};
  int *indices = new int[9];
  for(int i = 0 ; i<9; i++){
    indices[i] = i;
  }
  
  //bubble_sort(arr, 8, indices);
  for(int i = 0; i<9; i++){
    std::cout<<arr[i]<<" "<<indices[i]<<std::endl;
  }



  Matrix* data = new Matrix(10,2);

  assert(GenerateMatrix(data) == 0);
  WriteMatrixToFile(data, (std::string)"sorting_initialMatrix.txt");
  

  /* Indicate the sorting class used  */

  sorting* sort_alg = new brute_sort(data); 
  //sorting* sort_alg = new standard_sort(data);
  // sorting* sort_alg = new quick_sort(data);
  //sorting* sort_alg = new bubble_sort(data);

  /* Sorting settings and required functions */

  sort_alg -> SetRefColNum(0);
  sort_alg -> SetSortEndIndex(9); 
  sort_alg -> SetSortStartIndex(0);
  sort_alg -> generateIndexArray();
  sort_alg -> extractRefCol();

  /* Main routine  */
  sort_alg -> sort_data();



  assert(WriteMatrixToFile(data, (std::string)"sorting_finalMatrix.txt") == 0);

  std::cout<<"The unsorted matrix is written to: sorting_initialMatrix.txt"<<std::endl
	   <<"The sorted matrix is written to: sorting_finalMatrix.txt"<<std::endl;

  delete data;
  delete sort_alg;

  return 0;
}
