#!/usr/bin/env python

import numpy as np
import unittest

import sys
sys.path.append('../mod')

import maxslope
import matrix

class MaxSlope(unittest.TestCase):

    # Test most monotonic progress variable
    def testEndPointSlope1(self):
        print "\nTest MaxSlope Checking: EndPointSlope Monotonic and Largest Slope"
        rows = 5
        cols = 4
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

        # Set column 2 (progress variable 2)
        progVar.SetVal(0, 2, 5.0);
        progVar.SetVal(1, 2, 10.0);
        progVar.SetVal(2, 2, 20.0);
        progVar.SetVal(3, 2, 30.0);
        progVar.SetVal(4, 2, 50.0);

        # Set column 3 (progress variable 3)
        progVar.SetVal(0, 3, 5.0);
        progVar.SetVal(1, 3, 10.0);
        progVar.SetVal(2, 3, 15.0);
        progVar.SetVal(3, 3, 10.0);
        progVar.SetVal(4, 3, 2.0);

        maxchecker = maxslope.EndPointSlope(progVar) # Create EndPointSlope object
        monoAry = np.zeros(cols, dtype=np.int32)
        for j in range(cols):
            monoAry[j] = 3;
        monoAry[3] = 0; # Last progress variable isn't monotonic
        maxchecker.MostMonotonic(monoAry, 0)
        self.assertEqual(monoAry[2], 3)

    # Test monotonic progress variable without largest slope
    def testEndPointSlope2(self):
        print "\nTest MaxSlope Checking: EndPointSlope Monotonic Without Largest Slope"
        rows = 5
        cols = 4
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

        # Set column 2 (progress variable 2)
        progVar.SetVal(0, 2, 5.0);
        progVar.SetVal(1, 2, 10.0);
        progVar.SetVal(2, 2, 20.0);
        progVar.SetVal(3, 2, 30.0);
        progVar.SetVal(4, 2, 50.0);

        # Set column 3 (progress variable 3)
        progVar.SetVal(0, 3, 5.0);
        progVar.SetVal(1, 3, 10.0);
        progVar.SetVal(2, 3, 15.0);
        progVar.SetVal(3, 3, 10.0);
        progVar.SetVal(4, 3, 2.0);

        maxchecker = maxslope.EndPointSlope(progVar) # Create EndPointSlope object
        monoAry = np.zeros(cols, dtype=np.int32)
        for j in range(cols):
            monoAry[j] = 3;
        monoAry[3] = 0; # Last progress variable isn't monotonic
        maxchecker.MostMonotonic(monoAry, 0)
        self.assertEqual(monoAry[1], 2)

    # Test non-monotonic progress variable
    def testEndPointSlope3(self):
        print "\nTest MaxSlope Checking: EndPointSlope Non-Monotonic"
        rows = 5
        cols = 4
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

        # Set column 2 (progress variable 2)
        progVar.SetVal(0, 2, 5.0);
        progVar.SetVal(1, 2, 10.0);
        progVar.SetVal(2, 2, 20.0);
        progVar.SetVal(3, 2, 30.0);
        progVar.SetVal(4, 2, 50.0);

        # Set column 3 (progress variable 3)
        progVar.SetVal(0, 3, 5.0);
        progVar.SetVal(1, 3, 10.0);
        progVar.SetVal(2, 3, 15.0);
        progVar.SetVal(3, 3, 10.0);
        progVar.SetVal(4, 3, 2.0);

        maxchecker = maxslope.EndPointSlope(progVar) # Create EndPointSlope object
        monoAry = np.zeros(cols, dtype=np.int32)
        for j in range(cols):
            monoAry[j] = 3;
        monoAry[3] = 0; # Last progress variable isn't monotonic
        maxchecker.MostMonotonic(monoAry, 0)
        self.assertEqual(monoAry[3], 0)

    # Test most monotonic progress variable
    def testLinRegression1(self):
        print "\nTest MaxSlope Checking: LinRegression Monotonic and Largest Slope"
        rows = 5
        cols = 4
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

        # Set column 2 (progress variable 2)
        progVar.SetVal(0, 2, 5.0);
        progVar.SetVal(1, 2, 10.0);
        progVar.SetVal(2, 2, 20.0);
        progVar.SetVal(3, 2, 30.0);
        progVar.SetVal(4, 2, 50.0);

        # Set column 3 (progress variable 3)
        progVar.SetVal(0, 3, 5.0);
        progVar.SetVal(1, 3, 10.0);
        progVar.SetVal(2, 3, 15.0);
        progVar.SetVal(3, 3, 10.0);
        progVar.SetVal(4, 3, 2.0);

        maxchecker = maxslope.LinRegression(progVar) # Create LinRegression object
        monoAry = np.zeros(cols, dtype=np.int32)
        for j in range(cols):
            monoAry[j] = 3;
        monoAry[3] = 0; # Last progress variable isn't monotonic
        maxchecker.MostMonotonic(monoAry, 0)
        self.assertEqual(monoAry[2], 3)

    # Test monotonic progress variable without largest slope
    def testLinRegression2(self):
        print "\nTest MaxSlope Checking: LinRegression Monotonic Without Largest Slope"
        rows = 5
        cols = 4
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

        # Set column 2 (progress variable 2)
        progVar.SetVal(0, 2, 5.0);
        progVar.SetVal(1, 2, 10.0);
        progVar.SetVal(2, 2, 20.0);
        progVar.SetVal(3, 2, 30.0);
        progVar.SetVal(4, 2, 50.0);

        # Set column 3 (progress variable 3)
        progVar.SetVal(0, 3, 5.0);
        progVar.SetVal(1, 3, 10.0);
        progVar.SetVal(2, 3, 15.0);
        progVar.SetVal(3, 3, 10.0);
        progVar.SetVal(4, 3, 2.0);

        maxchecker = maxslope.LinRegression(progVar) # Create LinRegression object
        monoAry = np.zeros(cols, dtype=np.int32)
        for j in range(cols):
            monoAry[j] = 3;
        monoAry[3] = 0; # Last progress variable isn't monotonic
        maxchecker.MostMonotonic(monoAry, 0)
        self.assertEqual(monoAry[1], 2)

    # Test non-monotonic progress variable
    def testLinRegression3(self):
        print "\nTest MaxSlope Checking: LinRegression Non-Monotonic"
        rows = 5
        cols = 4
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

        # Set column 2 (progress variable 2)
        progVar.SetVal(0, 2, 5.0);
        progVar.SetVal(1, 2, 10.0);
        progVar.SetVal(2, 2, 20.0);
        progVar.SetVal(3, 2, 30.0);
        progVar.SetVal(4, 2, 50.0);

        # Set column 3 (progress variable 3)
        progVar.SetVal(0, 3, 5.0);
        progVar.SetVal(1, 3, 10.0);
        progVar.SetVal(2, 3, 15.0);
        progVar.SetVal(3, 3, 10.0);
        progVar.SetVal(4, 3, 2.0);

        maxchecker = maxslope.LinRegression(progVar) # Create LinRegression object
        monoAry = np.zeros(cols, dtype=np.int32)
        for j in range(cols):
            monoAry[j] = 3;
        monoAry[3] = 0; # Last progress variable isn't monotonic
        maxchecker.MostMonotonic(monoAry, 0)
        self.assertEqual(monoAry[3], 0)

if __name__ == '__main__':
    unittest.main()
