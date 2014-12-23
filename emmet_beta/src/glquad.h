#ifndef GLQuad_H_
#define GLQuad_H_

#include "integrator.h"
#include "alglibinternal.h"
#include "alglibmisc.h"
#include "ap.h"
#include "dataanalysis.h"
#include "diffequations.h"
#include "fasttransforms.h"
#include "integration.h"
#include "interpolation.h"
#include "linalg.h"
#include "optimization.h"
#include "solvers.h"
#include "specialfunctions.h"
#include "statistics.h"

class GLQuad : public Integrator {
 public:
  GLQuad(int Nodes);
  ~GLQuad();
  double integrate(double *integrand, double *Z, int ZPoints);

 private:
  int Nodes_;
  double *x_;
  double *w_;
};

#endif // GLQuad_H_
