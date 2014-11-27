/* monocheck is a program which checks whether a specified progress variable is monotonically increasing with respect to temperature. That is, C(T1)<=C(T2) for T1<=T2, where T1 and T2 are any two temperatures and C is the progress variable.

It takes input arguments in the following format:

monocheck < 
*/
#include <assert.h>
#include "monocheck.h"

/// Constructor
MonoCheck::MonoCheck(const Matrix &progVar)
  : nrows_(progVar.GetNumRows()),
    ncols_(progVar.GetNumCols()),
    progVar_(progVar)
{}

/// Destructor
MonoCheck::~MonoCheck()
{}

/// CheckIncreasing investigates which columns of progVar are monotonically increasing. monoAry must be an array of length ncols_. Every cell in monoAry (except the first) represents the monotonicity of a progress variable (C). Each cell holds a value of 3 if C is monotonic and 0 otherwise.
int MonoCheck::CheckIncreasing(double *monoAry){
  for (int j=0; j<ncols_; ++j){

  }
}
