/* This is the header file simplelnm.h

   See simplelnm.cc for detailed information about determining the
   least non-monotonic progress variable.
 */
#ifndef SIMPLELNM_H_
#define SIMPLELNM_H_

#include <stdio.h>
#include "leastnonmono.h"

class Matrix;

class SimpleLNM : public LeastNonMono {
 public:
  SimpleLNM(const Matrix &progVar);
  ~SimpleLNM();
  int LeastNonMonotonic(int *monoAry, const int ncols, const int col);

 private:
  const int nrows_; // number of rows in progVar matrix
  const int ncols_; // number of cols in progVar matrix
  const Matrix &progVar_; // matrix containing progress variables sorted in increasing order by temperature
  double *increasing_; // array containing the amount each progress variable is increasing
  double *decreasing_; // array containing the amount each progress variable is decreasing
};

#endif // SIMPLELNM_H_
