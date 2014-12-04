#ifndef MATRIX4D_H_
#define MATRIX4D_H_

class Matrix4D {
 public:
  Matrix4D(int dim1, int dim2, int dim3, int dim4);
  ~Matrix4D();
  double GetVal(int i, int j, int k, int l) const;
  void SetVal(int i, int j, int k, int l, double val);
  int GetNumDim1() const;
  int GetNumDim2() const;
  int GetNumDim3() const;
  int GetNumDim4() const;
 private:
  double *matrix_;
  const int dim1_;
  const int dim2_;
  const int dim3_;
  const int dim4_;
  
}


#endif // MATRIX4D_H_
