#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <stddef.h>

// PDFs
//#include "deltaPDF.h"
#include "pdf.h"
#include "betaPDF.h"
#include "deltaPDF.h"

// Convolution
#include "convolute.h"

// Integrators
#include "trapz.h"
#include "simpson.h"

// Matrix Classes
#include "matrix.h"
#include "matrix3d.h"
#include "matrix4d.h"

int main(int argc, char *argv[]) {

  //////////////////////////////////////////////////
  /* 
   * Change number of points, PDF used, and/or 
   * integrator
   */
  /////////////////////////////////////////////////

  // Corresponds to number of lines in input files
  const int ZPoints = 11;
  double *Z = new double[ZPoints];
  double *temp = new double[ZPoints];

  // Presumed to be identical to ZPoints
  const int ZmeanPoints = ZPoints;

  /* Points for variance of Z:
   * Delta distro: 1
   * Beta distro: 26
   */
  const int ZvarPoints = 1;

  // Beta PDF or Delta PDF
  PDF *pdf;
  pdf = new DeltaPDF(Z, ZPoints);

  // Integrator: Trapz or Simpson
  Integrator *intgr;
  intgr = new Trapz(Z, ZPoints);

  ///////////////////////////////////////////////////
  /* 
   * Make no more changes to test code below.
   */
  //////////////////////////////////////////////////

  /* Number of variables to filter:
   * reaction rates
   * progress variables
   */
  const int dataSize = 2;


  // Stores PDF data: f(Zvar, Zmean, Z)
  Matrix3D *pdfValuesM = new Matrix3D(ZvarPoints, ZmeanPoints, ZPoints);

  /* Stores convoluted data: f(Zvar, Zmean, Variables)
   * Variables are reaction rates and progress variables
   */
  Matrix *postConvVal[dataSize];
  for (int i = 0; i < dataSize; i++) {
    postConvVal[i] = new Matrix(ZvarPoints, ZmeanPoints);
  }

  // Stores test values for Z: range from 0 to 1
  for (int n = 0; n < ZPoints; n++) {
    Z[n] = double(n) / (ZPoints - 1);
  }

  // Stores test values for Zmean and Zvar
  double *mean = new double [ZPoints];
  for (int n = 0; n < ZPoints; n++) {
    mean[n] = Z[n];
  }
  double *var = new double [ZvarPoints];
  for (int n = 0; n < ZvarPoints; n++) {
    var[n] = 0.01*n;
  }

  // Calculates the PDF
  assert(pdf->pdfVal(mean, var, pdfValuesM) == 0);



  // Initializes instance of Convolution class
  Convolute *conv;
  conv = new Convolute(ZPoints);


  // Testing data
  double *rxnRate = new double[ZPoints];
  double *progVar = new double[ZPoints];
  for (int n = 0; n < ZPoints; n++) {
    rxnRate[n] = double(2*n) * (double(ZPoints) - double(2*n)) 
      / (double(ZPoints) * double(ZPoints) * double(ZPoints));
    progVar[n] = double(2*n) * double(2*n) * double(ZPoints)  
      / (double(ZPoints) * double(ZPoints) * double(ZPoints));
  }

  // Evaluates convolution integral
  assert(conv->convVal(pdfValuesM, rxnRate, progVar, postConvVal, intgr) == 0);



  // Prints out select values
  int j;
  if (ZvarPoints == 1) {
    j = 0;
  } else {
    j = 6;
  }
  int p = 5;
  printf("PDF\n");
  for (int k = 0; k < ZPoints; k++) {
    printf("Z = %f, mean = %f, var = %f, pdf = %f\n", Z[k], mean[p], var[j], pdfValuesM->GetVal(j, p, k));
  }
  printf("\n");
  for (int l = 0; l < dataSize; l++) {
    if (l == 0) {
      printf("Reaction Rates\n");
    } else {
      printf("Progress Variable\n");
    }
    for (int k = 0; k < ZmeanPoints; k++) {
      if (l == 0) {
	printf("Rxn = %f, mean = %f, var = %f\n", rxnRate[k], mean[k], var[j]);
      } else {
	printf("ProgVar = %f, mean = %f, var = %f\n", progVar[k], mean[k], var[j]);
      }
    }
    if (l == 0) {
      printf("Convoluted Reaction Rate = %f\n", postConvVal[l]->GetVal(j, p));
    } else {
      printf("Convoluted Progress Variable = %f\n", postConvVal[l]->GetVal(j, p));
    }
    printf("\n");
  }

  return 0;
}
