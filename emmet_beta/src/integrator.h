#ifndef INTEGRATOR_H_
#define INTEGRATOR_H_
#include <stdio.h>

class Integrator {

 public:
  virtual ~Integrator() {};
  
  virtual double integrate(double *integrand, double *Z, int ZPoints) = 0;

};

#endif // INTEGRATOR_H_
