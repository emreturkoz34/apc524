#ifndef MATRIX_H_
#define MATRIX_H_

class Matrix {
 public:
  Matrix(int rows, int cols);
  ~Matrix();
  double GetVal(int i, int j);
  void SetVal(int i, int j, double val);
  int GetNumRows();
  int GetNumCols();
  double* GetCol(int j);

 private:
  double *matrix_;
  int nrows_;
  int ncols_;
}

#endif // MATRIX_H_
