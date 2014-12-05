#ifndef LININTERP_H_
#define LININTERP_H_

#include "interpolator.h"

class LinInterp : public Interpolator {
	public: 
		LinInterp();
		~LinInterp();
		int Interp(const Matrix *matin, int col, double ival, double *vecout);
};

#endif // LININTERP_H_
