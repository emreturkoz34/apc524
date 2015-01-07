/* SimpleLNM is a class that determines the least non-monotonic
   progress variable with respect to temperature (or another specified
   column). It determines the percentage which the progress variable
   is strictly increasing and the percentage which the progress
   variable is strictly decreasing. The larger percentage not only
   determines whether the progress variable is increasing or
   decreasing, but will also be compared with the percentages of other
   progress variables. The progress variable with the largest
   percentage of increasing or decreasing values is the least
   non-monotonic progress variable. 

   If two progress variables share the highest percentages, then the
   progress variable which comes earlier in progVar is
   selected. Progress variables with neither increasing nor decreasing
   data are considered strongly non-monotonic.
 */
#include <assert.h>
#include <stdlib.h>
#include <cmath>

#include "simplelnm.h"
#include "matrix.h"

/// Constructor
SimpleLNM::SimpleLNM(const Matrix &progVar)
  : nrows_(progVar.GetNumRows()),
    ncols_(progVar.GetNumCols()),
    progVar_(progVar) {
  increasing_ = new double[ncols_];
  decreasing_ = new double[ncols_];
}

/// Destructor
SimpleLNM::~SimpleLNM() {
  delete [] increasing_;
  delete [] decreasing_;
}

/// LeastNonMonotonic calculates how much each progress variable is
/// strictly increasing and strictly decreasing. The input array
/// monoAry will initially be filled with 0s since all progress
/// variables are non-monotonic. This method will select the least
/// non-monotonic and change its value in monoAry to 1. col is the
/// reference column.
int SimpleLNM::LeastNonMonotonic(int *monoAry, const int ncols, const int col){
  assert(ncols == ncols_);

  if ((col < 0) || (col >= ncols)) {
    printf("Column %d is not a valid column number.\n", col);
    printf("The specified column must lie within 0 < col < %d.\n", ncols); 
    exit(1);
  }

  assert(monoAry != NULL && "monoAry input is a null pointer.\n");

  double *monoDomain = new double[nrows_];
  assert(progVar_.GetCol(col, monoDomain) == 0); // Domain over which monotonicity is checked (usually the temperature column of progVar_ - it is specified by the input "col")

  double *largest = new double[ncols]; // Store the largest
				       // percentages for each
				       // progress variable

  for (int j=0; j<ncols; ++j) { // Loop over cells in monoAry
    if (j != col) { // Avoid the reference column
      assert(monoAry[j] == 0 && "A monotonic progress variable exists.\n");

      double *progVarCol = new double[nrows_];
      assert(progVar_.GetCol(j, progVarCol) == 0);

      int biggerCount = 0; // Keeps track of the number of times each
			   // element in progVarCol is larger than the
			   // previous element
      int smallerCount = 0; // Keeps track of the number of times each
			    // element in progVarCol is smaller than
			    // the previous element

      // Determine amount which is increasing or decreasing
      for (int i=1; i<nrows_; ++i) {
	if (progVarCol[i] > progVarCol[i-1]) {
	  biggerCount = biggerCount + 1;
	}
	else {
	  if (progVarCol[i] < progVarCol[i-1]) {
	    smallerCount = smallerCount + 1;
	  }
	}
      }

      increasing_[j] = 1.0*biggerCount/nrows_;
      decreasing_[j] = 1.0*smallerCount/nrows_;

      if (increasing_[j] > decreasing_[j]) {
	largest[j] = increasing_[j];
      }
      else {
	if (decreasing_[j] > increasing_[j]) {
	  largest[j] = decreasing_[j];
	}
	else { // increasing_[j] == decreasing_[j])
	  if (increasing_[j] > 1.0/3.0) {
	    largest[j] = increasing_[j];
	  }
	  else { // Progress variable dominated by constant values
	    largest[j] = 0.0;
	  }
	}
      }

      delete [] progVarCol;
    }
    else { // Reference column
      increasing_[j] = 0.0;
      decreasing_[j] = 0.0;
    }
  }

  // Find progress variable with largest percentage & store index of location
  double maximum = 0.0; // Stores value of maximum percentage
  int index = -1; // Stores location of largest percentage

  for (int j=0; j<ncols; ++j) {
    if(j != col && largest[j] > maximum) {
      maximum = largest[j];
      index = j;
    }
  }

  // Check if any two or more progress variables share the same maximum percentage. If so, the progress variable with the largest magnitude slope is the least non-monotonic progress variable.

  int *maxpercent = new int[ncols]; // Used to store/mark all progress variable which share the maximum percentage with a value of 1; all other progress variables are marked with 0
  int count = 0; // Keep track of number of progress variables which share the maximum percentage

  for (int j=0; j<ncols; ++j) {
    maxpercent[j] = 0; // Initialize maxpercent
    if (largest[j] == maximum) {
      maxpercent[j] = 1; // Mark progress variables which have the maximum percentage
      count = count + 1;
    }
  }

  if (count > 1) { // If count = 1, then index = j as previously found
    double *slopes = new double[ncols];
    double maxSlope = -1.0; // Store value of greatest slope
    int indexmaxslope = -1; // Store location of greatest slope

    for (int j=0; j<ncols; ++j) {
      if (maxpercent[j] == 1) {
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
  delete [] largest;
  delete [] maxpercent;

  return 0;
}
