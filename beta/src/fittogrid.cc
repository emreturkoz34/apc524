#include "fittogrid.h"

int fittogrid(Matrix4D *datain, const double *cgrid, Interpolator *interp, Matrix3D *dataout) {
  // Assume datain is 4d matrix (mean, z~, z_v, file)
  // mean has dimension 2, contains w~ and c~
  // Interpolate w~ at c~ values given by cgrid input
  // dataout is 3d matrix (z~, z_v, cgrid), values are wgrid

  int flag1 = 0; // flag indicating success or failure

  // Retrieve matrix dimensions
  const int dim2 = datain->GetNumDim2();
  const int dim3 = datain->GetNumDim3();
  const int nfiles = datain->GetNumDim4();
  const int lcgrid = dataout->GetNumDim3();

  Matrix *tmat = new Matrix(nfiles, 2); // temp matrix for interpolation
  double tarr [2]; // temporary array for interpolation output
  int flag; // flag indicating status of interpolation
  Matrix3D *extrap = new Matrix3D(dim2, dim3, lcgrid); // matrix indicating whether or not extrapolation attempted

  // Loop over all z~, z_v
  for (int i = 0; i < dim2; ++i) {
    for (int j = 0; j < dim3; ++j) {
      // Store w~ and c~ for all files in a nfiles-by-2 matrix:
      for (int k = 0; k < nfiles; k++) {
	tmat->SetVal(k, 0, datain->GetVal(0, i, j, k)); // w~
	tmat->SetVal(k, 1, datain->GetVal(1, i, j, k)); // c~
      }

      // Loop over values in cgrid, interpolate to find wgrid
      for (int k = 0; k < lcgrid; k++) {
	flag = interp->Interp(tmat, 1, cgrid[k], tarr, 2);
	if (flag == 1) { // interpolation failed (tried to extrapolate)
	  dataout->SetVal(i, j, k, 0);
	  flag1 = 1;
	  extrap->SetVal(i, j, k, 1);
	} else {
	  dataout->SetVal(i, j, k, tarr[0]);
	  extrap->SetVal(i, j, k, 0);
	}
      }
    }
  }

  // For a point for which we tried to extrapolate, set the value of that point to
  // the value of the point which is nearest in (z~, c~) space.
  int dist = 0;
  int distmin = dim2*dim2 + lcgrid*lcgrid;
  double extrapval = 0;
  for (int i = 0; i < dim2; ++i) {
    for (int j = 0; j < dim3; ++j) {
      for (int k = 0; k < lcgrid; ++k) {
	if (extrap->GetVal(i, j, k) == 1) {
	  distmin = dim2*dim2 + lcgrid*lcgrid;
	  extrapval = 0;
	  for (int m = 0; m < dim2; ++m) {
	    for (int n = 0; n < lcgrid; ++n) {
	      if (extrap->GetVal(m, j, n) == 0) {
		dist = (m - i)*(m - i) + (n - k)*(n - k);
		if (dist < distmin) {
		  extrapval = dataout->GetVal(m, j, n);
		  distmin = dist;
		}
	      }
	    }
	  }
	  dataout->SetVal(i, j, k, extrapval);
	}
      }
    }
  }

  delete tmat;
  delete extrap;
  return flag1;
}
