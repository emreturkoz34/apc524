/* This is the header file advancedlnm.h

   See advancedlnm.cc for detailed information about determining the
   least non-monotonic progress variable.
 */
#ifndef ADVANCEDLNM_H_
#define ADVANCEDLNM_H_

#include <stdio.h>
#include "leastnonmono.h"

class Matrix;

class AdvancedLNM : public LeastNonMono {
 public:
  AdvancedLNM(const Matrix &progVar);
  ~AdvancedLNM();
  int LeastNonMonotonic(int *monoAry, const int ncols, const int col);

 private:
  const int nrows_; // number of rows in progVar matrix
  const int ncols_; // number of cols in progVar matrix
  const Matrix &progVar_; // matrix containing progress variables sorted in increasing order by temperature
  double *increasing_; // array containing the amount each progress variable is increasing
  double *decreasing_; // array containing the amount each progress variable is decreasing
};

#endif // ADVANCEDLNM_H_
