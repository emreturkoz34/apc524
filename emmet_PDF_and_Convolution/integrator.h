#ifndef INTEGRATOR_H_
#define INTEGRATOR_H_
#include <stdio.h>

class Integrator {

 public:
  virtual ~Integrator() {};
  
  virtual int integrate(const double *integrand, double *convRet) = 0;

};

#endif // INTEGRATOR_H_
