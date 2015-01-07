#!/usr/bin/env python

import sys
sys.path.append('../python')

import combinations as cs
import numpy as np
import unittest


class TestFunctions(unittest.TestCase):
    #def testCombinations(self):
    #    slope = 3.0
    #    def f(x):
    #        return slope * x + 5.0
    #    x0 = 2.0
    #    dx = 1.e-3
    #    Df_x = F.ApproximateJacobian(f, x0, dx)
    #    self.assertEqual(Df_x.shape, (1,1))
    #    self.assertAlmostEqual(Df_x, slope)

    # test subfunctions within the combinations matrix generator
    def testCombsSub(self):
        vectorlength = 12
        pickvec = [1, 2, 12]
        CorrectNumComs = [12, 12*11, 12]
        for pick in pickvec:
            numberofcoms=cs.numcoms(vectorlength,pick)
            testcombos=np.zeros((vectorlength, numberofcoms))
            cs.combos(pick,testcombos)
            self.assertEqual
            self.assertEqual(testcombos.sum(),pick*numberofcoms, "The sum of elements of the output of combos is incorrect")
    
    # test the combinations matrix generator
    def testCombs(self):
        vectorlength = 12
        tot_numberofcoms = cs.totnumcoms(vectorlength)
        testmatrix = np.zeros((vectorlength, tot_numberofcoms))
        cs.combination_mat(testmatrix)
        correctsum = 0
        for i in range(vectorlength):
            correctsum += cs.numcoms(12,i+1)*(i+1)
        self.assertEqual(correctsum, testmatrix.sum())

if __name__ == '__main__':
    unittest.main()



