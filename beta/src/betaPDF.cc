#include "betaPDF.h"
#include "math.h"
#include "assert.h"

/// Constructor
BetaPDF::BetaPDF(const double *Zmean, const int ZmeanPoints, const double *Zvar, const int ZvarPoints)
  : Zmean_(Zmean),
    ZmeanPoints_(ZmeanPoints),
    Zvar_(Zvar),
    ZvarPoints_(ZvarPoints) {
}

/// Destructor
BetaPDF::~BetaPDF() {
}


/// Main routine that generates the PDF values
/*!  The Beta PDF uses statistics (means and variances) to generate a
  PDF. The PDF values are stored in a Matrix3D object: dim1 is the
  variance, dim2 is the mean, and dim3 are the data points.

  \verbatim

  INPUTS: 
  const double* Z        double array containing mixture fraction values coming from the files

  const int ZPoints      number of mixture fraction values in the Z array

  Matrix3D* pdfValM      the Matrix3D type container that stores the PDF values

  
  OUTPUT:

  int                    flag specifying whether or not the function succeeded
                          = 0: success
			 != 0: something went wrong

  \endverbatim

*/
int BetaPDF::pdfVal(const double *Z, const int ZPoints, Matrix3D *pdfValM) {

  // Check dimensions of output matrix match dimensions of input arrays
  assert(pdfValM->GetNumDim1() == ZvarPoints_);
  assert(pdfValM->GetNumDim2() == ZmeanPoints_);
  assert(pdfValM->GetNumDim3() == ZPoints);

  double *temp = new double[ZPoints];
  double ZvarVal, ZmeanVal, Weight;
  double alpha, beta, factor;
  double lnpdf;

  int i;
  for (int n = 0; n < ZvarPoints_; n++) {
    ZvarVal  = Zvar_[n];

    for (int m = 0; m < ZmeanPoints_; m++) {
      ZmeanVal = Zmean_[m];

      Weight = double(ZPoints) - 1;

      // resets points to 0
      for (int k = 0; k < ZPoints; k++) {
	temp[k] = 0;
      }  

      // check for Min or Max mean
      if (ZmeanVal == 1) {
	temp[ZPoints-1] = Weight * 1;
      } else if (ZmeanVal == 0) {
	temp[0] = Weight * 1;

	// Delta PDF for zero variance
      } else if (ZvarVal == 0) {
	i = 0;
	while (Z[i] < ZmeanVal) {
	  i = i+1;
	}
	temp[i-1] = Weight * (Z[i]  - ZmeanVal)  / (Z[i] - Z[i-1]);
	temp[i]   = Weight * (ZmeanVal - Z[i-1]) / (Z[i] - Z[i-1]);

	// Impossible cases: becomes double delta PDF
      } else if (ZvarVal >= ZmeanVal*(1-ZmeanVal)) {
	temp[0] = Weight * (1-ZmeanVal);
	temp[ZPoints-1] = Weight * ZmeanVal;

	// BetaPDF
      } else {

	alpha = ZmeanVal * (ZmeanVal * (1 - ZmeanVal) / ZvarVal - 1);
	beta = alpha / ZmeanVal - alpha;
	factor = lgamma(alpha + beta) - lgamma(alpha) - lgamma(beta);

	// Middle points: 0 < n < ZPoints-1
	for (int n = 1; n < ZPoints-1; n++) {
	  lnpdf = factor + (alpha - 1) * log(Z[n]) + (beta - 1) * log(1 - Z[n]);
	  temp[n] = exp(lnpdf);
	}

	// End points
	temp[0] = temp[1];
	temp[ZPoints-1] = temp[ZPoints-2];

	for (int k = 0; k < ZPoints; k++) {
	  temp[k] = temp[k];
	}
      }

      // Set PDF to output
      for (int k = 0; k < ZPoints; k++) {
	pdfValM->SetVal(n, m, k, temp[k]);
      }
    }
  }

  delete temp;
  return 0;
}
