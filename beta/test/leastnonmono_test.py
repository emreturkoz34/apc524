#!/usr/bin/env python

import numpy as np
import unittest

import sys
sys.path.append('../mod')

import leastnonmono
import matrix

class LeastNonMono(unittest.TestCase):

    # Test least non-monotonic progress variable
    def testSimpleLNM1(self):
        print "\nTest LeastNonMono Checking: SimpleLNM Least Non-Monotonic"
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
        progVar.SetVal(1, 1, 4.0);
        progVar.SetVal(2, 1, 2.0);
        progVar.SetVal(3, 1, 3.0);
        progVar.SetVal(4, 1, 5.0);

        # Set column 2 (progress variable 2)
        progVar.SetVal(0, 2, 1.0);
        progVar.SetVal(1, 2, 2.0);
        progVar.SetVal(2, 2, 5.0);
        progVar.SetVal(3, 2, 4.0);
        progVar.SetVal(4, 2, 3.0);

        # Set column 3 (progress variable 3)
        progVar.SetVal(0, 3, 1.0);
        progVar.SetVal(1, 3, 7.0);
        progVar.SetVal(2, 3, 9.0);
        progVar.SetVal(3, 3, 11.0);
        progVar.SetVal(4, 3, 8.0);

        lnmchecker = leastnonmono.SimpleLNM(progVar) # Create SimpleLNM object
        monoAry = np.zeros(cols, dtype=np.int32)
        lnmchecker.LeastNonMonotonic(monoAry, 0)
        self.assertEqual(monoAry[3], 1)

    # Test non-monotonic progress variable
    def testSimpleLNM2(self):
        print "\nTest LeastNonMono Checking: SimpleLNM Non-Monotonic"
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
        progVar.SetVal(1, 1, 4.0);
        progVar.SetVal(2, 1, 2.0);
        progVar.SetVal(3, 1, 3.0);
        progVar.SetVal(4, 1, 5.0);

        # Set column 2 (progress variable 2)
        progVar.SetVal(0, 2, 1.0);
        progVar.SetVal(1, 2, 2.0);
        progVar.SetVal(2, 2, 3.0);
        progVar.SetVal(3, 2, 4.0);
        progVar.SetVal(4, 2, 3.0);

        # Set column 3 (progress variable 3)
        progVar.SetVal(0, 3, 1.0);
        progVar.SetVal(1, 3, 7.0);
        progVar.SetVal(2, 3, 9.0);
        progVar.SetVal(3, 3, 11.0);
        progVar.SetVal(4, 3, 8.0);

        lnmchecker = leastnonmono.SimpleLNM(progVar) # Create SimpleLNM object
        monoAry = np.zeros(cols, dtype=np.int32)
        lnmchecker.LeastNonMonotonic(monoAry, 0)
        self.assertEqual(monoAry[1], 0)

    # Test non-monotonic progress variables with same percentages
    def testSimpleLNM3(self):
        print "\nTest LeastNonMono Checking: SimpleLNM Non-Monotonic Same Percentages"
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
        progVar.SetVal(1, 1, 4.0);
        progVar.SetVal(2, 1, 2.0);
        progVar.SetVal(3, 1, 3.0);
        progVar.SetVal(4, 1, 5.0);

        # Set column 2 (progress variable 2)
        progVar.SetVal(0, 2, 1.0);
        progVar.SetVal(1, 2, 2.0);
        progVar.SetVal(2, 2, 3.0);
        progVar.SetVal(3, 2, 4.0);
        progVar.SetVal(4, 2, 3.0);

        # Set column 3 (progress variable 3)
        progVar.SetVal(0, 3, 1.0);
        progVar.SetVal(1, 3, 7.0);
        progVar.SetVal(2, 3, 9.0);
        progVar.SetVal(3, 3, 11.0);
        progVar.SetVal(4, 3, 8.0);

        lnmchecker = leastnonmono.SimpleLNM(progVar) # Create SimpleLNM object
        monoAry = np.zeros(cols, dtype=np.int32)
        lnmchecker.LeastNonMonotonic(monoAry, 0)
        self.assertEqual(monoAry[3], 1)

    # Test least non-monotonic progress variable
    def testAdvancedLNM1(self):
        print "\nTest LeastNonMono Checking: AdvancedLNM Least Non-Monotonic"
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
        progVar.SetVal(1, 1, 4.0);
        progVar.SetVal(2, 1, 2.0);
        progVar.SetVal(3, 1, 3.0);
        progVar.SetVal(4, 1, 5.0);

        # Set column 2 (progress variable 2)
        progVar.SetVal(0, 2, 1.0);
        progVar.SetVal(1, 2, 2.0);
        progVar.SetVal(2, 2, 5.0);
        progVar.SetVal(3, 2, 4.0);
        progVar.SetVal(4, 2, 3.0);

        # Set column 3 (progress variable 3)
        progVar.SetVal(0, 3, 1.0);
        progVar.SetVal(1, 3, 7.0);
        progVar.SetVal(2, 3, 9.0);
        progVar.SetVal(3, 3, 11.0);
        progVar.SetVal(4, 3, 8.0);

        lnmchecker = leastnonmono.AdvancedLNM(progVar) # Create AdvancedLNM object
        monoAry = np.zeros(cols, dtype=np.int32)
        lnmchecker.LeastNonMonotonic(monoAry, 0)
        self.assertEqual(monoAry[3], 1)

    # Test non-monotonic progress variable
    def testAdvancedLNM2(self):
        print "\nTest LeastNonMono Checking: AdvancedLNM Non-Monotonic"
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
        progVar.SetVal(1, 1, 4.0);
        progVar.SetVal(2, 1, 2.0);
        progVar.SetVal(3, 1, 3.0);
        progVar.SetVal(4, 1, 5.0);

        # Set column 2 (progress variable 2)
        progVar.SetVal(0, 2, 1.0);
        progVar.SetVal(1, 2, 2.0);
        progVar.SetVal(2, 2, 3.0);
        progVar.SetVal(3, 2, 4.0);
        progVar.SetVal(4, 2, 3.0);

        # Set column 3 (progress variable 3)
        progVar.SetVal(0, 3, 1.0);
        progVar.SetVal(1, 3, 7.0);
        progVar.SetVal(2, 3, 9.0);
        progVar.SetVal(3, 3, 11.0);
        progVar.SetVal(4, 3, 8.0);

        lnmchecker = leastnonmono.AdvancedLNM(progVar) # Create AdvancedLNM object
        monoAry = np.zeros(cols, dtype=np.int32)
        lnmchecker.LeastNonMonotonic(monoAry, 0)
        self.assertEqual(monoAry[1], 0)

    # Test non-monotonic progress variables with same percentages
    def testAdvancedLNM3(self):
        print "\nTest LeastNonMono Checking: AdvancedLNM Non-Monotonic Same Percentages"
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
        progVar.SetVal(1, 1, 4.0);
        progVar.SetVal(2, 1, 2.0);
        progVar.SetVal(3, 1, 3.0);
        progVar.SetVal(4, 1, 5.0);

        # Set column 2 (progress variable 2)
        progVar.SetVal(0, 2, 1.0);
        progVar.SetVal(1, 2, 2.0);
        progVar.SetVal(2, 2, 3.0);
        progVar.SetVal(3, 2, 4.0);
        progVar.SetVal(4, 2, 3.0);

        # Set column 3 (progress variable 3)
        progVar.SetVal(0, 3, 1.0);
        progVar.SetVal(1, 3, 7.0);
        progVar.SetVal(2, 3, 9.0);
        progVar.SetVal(3, 3, 11.0);
        progVar.SetVal(4, 3, 8.0);

        lnmchecker = leastnonmono.AdvancedLNM(progVar) # Create AdvancedLNM object
        monoAry = np.zeros(cols, dtype=np.int32)
        lnmchecker.LeastNonMonotonic(monoAry, 0)
        self.assertEqual(monoAry[3], 1)

if __name__ == '__main__':
    unittest.main()
