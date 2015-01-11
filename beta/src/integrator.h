#ifndef INTEGRATOR_H_
#define INTEGRATOR_H_

class Integrator {
 public:
  virtual ~Integrator() {};
  /// Virtual function to be inherited by each integration algorithm to integrate the given data set
  virtual double integrate(const double *integrand, const double *Z, const int ZPoints) = 0;
};

#endif // INTEGRATOR_H_
