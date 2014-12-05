#include <stdio.h>
#include <stdlib.h>
#include "matrix.h"
#include "lininterp.h"

// Print contents of Matrix object
void printMat(const Matrix* mat) {
	for (int i = 0; i < mat->GetNumRows(); i++) {
		for (int j = 0; j < mat->GetNumCols(); j++) {
			printf("%6.3f ", mat->GetVal(i, j));
		}
		printf("\n");
	}
}

// Print contents of an array
void printArr(const double* data, int len) {
	for (int i = 0; i < len; i++) {
		printf("%6.3f ", data[i]);
	}
	printf("\n");
}

int main(int argc, char *argv[]) {

	if (argc != 3) {
		printf("USAGE: %s <interpolation column> <interpolation value>\n", argv[0]);
		exit(1);
    }

	// Set up a matrix object
	const int rows = 7;
	const int cols = 10;
	Matrix *mat = new Matrix(rows, cols);
	
	// Fill in the matrix with numbers
	for (int i = 0; i < rows; i++) {
		for (int j = 0; j < cols; j++) {
			mat->SetVal(i, j, i*j + 1);
		}
	}
	
	// Print the matrix
	printf("The matrix is: \n");
	printMat(mat);
	
	// Set up linear interpolator
	Interpolator *linterp;
	linterp = new LinInterp();
	const int icol = atoi(argv[1]);    // interpolation column
	const double ival = atof(argv[2]); // interpolation value
	double *vecout = new double[cols]; // interpolated row
	
	// Make sure interpolation column is within bounds
	if (icol < 0 || icol >= cols) {
		printf("\nInterpolation failed: interpolation column out of bounds\n");
		exit(1);
	}
	
	// Perform linear interpolation
	int flag = linterp->Interp(mat, icol, ival, vecout);
	if (flag == 1) {
		printf("\nInterpolation failed: interpolation value out of bounds\n");
		exit(1);
	}
	
	// Print the interpolated row
	printf("\nInterpolating along column %i at %.3f:\n", icol, ival);
	printArr(vecout, cols);
	
	// Free memory
	delete mat;
	delete linterp;
	delete[] vecout;
	
	return 0;
}
