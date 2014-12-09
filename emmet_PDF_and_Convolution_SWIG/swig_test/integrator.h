#ifndef INTEGRATOR_H_
#define INTEGRATOR_H_
#include <stdio.h>

class Integrator {

 public:
  virtual ~Integrator() {};
  
  virtual double integrate(const double *integrand) = 0;

};

#endif // INTEGRATOR_H_
