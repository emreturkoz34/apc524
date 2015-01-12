#!/usr/bin/env python

import numpy as np
import unittest

import sys
sys.path.append('../mod')

import maxslope
import matrix

class MaxSlope(unittest.TestCase):

    # Test strictly increasing progress variable case
    def testStrictlyIncreasing(self):
        print "\nTest Monotonicity Checking: Strictly Increasing"
        rows = 5
        cols = 2
        progVar = matrix.Matrix(rows, cols);

        # Set column 0 (Reference column)
        progVar.SetVal(0, 0, 0.0);
        progVar.SetVal(1, 0, 1.0);
        progVar.SetVal(2, 0, 2.0);
        progVar.SetVal(3, 0, 3.0);
        progVar.SetVal(4, 0, 4.0);

        # Set column 1 (progress variable 1)
        progVar.SetVal(0, 1, 5.0);
        progVar.SetVal(1, 1, 10.0);
        progVar.SetVal(2, 1, 15.0);
        progVar.SetVal(3, 1, 20.0);
        progVar.SetVal(4, 1, 25.0);

        checker = monocheck.MonoCheck(progVar) #Create MonoCheck object
        monoAry = np.zeros(cols, dtype=np.int32)
        checker.CheckStrictMonoticity(monoAry, 0)
        self.assertEqual(monoAry[1], 3)

    # Test strictly decreasing progress variable case
    def testStrictlyDecreasing(self):
        print "\nTest Monotonicity Checking: Strictly Decreasing"
        rows = 5
        cols = 2
        progVar = matrix.Matrix(rows, cols);

        # Set column 0 (Reference column)
        progVar.SetVal(0, 0, 0.0);
        progVar.SetVal(1, 0, 1.0);
        progVar.SetVal(2, 0, 2.0);
        progVar.SetVal(3, 0, 3.0);
        progVar.SetVal(4, 0, 4.0);

        # Set column 1 (progress variable 1)
        progVar.SetVal(0, 1, 25.0);
        progVar.SetVal(1, 1, 20.0);
        progVar.SetVal(2, 1, 15.0);
        progVar.SetVal(3, 1, 10.0);
        progVar.SetVal(4, 1, 5.0);

        checker = monocheck.MonoCheck(progVar) #Create MonoCheck object
        monoAry = np.zeros(cols, dtype=np.int32)
        checker.CheckStrictMonoticity(monoAry, 0)
        self.assertEqual(monoAry[1], 3)

    # Test almost strictly increasing progress variable case
    def testAlmostStrictlyIncreasing(self):
        print "\nTest Monotonicity Checking: Almost Strictly Increasing"
        rows = 5
        cols = 2
        progVar = matrix.Matrix(rows, cols);

        # Set column 0 (Reference column)
        progVar.SetVal(0, 0, 0.0);
        progVar.SetVal(1, 0, 1.0);
        progVar.SetVal(2, 0, 2.0);
        progVar.SetVal(3, 0, 3.0);
        progVar.SetVal(4, 0, 4.0);

        # Set column 1 (progress variable 1)
        progVar.SetVal(0, 1, 5.0);
        progVar.SetVal(1, 1, 10.0);
        progVar.SetVal(2, 1, 15.0);
        progVar.SetVal(3, 1, 20.0);
        progVar.SetVal(4, 1, 20.0);

        checker = monocheck.MonoCheck(progVar) #Create MonoCheck object
        monoAry = np.zeros(cols, dtype=np.int32)
        checker.CheckStrictMonoticity(monoAry, 0)
        self.assertEqual(monoAry[1], 0)

    # Test almost strictly decreasing progress variable case
    def testAlmostStrictlyDecreasing(self):
        print "\nTest Monotonicity Checking: Almost Strictly Decreasing"
        rows = 5
        cols = 2
        progVar = matrix.Matrix(rows, cols);

        # Set column 0 (Reference column)
        progVar.SetVal(0, 0, 0.0);
        progVar.SetVal(1, 0, 1.0);
        progVar.SetVal(2, 0, 2.0);
        progVar.SetVal(3, 0, 3.0);
        progVar.SetVal(4, 0, 4.0);

        # Set column 1 (progress variable 1)
        progVar.SetVal(0, 1, 20.0);
        progVar.SetVal(1, 1, 20.0);
        progVar.SetVal(2, 1, 15.0);
        progVar.SetVal(3, 1, 10.0);
        progVar.SetVal(4, 1, 5.0);

        checker = monocheck.MonoCheck(progVar) #Create MonoCheck object
        monoAry = np.zeros(cols, dtype=np.int32)
        checker.CheckStrictMonoticity(monoAry, 0)
        self.assertEqual(monoAry[1], 0)

    # Test constant progress variable case
    def testConstant(self):
        print "\nTest Monotonicity Checking: Constant"
        rows = 5
        cols = 2
        progVar = matrix.Matrix(rows, cols);

        # Set column 0 (Reference column)
        progVar.SetVal(0, 0, 0.0);
        progVar.SetVal(1, 0, 1.0);
        progVar.SetVal(2, 0, 2.0);
        progVar.SetVal(3, 0, 3.0);
        progVar.SetVal(4, 0, 4.0);

        # Set column 1 (progress variable 1)
        progVar.SetVal(0, 1, 0.0);
        progVar.SetVal(1, 1, 0.0);
        progVar.SetVal(2, 1, 0.0);
        progVar.SetVal(3, 1, 0.0);
        progVar.SetVal(4, 1, 0.0);

        checker = monocheck.MonoCheck(progVar) #Create MonoCheck object
        monoAry = np.zeros(cols, dtype=np.int32)
        checker.CheckStrictMonoticity(monoAry, 0)
        self.assertEqual(monoAry[1], 0)

if __name__ == '__main__':
    unittest.main()
