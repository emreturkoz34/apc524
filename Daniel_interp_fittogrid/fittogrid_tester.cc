#include <stdio.h>
#include <stdlib.h>
#include "matrix4d.h"
#include "matrix3d.h"
#include "fittogrid.h"
#include "lininterp.h"

int main(int argc, char *argv[]) {
	/* This program tests the fittogrid function. fittogrid takes a 4d matrix as input and
	interpolates along a given cgrid. For clarity of presentation, in this case the 4d 
	matrix will be 2-by-1-by-1-by-10, essentially a 2d matrix. The first row will be 10 
	values of w~, and the second row will be 10 values of c~. fittogrid will interpolate 
	to find values of w~ at values of c~ given by cgrid. */
	
	// Set up inputs to fittogrid function
	const int dim1 = 2;    // w~ and c~
	const int dim2 = 1;    // dimension of z~
	const int dim3 = 1;    // dimension of z_v
	const int dim4 = 10;   // number of files
	const int lcgrid = 10; // length of cgrid
	Matrix4D *datain = new Matrix4D(dim1, dim2, dim3, dim4);
	double cgrid [lcgrid];
	Interpolator *interp;
	interp = new LinInterp(); // use linear interpolator
	Matrix3D *dataout = new Matrix3D(dim2, dim3, lcgrid);
	
	// Fill datain with numbers
	for (int i = 0; i < dim4; i++) {
		datain->SetVal(0, 0, 0, i, i*i); // w~
		datain->SetVal(1, 0, 0, i, i + 1); // c~
	}
	
	// Fill cgrid with numbers
	for (int i = 0; i < lcgrid; ++i) {
		cgrid[i] = 2.5 + i/2.0;
	}
	
	// Print the input w~ and c~
	char dummy[] = "wc";
	for (int i = 0; i < 2; ++i) {
		printf("%c~ is:\n", dummy[i]);
		for (int j = 0; j < dim4; ++j) {
			printf("%6.3f ", datain->GetVal(i, 0, 0, j));
			//printf("%i ", datain->GetVal(i, 0, 0, j));
		}
		printf("\n\n");
	}
	
	// Print cgrid
	printf("cgrid is:\n");
	for (int i = 0; i < lcgrid; ++i) {
		printf("%6.3f ", cgrid[i]);
	}
	printf("\n\n");
		
	// Interpolate w~ along the cgrid
	int flag = fittogrid(datain, cgrid, interp, dataout);
	if (flag == 1) {
		printf("\nInterpolation failed: interpolation value out of bounds\n");
		exit(1);
	}
	
	// Print w~ values interpolated along cgrid
	printf("w~ inteprolated along cgrid is:\n");
	for (int i = 0; i < lcgrid; ++i) {
		printf("%6.3f ", dataout->GetVal(0, 0, i));
	}
	printf("\n\n");
	
	// Free memory
	delete datain;
	delete dataout;
	delete interp;
	
	return 0; // success
}
