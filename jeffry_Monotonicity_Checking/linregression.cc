/* linregression is a class that determines the most monotonic progress variable with respect to temperature (or another specified column). It calculates the slope of the best linear approximation for each progress variable and selects the largest.

   The slope is given by {sum_i=1_i=N (C_i-C_ave)(T_i-T_ave)}/{sum_i=1_i=N (T_i-T_ave)^2}
 */
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

#include "maxslope.h"
#include "linregression.h"
#include "matrix.h"

/// Constructor
LinRegression::LinRegression(const Matrix &progVar)
  : nrows_(progVar.GetNumRows()),
    ncols_(progVar.GetNumCols()),
    progVar_(progVar) {
  slopes_ = new double[ncols_];
}

/// Destructor
LinRegression::~LinRegression() {
  delete [] slopes_;
}

/// MostMonotonic calculates the slope of the best linear approximation for each progress variable which is strictly increasing. The output array monoAry must be of length ncols_, where each cell holds a value of 3 if C is strictly increasing and has the largest slope, 2 if C is strictly increasing but does not have the largest slope, and 0 for non-monotonic C.
int LinRegression::MostMonotonic(const int col, int *monoAry){
  if ((col < 0) || (col >= ncols_)) {
    printf("Column %d is not a valid column number.\n", col);
    printf("The specified column must lie within 0 < col < %d.\n", ncols_); 
    exit(1);
  }

  if (monoAry == NULL) {
    printf("monoAry input is a null pointer.\n");
    exit(1);
  }

  /*
  // Check whether monoAry contains any monotonic progress variables
  int sum = 0;
  for (int j=0; j<ncols_; ++j) {
    sum = sum + monoAry[j];
  }
  if (sum == 3) {

  }
  */

  const double *monoDomain = progVar_.GetCol(col); // Domain over which monotonicity is checked (usually the temperature column of progVar_ - it is specified by the input "col")

  // Calculate average domain value (usually average temperature)
  double Tsum = 0.0;
  for (int itr=0; itr<nrows_; ++itr) {
    Tsum = Tsum + monoDomain[itr];
  }
  double Tave = Tsum/nrows_;

  for (int j=0; j<ncols_; ++j) { // Loop over cells in monoAry
    if (monoAry[j] == 3) { // Monotonic progress variable
      const double *progVarCol = progVar_.GetCol(j);

      // Calculate average progress variable
      double Csum = 0.0;
      for (int i=0; i<nrows_; ++i) {
	Csum = Csum + progVarCol[i];
      }
      double Cave = Csum/nrows_;

      // Calculate slope of best fit line
      double sumNumerator = 0.0;
      double sumDenominator = 0.0;
      double slope = -1.0;

      for (int i=0; i<nrows_; ++i) {
	sumNumerator = sumNumerator + (progVarCol[i]-Cave)*(monoDomain[i]-Tave);
	sumDenominator = sumDenominator + (monoDomain[i]-Tave)*(monoDomain[i]-Tave);
      }

      if (sumDenominator != 0) {
	slope = sumNumerator/sumDenominator;
      }
      else {
	printf("Unable to calculate slope of best fit line.\n");
	exit(1);
      }

      slopes_[j] = slope; // Store slope 
    }
  }

  if (slope == -1.0) {
    return 1;
  }
  return 0;
}
