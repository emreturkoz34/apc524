#!/usr/bin/env python

import sys
sys.path.append('../python')
sys.path.append('../mod')

import iofuncs as iof
import numpy as np
import os
import unittest


class TestFunctions(unittest.TestCase):
    
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

    # test the read_inpit function in ioFuncs
    # tests for correct reading and raising appropriate errors, using defaults when relevant
    def testReadInput(self):
        inputsarray = [0] * 5
        inputsarray[0] = ['input1:', 3]
        inputsarray[1] = ['input2:', 'dogs']
        inputsarray[2] = ['input3:', 'rats']
        inputsarray[3] = ['input3:', 'cats']
        inputsarray[4] = ['input4:', 'cats', 'dogs', 'tigers']
        self.assertEqual(['dogs'], iof.read_input('input2:',inputsarray))
        self.assertEqual([3], iof.read_input('input1:', inputsarray))
        self.assertEqual([3], iof.read_input('input17:', inputsarray, default=[3]))
        self.assertEqual([3], iof.read_input('input1:', inputsarray, default=[2]))
        np.testing.assert_array_equal(['cats', 'dogs', 'tigers'], iof.read_input('input4:', inputsarray))
        self.assertRaises(IOError, iof.read_input,'input3:',inputsarray)
        self.assertRaises(IOError, iof.read_input,'input17:',inputsarray)
        self.assertRaises(IOError, iof.read_input,'input1',inputsarray)
        self.assertRaises(IOError, iof.read_input,'input2:',inputsarray, minargs=2)

    # test the python interpolation wrapper in iofuncs
    def testInterpolate(self):
        f = open('testfile','w')
        f.write('* \n')
        f.write('A\tB\tC\tD\tE\tF\tG\tH\tI\tJ\n')
        for i in range(10):
            for j in range(10):
                f.write('%d\t' % (i*10+j))
            f.write('\n')
        f.close()
        dataobj = iof.ProcFile('testfile')
        locs = np.zeros(3)
        datavec = np.zeros(4)
        dataobj.interpolate(['C', 'D', 'J'], locs, datavec, interpval = 63)
        np.testing.assert_array_almost_equal(datavec, [64, 65, 66, 72])
        self.assertRaises(RuntimeError, dataobj.interpolate, ['C', 'D', 'J'], locs, datavec, interpval = 124)
        self.assertRaises(IOError, dataobj.interpolate, ['C', 'D', 'J'], locs, datavec, interpmethod = 'linexar')
        self.assertRaises(IOError, dataobj.interpolate, ['C', 'Q', 'J'], locs, datavec, interpmethod = 'linear')
        os.remove('testfile')
        
if __name__ == '__main__':
    unittest.main()






