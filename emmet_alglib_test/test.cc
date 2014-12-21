#include "alglibinternal.h"
#include "alglibmisc.h"
#include "ap.h"
#include "dataanalysis.h"
#include "fasttransforms.h"
#include "integration.h"
#include "interpolation.h"
#include "linalg.h"
#include "optimization.h"
#include "solvers.h"
#include "specialfunctions.h"
#include "statistics.h"
#include "stdafx.h"
#include "stdio.h"
#include "assert.h"

using namespace alglib;

int main() {

  ae_int_t n = 3;
  ae_int_t info;
  real_1d_array x;
  real_1d_array w;

  gqgenerategausslegendre(n, info, x, w);

  printf("i = 0, x = %f, w = %f\n", x[0], w[0]);
  printf("i = 1, x = %f, w = %f\n", x[1], w[1]);
  printf("i = 2, x = %f, w = %f\n", x[2], w[2]);

  printf("Integration test\n");

  double *f = new double(n-1);
  for (int i = 0; i < n; i++) {
    f[i] = x[i]*x[i];
  }
  // calculate integral
  double intgrl = 0;
  for (int i = 0; i < n; i++) {
    intgrl = intgrl + f[i]*w[i];
  }
  printf("intgrl = %f\n", intgrl);
  return 0;
}
