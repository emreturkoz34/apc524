/*! AdvancedLNM is a class that determines the least non-monotonic
   progress variable with respect to temperature (or another specified
   column). It determines the progress variable with the smallest
   percentage of non-unique (one-to-one) points and selects it as the
   least non-monotonic progress variable.

   If two or more progress variables share the smallest percentage,
   then the progress variable with the greatest magnitude slope (by
   endpoints) is selected.
*/
#include <assert.h>
#include <stdlib.h>
#include <cmath>

#include "advancedlnm.h"
#include "matrix.h"

/// Constructor
AdvancedLNM::AdvancedLNM(const Matrix &progVar)
  : nrows_(progVar.GetNumRows()),
    ncols_(progVar.GetNumCols()),
    progVar_(progVar) {
  increasing_ = new double[ncols_];
  decreasing_ = new double[ncols_];
}

/// Destructor
AdvancedLNM::~AdvancedLNM() {
  delete [] increasing_;
  delete [] decreasing_;
}

/// Method to find least monotonic progress variable
/*!  LeastNonMonotonic calculates the percentage of non-unique
points. The input array monoAry will initially be filled with 0s since
all progress variables are non-monotonic. This method will select the
least non-monotonic and change its value in monoAry to 1. col is the
reference column.
*/
int AdvancedLNM::LeastNonMonotonic(int *monoAry, const int ncols, const int col){
  assert(ncols == ncols_);

  if ((col < 0) || (col >= ncols)) {
    printf("Column %d is not a valid column number.\n", col);
    printf("The specified column must lie within 0 < col < %d.\n", ncols); 
    exit(1);
  }

  assert(monoAry != NULL && "monoAry input is a null pointer.\n");

  double *monoDomain = new double[nrows_];
  assert(progVar_.GetCol(col, monoDomain) == 0); // Domain over which monotonicity is checked (usually the temperature column of progVar_ - it is specified by the input "col")

  double *smallest = new double[ncols]; // Store the smallest
					// percentages for each
					// progress variable

  for (int j=0; j<ncols; ++j) { // Loop over cells in monoAry
    if (j != col) { // Avoid the reference column
      assert(monoAry[j] == 0 && "A monotonic progress variable exists.\n");

      double *progVarCol = new double[nrows_];
      assert(progVar_.GetCol(j, progVarCol) == 0);

      // Calculate number of non-unique points with increasing and decreasing assumptions
      double localMax = progVarCol[0]; // Keeps track of local maximum within progress variable
      double localMin = progVarCol[0]; // Keeps track of local minimum within progress variable

      int nonuniqueincreasing = 0; // Keeps track of the number of non-unique points when assuming an increasing progress variable
      int nonuniquedecreasing = 0; // Keeps track of the number of non-unique points when assuming a decreasing progress variable

      for (int i=1; i<nrows_; ++i) {
	if (progVarCol[i] > localMax) { // Increasing assumption
	  localMax = progVarCol[i];
	}
	else {
	  nonuniqueincreasing = nonuniqueincreasing + 1;
	}

	if (progVarCol[i] < localMin) { // Decreasing assumption
	  localMin = progVarCol[i];
	}
	else {
	  nonuniquedecreasing = nonuniquedecreasing + 1;
	}
      }
      
      // Store percentage of non-unique data
      increasing_[j] = 1.0*nonuniqueincreasing/nrows_; 
      decreasing_[j] = 1.0*nonuniquedecreasing/nrows_;
      
      // Store smaller of values between increasing_[] and decreasing_[] arrays in smallest[]
      if (increasing_[j] < decreasing_[j]) {
	smallest[j] = increasing_[j];
      }
      else {
	smallest[j] = decreasing_[j];
      }

      delete [] progVarCol;
    }
    else { // Reference column
      increasing_[j] = -1.0;
      decreasing_[j] = -1.0;
      smallest[j] = -1.0;
    }
  }

  // Find progress variable with smallest percentage & store index of location
  double minimum = 1.0; // Stores value of smallest percentage
  int index = -1; // Stores location of smallest percentage

  for (int j=0; j<ncols; ++j) {
    if(j != col && smallest[j] < minimum) {
      minimum = smallest[j];
      index = j;
    }
  }

  // Check if any two or more progress variables share the same
  // minimum percentage. If so, the progress variable with the
  // largest magnitude slope is the least non-monotonic progress
  // variable.

  int *minpercent = new int[ncols]; // Used to store/mark all progress variable which share the minimum percentage with a value of 1; all other progress variables are marked with 0
  int count = 0; // Keep track of number of progress variables which share the minimum percentage

  for (int j=0; j<ncols; ++j) {
    minpercent[j] = 0; // Initialize minpercent
    if (j != col && smallest[j] == minimum) {
      minpercent[j] = 1; // Mark progress variables which have the minimum percentage
      count = count + 1;
    }
  }

  if (count > 1) { // If count = 1, then index = j as previously found
    double *slopes = new double[ncols];
    double maxSlope = -1.0; // Store value of greatest slope
    int indexmaxslope = -1; // Store location of greatest slope

    for (int j=0; j<ncols; ++j) {
      if (minpercent[j] == 1) {
	slopes[j] = std::abs((progVar_.GetVal(nrows_-1, j) - progVar_.GetVal(0, j))/nrows_); // Calculate the magnitude of the slope of the progress variable using endpoints
	if (slopes[j] > maxSlope) {
	  maxSlope = slopes[j];
	  indexmaxslope = j;
	}
      }
      else {
	slopes[j] = -1.0; // Progress variable isn't considered
      }
    }

    index = indexmaxslope; // Set location to progress variable with largest magnitude slope
    delete [] slopes;
  }

  assert(index >= 0 && "All progress variables are mainly constant.\n");

  // Rewrite monoAry to have a value of 1 for the least non-monotonic
  // progress variable and leave the other values untouched.
  monoAry[index] = 1;

  delete [] monoDomain;
  delete [] smallest;
  delete [] minpercent;

  return 0;
}
