#ifndef INTERPOLATOR_H_
#define INTERPOLATOR_H_

#include "matrix.h"

class Interpolator {
	public: 
		virtual ~Interpolator() {}
		virtual int Interp(const Matrix *matin, int col, double ival, double *vecout, int cols) = 0;
};

#endif // INTERPOLATOR_H_
