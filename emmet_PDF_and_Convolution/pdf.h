#ifndef PDF_H_
#define PDF_H_
#include <stdio.h>

class PDF {

 public:
  virtual ~PDF() {};
  
  /// Calculates values of a PDF
  //virtual int pdfVal(const double Zmean, const double Zvar, double *pdfRet) = 0;
  virtual int pdfVal(const double Zmean, const double Zvar, double *pdfRet) = 0;

};

#endif // PDF_H_
