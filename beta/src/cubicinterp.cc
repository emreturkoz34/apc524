#include "cubicinterp.h"

/// Constructor
CubicInterp::CubicInterp() {}

/// Destructor
CubicInterp::~CubicInterp() {}

/// Cubic spline interpolation function
/*!
  This function takes in a 2D matrix of data and interpolates an entire row from it using
  a cubic spline interpolator. Each column of the matrix is treated as a variable, with a 
  specified column being the independent variable. The input data is assumed to be sorted
  by the independent variable.


  \verbatim
  INPUTS:

  const Matrix *matin    pointer to a Matrix object. This is the input data.

  int col                integer specifying which column of the input Matrix is the independent
                         variable

  double ival            value at which to interpolate

  double *vecout         pointer to an array which contains the interpolated row. This array has
                         the same number of columns as the input Matrix.

  int cols               number of columns of matin/vecout

  OUTPUTS:

  int                    flag specifying whether or not the function succeeded
                         = 0: success
			 = 1: extrapolation attempted
  \endverbatim

*/
int CubicInterp::Interp(const Matrix *matin, int col, double ival, double *vecout, int cols) {

   // Allocate memory necessary for calculations
   int n = matin->GetNumRows();
   if (ival < matin->GetVal(0, col) || ival > matin->GetVal(n-1, col)) {
      return 1; // tried to extrapolate
   }
   double *h = new double [n-1];
   double *p = new double [n-1];
   double *u = new double [n-1];
   double *v = new double [n-1];
   double *z = new double [n];
   double *a = new double [n-1];
   double *b = new double [n-1];
   double *c = new double [n-1];
   double *d = new double [n-1];

   for (int k = 0; k < cols; ++k) {
      if (k == col) { // current column is independent variable
	 vecout[k] = ival;
      } else { // current column is dependent variable
         // Compute h and p
	 for (int i = 0; i < n-1; ++i) {
	    h[i] = matin->GetVal(i+1, col) - matin->GetVal(i, col);
	    p[i] = (matin->GetVal(i+1, k) - matin->GetVal(i, k))/h[i];
	 }

         // Gaussian elimination
	 u[1] = 2*(h[0] + h[1]);
	 v[1] = 6*(p[1] - p[0]);
	 for (int i = 2; i < n-1; ++i) {
	    u[i] = 2*(h[i-1] + h[i]) - h[i-1]*h[i-1]/u[i-1];
	    v[i] = 6*(p[i] - p[i-1]) - h[i-1]*v[i-1]/u[i-1];
	 }
	 
         // Back substitution
	 z[n-1] = 0;
	 for (int i = n-2; i > 0; --i) { 
	    z[i] = (v[i] - h[i]*z[i+1])/u[i];
	 }
	 z[0] = 0;
	 
         // Store coefficients
	 for (int i = 0; i < n-1; ++i) {
	    a[i] = matin->GetVal(i, k);
	    b[i] = -h[i]*z[i+1]/6 - h[i]*z[i]/3 + (matin->GetVal(i+1, k) - matin->GetVal(i, k))/h[i];
	    c[i] = z[i]/2;
	    d[i] = (z[i+1] - z[i])/(6*h[i]);
	 }
	 
         // Evaluate interpolated polynomial at interpolation point
	 int i;
	 for (i = 0; i < n-1; ++i) {
	    if (ival <= matin->GetVal(i+1, col)) {
	       break;
	    }
	 }
	 vecout[k] = a[i] + (ival - matin->GetVal(i, col))*(b[i] + 
		    (ival - matin->GetVal(i, col))*(c[i] + (ival - matin->GetVal(i, col))*d[i]));
	 
      }
   }
   
   // Free memory
   delete[] h;
   delete[] p;
   delete[] u;
   delete[] v;
   delete[] z;
   delete[] a;
   delete[] b;
   delete[] c;
   delete[] d;
   
   return 0; // success
}
