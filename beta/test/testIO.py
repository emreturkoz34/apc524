#!/usr/bin/env python

import sys
sys.path.append('../python')
sys.path.append('../mod')

import iofuncs as iof
import combinations as cs
import numpy as np
import os
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
    
    # test the gettitles function in ioFuncs
    def testGetTitles(self):
        f = open('testfile','w')
        f.write('* \n')
        strings = ['dojkfr', 'jkn   vsnkl', 'afkjaf', 'ajknnjv   nsv', '99"|} {{{}}#^&$']
        for i in strings:
            f.write(i)
            f.write('\t')
        f.close()
        dataobj = iof.ProcFile('testfile')
        titles = dataobj.gettitles()
        os.remove('testfile')
        np.testing.assert_array_equal(strings,titles)

    #test the read_inpit function in ioFuncs
    def testReadInput(self):
        inputsarray = [0] * 4
        inputsarray[0] = ['input1:', 3]
        inputsarray[1] = ['input2:', 'dogs']
        inputsarray[2] = ['input3:', 'rats']
        inputsarray[3] = ['input3:', 'cats']
        self.assertEqual(['dogs'], iof.read_input('input2:',inputsarray))
        self.assertEqual([3], iof.read_input('input1:', inputsarray))
        self.assertEqual([3], iof.read_input('input17:', inputsarray, default=[3]))
        self.assertEqual([3], iof.read_input('input1:', inputsarray, default=[2]))
        self.assertRaises(IOError, iof.read_input,'input3:',inputsarray)
        self.assertRaises(IOError, iof.read_input,'input17:',inputsarray)
        self.assertRaises(IOError, iof.read_input,'input1',inputsarray)
        self.assertRaises(IOError, iof.read_input,'input2:',inputsarray, minargs=2)
        

if __name__ == '__main__':
    unittest.main()




