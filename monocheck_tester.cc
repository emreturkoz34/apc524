/* monocheck_tester is a program which tests the robustness of monocheck.cc

To run this program, call "check_monotonic" from the terminal after running "make clean" and "make".
 */

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

#include "matrix.h"
#include "monocheck.h"

/// Print progVar matrix
/// progVar[0] progVar[1] ... progVar[ncols-1]
/// progVar[ncols] progVar[ncols+1] ... progVar[2*ncols-1]
/// ... 
/// progVar[(nrows-1)*ncols] progVar[(nrows-1)*ncols+1] ... progVar[nrows*ncols-1]
/// to standard out
void PrintState(int nrows, int ncols, const Matrix &progVar) {
  for (int i = 0; i<nrows; ++i) {
    for (int j = 0; j<ncols; ++j) {
      printf("%f\t", progVar.GetVal(i, j));
    }
    printf("\n");
  }
}

int main(int argc, char *argv[]) {
  const int rows = 5;
  const int cols = 4;
  int count = 0;
  Matrix *progVar = new Matrix(rows, cols);

  // Initialize test matrix progVar with values
  for (int i=0; i<rows-1; ++i) {
    for (int j=0; j<cols; ++j) {
      progVar->SetVal(i, j, count);
      count = count + 1;
    }
  }
  for (int j=0; j<cols; ++j) {
    progVar->SetVal(rows-1, j, 14.0);
  }

  // Print out matrix progVar to ensure proper initialization of values
  PrintState(rows, cols, *progVar);

  MonoCheck *checker = new MonoCheck(*progVar);
  int *monoAry = new int[cols]; // Array to store monotonicity output

  int success = checker->CheckIncreasing(0, monoAry); // Check which columns of progVar are monotonically increasing and store result in monoAry

  for (int j = 0; j<cols; ++j) {
    printf("%d\t", monoAry[j]); // Print output array filled with 3s or 0s
  }
  printf("\n");

  if (success == 1) {
    printf("CheckIncreasing ran unsuccessfully.\n");
    exit(1);
  }
  else {
    return 0;
  }
}
