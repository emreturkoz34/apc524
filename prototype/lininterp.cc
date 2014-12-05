#include "lininterp.h"
#include <limits>
#include <stdlib.h>
#include <stdio.h>
#include <iostream>

// Constructor
LinInterp::LinInterp() {}

// Destructor
LinInterp::~LinInterp() {}

// Linear interpolation function
int LinInterp::Interp(const Matrix *matin, int col, double ival, double *vecout) {
	// Find the rows about which to interpolate
	int row1 = -1, row2 = -1;
	double val2 = std::numeric_limits<double>::max(), val1 = -val2;
	double tempval = 0;
	for (int i = 0; i < matin->GetNumRows(); ++i) {
		tempval = matin->GetVal(i, col);
		if (tempval > val1 && tempval <= ival) {
			row1 = i;
			val1 = tempval;
		}
		if (tempval < val2 && tempval >= ival) {
			row2 = i;
			val2 = tempval;
		}
	}
	
	// Check if proper interpolation rows found
	if (row1 == -1 || row2 == -1) {
		return 1; // failure
	}

	// Perform linear interpolation
	if (val1 == val2) {
		for (int j = 0; j < matin->GetNumCols(); ++j) {
			vecout[j] = matin->GetVal(row1, j);
		}
	} else {
		for (int j = 0; j < matin->GetNumCols(); ++j) {
			vecout[j] = matin->GetVal(row1, j) + (ival - val1)*(matin->GetVal(row2, j) - matin->GetVal(row1, j))/(val2 - val1);
		}
	}

	return 0; // success
}
