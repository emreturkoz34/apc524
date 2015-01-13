#!/usr/bin/env python

import numpy as np
import unittest

import sys
sys.path.append('../mod')

import fittogrid
import interpolator
import matrix
import matrix3d
import matrix4d
    
# Set up inputs to fittogrid function
dim1 = 2    # w~ and c~
dim2 = 1    # dimension of z~
dim3 = 1    # dimension of z_v
dim4 = 10   # number of files
lcgrid = 10 # length of cgrid
datain = matrix4d.Matrix4D(dim1, dim2, dim3, dim4)
cgrid = np.zeros((lcgrid))
interp = interpolator.LinInterp()
dataout = matrix3d.Matrix3D(dim2, dim3, lcgrid)
nthreads = 1

# Fill input data with numbers
for i in range(dim4):
    datain.SetVal(0, 0, 0, i, i*i)
    datain.SetVal(1, 0, 0, i, i + 1)

class FitToGrid(unittest.TestCase):

    def testNodes(self):
        # Test if node values are returned when the interpolating grid
        # is exactly along the nodes
        for i in range(lcgrid):
            cgrid[i] = i + 1
        flag = fittogrid.fittogrid_func(datain, cgrid, interp, dataout, nthreads, 0)
        self.assertEqual(flag, 0)
        for i in range(lcgrid):
            self.assertAlmostEqual(dataout.GetVal(0, 0, i), datain.GetVal(0, 0, 0, i))

    def testExtrap1(self):
        # Test if extrapolation caught and data is correctly extrapolated (extrap = on)
        for i in range(lcgrid - 2):
            cgrid[i+1] = i + 2
        cgrid[0] = 0
        cgrid[lcgrid-1] = 11
        flag = fittogrid.fittogrid_func(datain, cgrid, interp, dataout, nthreads, 1)
        self.assertEqual(flag, 1)
        for i in range(lcgrid - 2):
            self.assertAlmostEqual(dataout.GetVal(0, 0, i+1), datain.GetVal(0, 0, 0, i+1))
        self.assertEqual(dataout.GetVal(0, 0, 0), datain.GetVal(0, 0, 0, 1))
        self.assertEqual(dataout.GetVal(0, 0, lcgrid-1), datain.GetVal(0, 0, 0, lcgrid-2))

    def testExtrap2(self):
        # Test if extrapolation caught and data is correctly extrapolated (extrap = off)
        for i in range(lcgrid - 2):
            cgrid[i+1] = i + 2
        cgrid[0] = 0
        cgrid[lcgrid-1] = 11
        flag = fittogrid.fittogrid_func(datain, cgrid, interp, dataout, nthreads, 0)
        self.assertEqual(flag, 1)
        for i in range(lcgrid - 2):
            self.assertAlmostEqual(dataout.GetVal(0, 0, i+1), datain.GetVal(0, 0, 0, i+1))
        self.assertEqual(dataout.GetVal(0, 0, 0), 0)
        self.assertEqual(dataout.GetVal(0, 0, lcgrid-1), 0)

if __name__ == '__main__':
    unittest.main()
    
