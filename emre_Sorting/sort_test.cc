
// Standard C includes
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

// User defined library includes
#include "matrix.h"
#include "brute_sort.h"



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

}




int main(){
  

  Matrix* data = new Matrix(9,2);

  GenerateMatrix(data);
  WriteMatrixToFile(data, (std::string)"initialMatrix.txt");
  

  sorting* sort_alg = new brute_sort(data); 
  sort_alg -> SetRefColNum(0);
  sort_alg -> sort_data();

  WriteMatrixToFile(data, (std::string)"finalMatrix.txt");

  std::cout<<"Everything seems to be OK!"<<std::endl;

  return 0;
}
