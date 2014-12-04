#ifndef MATRIX4D_H_
#define MATRIX4D_H_

class Matrix4D {
 public:
  Matrix4(int dim1, int dim2, int dim3);
  ~Matrix4();
  double GetVal(int i, int j, int k, int l) const;
  void SetVal(int i, int j, int k, int l, double vol);
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
