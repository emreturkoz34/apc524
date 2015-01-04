/* This is the header file linregression.h
   
   See linregression.cc for detailed information about determining the
   most monotonic progress variable.
 */
#ifndef LINREGRESSION_H_
#define LINREGRESSION_H_

#include <stdio.h>
#include <vector>

#include "vector.h"
#include "maxslope.h"
class Matrix;

class LinRegression : public MaxSlope {
 public:
  LinRegression(const Matrix &progVar);
  ~LinRegression();
  int MostMonotonic(const int col, Vector *monoAry);
  //int MostMonotonic(const int col, int *monoAry);

 private:
  const int nrows_; // number of rows in progVar matrix
  const int ncols_; // number of cols in progVar matrix
  const Matrix &progVar_; // matrix containing progress variables sorted in increasing order by temperature
  double *slopes_; // array containing the slopes of each progress variable 
};

#endif // LINREGRESSION_H_
