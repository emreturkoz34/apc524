/* MaxSlope is an abstract class which provides the framework to
   determine the most monotonic progress variable.
 */
#ifndef MAXSLOPE_H_
#define MAXSLOPE_H_

class Matrix;

class MaxSlope {
 public:
  virtual ~MaxSlope() {}

  virtual int MostMonotonic(const int col, int *monoAry) = 0;
};

#endif // MAXSLOPE_H_
