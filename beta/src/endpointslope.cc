/* EndPointSlope is a class that determines the most monotonic
 * progress variable with respect to temperature (or another specified
 * column). It calculates the slope from the first and last endpoints
 * of each progress variable column and selects the progress variable
 * with the largest magnitude slope.
 *
 * The slope is given by [C_i(N)-C_i(1)]/N
 */
#include <assert.h>
#include <stdlib.h>
#include <cmath>

#include "endpointslope.h"
#include "matrix.h"

/// Constructor
EndPointSlope::EndPointSlope(const Matrix &progVar)
  : nrows_(progVar.GetNumRows()),
    ncols_(progVar.GetNumCols()),
    progVar_(progVar) {
  slopes_ = new double[ncols_];
}

/// Destructor
EndPointSlope::~EndPointSlope() {
  delete [] slopes_;
}

/// MostMonotonic calculates the slope of the best linear
/// approximation for each progress variable which is strictly
/// increasing or strictly decreasing. The output array monoAry must
/// be of length ncols, where each cell holds a value of 3 if C is
/// strictly monotonic and has the largest slope, 2 if C is strictly
/// monotonic but does not have the largest slope, and 0 for
/// non-monotonic C. col is the reference column.

int EndPointSlope::MostMonotonic(int *monoAry, const int ncols, const int col){
  assert(ncols == ncols_);

  if ((col < 0) || (col >= ncols)) {
    printf("Column %d is not a valid column number.\n", col);
    printf("The specified column must lie within 0 < col < %d.\n", ncols); 
    exit(1);
  }

  assert(monoAry != NULL && "monoAry input is a null pointer.\n");

  for(int j=0; j<ncols; ++j) {
    if (monoAry[j] == 3) { // Monotonic progress variable
      const double begin = progVar_.GetVal(0, j);
      const double end = progVar_.GetVal(nrows_-1, j);
      double slope = (end - begin)/nrows_;
      slopes_[j] = slope; // Store slope
    }
    else { // Not monotonic
      slopes_[j] = 0.0; // Set slope to 0 to indicate a non-monotonic progress variable
    }
  }

  /*
  // Print slopes for testing purposes
  printf("Slopes from endpoints for strictly monotonic C:\n");
  for (int j = 0; j<ncols; ++j) {
    printf("%6.3f\t", slopes_[j]);
  }
  printf("\n");
  */

  // Find slope with the maximum magnitude in slopes_ array & store
  // index of location
  double maxSlope = 0.0; // Stores value of maximum slope of best fit line for monotonic progress variables
  int index = -1; // Stores location of maximum slope value 

  for (int j=0; j<ncols; ++j) {
    if(monoAry[j] == 3 && std::abs(slopes_[j]) > maxSlope) {
      maxSlope = slopes_[j];
      index = j;
    }
  }

  assert(index >= 0 && "No progress variable is monotonic.\n");

  // Rewrite monoAry to have values of 3 for the best monotonic
  // progress variable, 2 for progress variables that are monotonic
  // but not the best, and 0 otherwise
  for (int j=0; j<ncols; ++j) {
    if (j == index) { // Best progress variable
      monoAry[j] = 3;
    }
    else {
      if (monoAry[j] == 3) {
	monoAry[j] = 2;
      }
    }
  }

  return 0;
}
