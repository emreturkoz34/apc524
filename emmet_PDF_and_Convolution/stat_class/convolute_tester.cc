#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include "deltaPDF.h"
#include "betaPDF.h"
#include "convolute.h"
#include "trapz.h"
#include "simpson.h"
#include <stddef.h>

int main(int argc, char *argv[]) {

  const int nPoints = 101;
  double *Z = new double[nPoints];
  double *pdfValues = new double[nPoints];

  /* NOTE: Z here is the Z from the flamelet solutions
   * 
   * This Z should be the same for all files. Here it is taken to be
   * linear, ranging from 0 to 1, as outputted by FlameMaster.
   */
  for (int n = 0; n < nPoints; n++) {
    Z[n] = double(n) / (nPoints - 1);
    printf("Z[%d] = %f\n", n, Z[n]);
  }

  /* NOTE: Can use DeltaPDF or BetaPDF here.
   *
   * Still need to implement MostProbPDF
   */
  PDF *pdf;
  pdf = new BetaPDF(Z, nPoints);

  /* NOTE: pdf->pdfVal(Zmean, Zvar, pdfValues) 
   * 
   * Zmean and Zvar will be specified by input and will be a set of
   * values.
   *
   * This will be done for every Zmean and every Zvar.
  */
  assert(pdf->pdfVal(0.1, 0.1, pdfValues) == 0);

  // This is just for testing.
  for (int i = 0; i < nPoints; i++) {
    printf("pdfValues[%d] = %f\n", i, pdfValues[i]);
  }

  /* NOTE: Currently only 1 convolution will be performed, hence
   * convValues is an array of length 1. Ultimately, it will need to
   * be an array of length(Zmean) * length(Zvar) per file!!!
   */
  Convolute *conv;
  conv = new Convolute(nPoints);
  double *convValues = new double[1];

  /* NOTE: Currently only Trapezoid Method.
   *
   * Still need to implement Simpson's Rule and Gaussian Quadrature.
   */
  Integrator *intgr = new Trapz(Z, nPoints);
  //  intgr = new Trapz(Z, nPoints);


  /* NOTE: omega will be the source term from the files.
   */
  double *omega = new double[nPoints];
  for (int n = 0; n < nPoints; n++) {
    omega[n] = double(n) * (double(nPoints) - double(n));
    //omega[n] = 1;
    printf("omega[%d] = %f\n", n, omega[n]);
  }

  /* Performs the convolution integral
   *
   * NOTE: This will need to be a loop over all sets of pdfValues (one
   * set per Zmean, Zvar pair).
   *
   * Each iteration returns a scalar to convValues which represents a
   * filtered omega at Zmean and Zvar. Later, these filtered omega
   * values will be interpolated at a fixed Zmean and Zvar
   * (i.e. interpolate between results from different files) to get
   * the filtered omega at every pre-specified Cmean.
   */
  assert(conv->convVal(pdfValues, omega, convValues, intgr) == 0);

  printf("convValues = %f\n", *convValues);

  return 0;
}
