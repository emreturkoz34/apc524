#!/usr/bin/env python

import sys
sys.path.append('../python')
sys.path.append('../mod')

import iofuncs as iof
import findprogvar as fpv
import numpy as np
import os
import unittest
import shutil


class TestFunctions(unittest.TestCase):
    
    # test the findC function
    def testFindC(self):
        
        # set up inputs for test
        f = open('testfile1','w')
        f.write('*\nA\tB\tC\tD\tE\tF\tG\n')
        f.write('0\t10\t1\t10\t60\t2\t10\n')
        f.write('1\t20\t2\t20\t70\t3\t9\n')
        f.close()
        f = open('testfile2','w')
        f.write('*\nA\tB\tC\tD\tE\tF\tG\n')
        f.write('0\t30\t3\t40\t80\t6\t8\n')
        f.write('1\t40\t4\t50\t100\t7\t7\n')
        f.close()
        f = open('testfile3','w')
        f.write('*\nA\tB\tC\tD\tE\tF\tG\n')
        f.write('0\t20\t2\t30\t0\t10\t4\n')
        f.write('1\t30\t3\t40\t10\t9\t3\n')
        f.close()
        f = open('testfile4','w')
        f.write('*\nA\tB\tQ\tD\tE\tF\tG\n')
        f.close()
        datafiles = ['testfile1', 'testfile2', 'testfile3']
        bestC = []
        testspecies = ['C', 'D', 'E', 'F', 'G']
        options = {}
        options["sort method"] = ['bubble']
        options["StoichMassFrac"] = [0.5]
        options["InterpMethod"] = ['linear']
        options["MaxSlopeTest"] = ['linear regression']
        options["PlotAllC"] = ['yes']
        options["SkipProgVar"] = ['no']
        options["lnmcheck"] = ['simple']
        try:
            os.stat('output')
        except:
            os.mkdir('output')

        # most monotonic test
        fpv.findC(datafiles, testspecies, bestC, options)
        np.testing.assert_array_equal(bestC[1], ['C', 'D', 'F'])

        #least nonmonotonic test
        testspecies = ['E', 'F']
        fpv.findC(datafiles, testspecies, bestC, options)
        np.testing.assert_array_equal(bestC[1], ['E', 'F'])

        #skip optimization and use user input test
        testspecies = ['C', 'D', 'E', 'F', 'G']
        options["SkipProgVar"] = ['yes']
        fpv.findC(datafiles, testspecies, bestC, options)
        np.testing.assert_array_equal(bestC[1], ['C', 'D', 'E', 'F', 'G'])

        #test for raising error if datafile headers are not the same
        datafiles = ['testfile1', 'testfile2', 'testfile3', 'testfile4']
        self.assertRaises(AssertionError, fpv.findC, datafiles, testspecies, bestC, options)
        datafiles = ['testfile1', 'testfile2', 'testfile3']

        #test for errors when invalid options are specified
        options["sort method"] = ['bubblezfgvs']
        self.assertRaises(IOError, fpv.findC, datafiles, testspecies, bestC, options)
        options["sort method"] = ['bubble']
        options["SkipProgVar"] = ['ye1s']
        self.assertRaises(AssertionError, fpv.findC, datafiles, testspecies, bestC, options)
        options["SkipProgVar"] = ['no']
        options["MaxSlopeTest"] = ['cats and dogs']
        self.assertRaises(IOError, fpv.findC, datafiles, testspecies, bestC, options)
        options["MaxSlopeTest"] = ['linear regression']

        #remove data files generatred for testing purposes
        for i in ["testfile1", 'testfile2', 'testfile3', 'testfile4']:
            os.remove(i)
        shutil.rmtree('output')
        
        
if __name__ == '__main__':
    unittest.main()






