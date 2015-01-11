/*! This is the header file endpointslope.h

   See endpointslope.cc for detailed information about determining the
   most monotonic progress variable.
*/
#ifndef ENDPOINTSLOPE_H_
#define ENDPOINTSLOPE_H_

#include <stdio.h>
#include "maxslope.h"

class Matrix;

class EndPointSlope : public MaxSlope {
 public:
  EndPointSlope(const Matrix &progVar);
  ~EndPointSlope();
  int MostMonotonic(int *monoAry, const int ncols, const int col);

 private:
  const int nrows_; // number of rows in progVar matrix
  const int ncols_; // number of cols in progVar matrix
  const Matrix &progVar_; // matrix containing progress variables sorted in increasing order by temperature
  double *slopes_; // array containing the slopes of each progress variable 
};

#endif // ENDPOINTSLOPE_H_
