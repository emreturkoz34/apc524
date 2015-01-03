%module integrator
%{
#define SWIG_FILE_WITH_INIT
#include "integrator.h"
#include "trapz.h"
#include "simpson.h"
#include "glquad.h"
%}

%include "integrator.h"
%include "trapz.h"
%include "simpson.h"
%include "glquad.h"

// Will only be used for Python testing
%include "numpy.i"
%init %{
  import_array();
%}

%apply (double *IN_ARRAY1, int DIM1) {(const double *integrand, 
				        const int iPoints),(const double *Z, const int ZPoints)}

%inline %{
  double trapz(const double *integrand, const int iPoints, 
			  const double *Z, const int ZPoints) {
    double temp;
    Integrator *intgr = new Trapz();
    temp = intgr->integrate(integrand, Z, ZPoints);
    delete intgr;
    return temp;
  }

  double simpson(const double *integrand, const int iPoints, 
			  const double *Z, const int ZPoints) {
    double temp;
    Integrator *intgr = new Simpson();
    temp = intgr->integrate(integrand, Z, ZPoints);
    delete intgr;
    return temp;
  }

  double glquad(const double *integrand, const int iPoints, 
		const double *Z, const int ZPoints, const int Nodes) {
    double temp;
    Integrator *intgr = new GLQuad(Nodes);
    temp = intgr->integrate(integrand, Z, ZPoints);
    delete intgr;
    return temp;
  }
%}
