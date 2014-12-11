#ifndef INTEGRATOR_H_
#define INTEGRATOR_H_
#include <stdio.h>

#include "vector.h"

class Integrator {

 public:
  virtual ~Integrator() {};
  
  virtual double integrate(Vector *integrand) = 0;

};

#endif // INTEGRATOR_H_
