#ifndef INTEGRATOR_H_
#define INTEGRATOR_H_

class Integrator {
 public:
  virtual ~Integrator() {};
  virtual double integrate(double *integrand, double *Z, int ZPoints) = 0;
};

#endif // INTEGRATOR_H_
