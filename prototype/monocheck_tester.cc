/* monocheck_tester is a program which tests the robustness of
 * monocheck.cc. For testing purposes, it will also check the
 * robustness of linregression.cc. In the actual program, monoAry will
 * be passed to the max slope/least non-monotonic methods by Python.
 *
 * To run this program, call "check_monotonic" from the terminal after
 * running "make clean" and "make".
 */

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

#include "matrix.h"
#include "monocheck.h"

#include "linregression.h"

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
    for (int j=0; j<cols-1; ++j) {
      progVar->SetVal(i, j, count);
      count = count + 1;
    }
  }
  for (int j=0; j<cols-1; ++j) {
    progVar->SetVal(rows-1, j, 11.0);
  }
  for (int i=0; i<rows; ++i) { // Set last column as decreasing
    progVar->SetVal(i, cols-1, count);
    count = count - 5;
  }

  // Print out matrix progVar to ensure proper initialization of values
  printf("Test matrix:\n");
  PrintState(rows, cols, *progVar);

  MonoCheck *checker = new MonoCheck(*progVar);
  int *monoAry = new int[cols]; // Array to store monotonicity output

  assert(checker->CheckStrictMonoticity(0, monoAry) == 0 && "CheckStrictMonoticity ran unsuccessfully.\n"); // Check which columns of progVar are strictly increasing or strictly decreasing and store result in monoAry

  printf("Strictly monotonic progress variables marked:\n");
  for (int j = 0; j<cols; ++j) {
    printf("%d\t", monoAry[j]); // Print output array filled with 3s or 0s
  }
  printf("\n");

  // Max slope testing commences
  MaxSlope *maxchecker = new LinRegression(*progVar);
  assert(maxchecker->MostMonotonic(0, monoAry) == 0 && "MostMonotonic ran unsuccessfully.\n"); // Distinguish the best monotonic progress variables

  printf("Best C indicated:\n");
  for (int j = 0; j<cols; ++j) {
    printf("%d\t", monoAry[j]); // Print output array filled with 3s, 2s, and 0s
  }
  printf("\n");

  delete checker;
  delete maxchecker;

  return 0;
}
