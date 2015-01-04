/* LeastNonMono is an abstract class which provides the framework to
   determine the least non-monotonic progress variable.
 */
#ifndef LEASTNONMONO_H_
#define LEASTNONMONO_H_

class Matrix;

class LeastNonMono {
 public:
  virtual ~LeastNonMono() {}
  virtual int LeastNonMonotonic(int *monoAry, const int ncols, const int col) = 0;
};

#endif // LEASTNONMONO_H_
