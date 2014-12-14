#ifndef TRAPZ_H_
#define TRAPZ_H_

#include "integrator.h"
#include "vector.h"

class Trapz : public Integrator {
 public:
  Trapz(Vector *Z, const int nPoints);
  ~Trapz();
  double integrate(Vector *integrand);

 private:
  const int nPoints_;
  Vector *Z_;
};

#endif // TRAPZ_H_
