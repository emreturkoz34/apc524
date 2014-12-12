import matrix
import bubble_sort

import numpy as np


mat = matrix.Matrix(9,2)


mat.SetVal(0,0, 5.0)
mat.SetVal(1,0, 15.0)
mat.SetVal(2,0, 25.0)
mat.SetVal(3,0, 35.0)
mat.SetVal(4,0, 30.0)
mat.SetVal(5,0, 10.0)
mat.SetVal(6,0, 20.0)
mat.SetVal(7,0, 40.0)
mat.SetVal(8,0, 45.0)

mat.SetVal(0,1, 1.0)
mat.SetVal(1,1, 2.0)
mat.SetVal(2,1, 3.0)
mat.SetVal(3,1, 4.0)
mat.SetVal(4,1, 5.0)
mat.SetVal(5,1, 6.0)
mat.SetVal(6,1, 7.0)
mat.SetVal(7,1, 8.0)
mat.SetVal(8,1, 9.0)


sorter = bubble_sort.bubble_sort(mat)

sorter.SetRefColNum(0)
sorter.SetSortEndIndex(8);
sorter.SetSortStartIndex(0);
sorter.generateIndexArray();
sorter.extractRefCol();

sorter.sort_data()


for i in range (0,8):
    print mat.GetVal(i,0)
