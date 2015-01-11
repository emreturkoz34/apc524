#include "hermiteinterp.h"
using namespace alglib;

// Constructor
HermiteInterp::HermiteInterp() {}

// Destructor
HermiteInterp::~HermiteInterp() {}

// Hermite spline interpolation function
int HermiteInterp::Interp(const Matrix *matin, int col, double ival, double *vecout, int cols) {

  // Initialize 1d arrays to store x points, y points, and dy/dx at points
  int n = matin->GetNumRows();
  real_1d_array d, x, y;
  d.setlength(n);
  x.setlength(n);
  y.setlength(n);

  spline1dinterpolant s; // spline structure

  if (ival < matin->GetVal(0, col) || ival > matin->GetVal(n-1, col)) {
    return 1; // tried to extrapolate
  }

  for (int i = 0; i < n; ++i) {
    x[i] = matin->GetVal(i, col);
  }

  for (int k = 0; k < cols; ++k) {
    if (k == col) { // current column is independent variable
      vecout[k] = ival;
    } else { // current column is dependent variable
      // Update y values
      for (int i = 0; i < n; ++i) {
	y[i] = matin->GetVal(i, k);
      }
      
      // Numerically calculate derivative at each point
      for (int i = 1; i < n-1; ++i) {
	d[i] = 0.5*((y[i+1] - y[i])/(x[i+1] - x[i]) + (y[i] - y[i-1])/(x[i] - x[i-1]));
      }
      d[0] = (y[1] - y[0])/(x[1] - x[0]);
      d[n-1] = (y[n-1] - y[n-2])/(x[n-1] - x[n-2]);

      // Build spline structure
      spline1dbuildhermite(x, y, d, s);

      // Evaluate spline at point of interest
      vecout[k] = spline1dcalc(s, ival);
    }
  }

  return 0; // success
}
