#!/usr/bin/env python

import numpy as np
import unittest

import sys
sys.path.append('../mod')

import matrix
import matrix3d
import pdf
import integrator
import convolute

class PDF(unittest.TestCase):
    np.set_printoptions(precision=2, suppress=True)
    
    def testDeltaPDF1(self):
        print "\n Delta PDF 1:"
        """
        NOTE: Simpson's Rule doesn't work for Delta PDFs; see integrator
        test for a proof/explanation
        """

        ZPoints = 5
        ZmeanPoints = 1
        ZvarPoints = 1
        
        ZMin = 0
        ZMax = 1
        ZmeanMin = 0.25
        ZmeanMax = ZmeanMin
        ZvarMin = 0
        ZvarMax = ZvarMin
                
        Nodes = 50

        # create arrays of type "double *"
        Z = np.linspace(ZMin, ZMax, ZPoints)
        Zmean = np.linspace(ZmeanMin, ZmeanMax, ZmeanPoints)
        Zvar = np.linspace(ZvarMin, ZvarMax, ZvarPoints)
        
        # create instances of PDF class
        d = pdf.DeltaPDF(Zmean) 
        dPdfValM = matrix3d.Matrix3D(ZvarPoints, ZmeanPoints, ZPoints)
        
        # expected PDF values
        PDF = np.zeros(ZPoints)
        PDF[1] = 1 * (ZPoints-1)

        # calculate PDF
        test = d.pdfVal(Z, dPdfValM)
        PDFCalc = np.zeros(ZPoints)

        # test
        for k in range(ZPoints):
            PDFCalc[k] = dPdfValM.GetVal(0,0,k)
            self.assertAlmostEqual(PDF[k], PDFCalc[k])

        # create Integrators
        Trapz = integrator.Trapz()
        Quadr = integrator.GLQuad(Nodes)

        # create Filtered Data Matrices
        postTrapz  = matrix.Matrix(ZvarPoints, ZmeanPoints)
        postQuadr  = matrix.Matrix(ZvarPoints, ZmeanPoints)

        # create matrix for printing
        filterTrapz = np.zeros(ZmeanPoints)
        filterQuadr = np.zeros(ZmeanPoints)

        # create test data
        testData = np.ones(ZPoints)

        # calculate filtered reaction rates
        c = convolute.convVal_func(Z, testData, dPdfValM, postTrapz, Trapz)
        c = convolute.convVal_func(Z, testData, dPdfValM, postQuadr, Quadr)

        for j in range(ZmeanPoints):
            filterTrapz[j] = postTrapz.GetVal(0,j)
            filterQuadr[j] = postQuadr.GetVal(0,j)
            self.assertEqual(filterTrapz[j], 1)
            self.assertAlmostEqual(filterQuadr[j], 1, 1)

    """
    NOTE: Simpson's Rule doesn't work for Delta PDFs and 
    is not tested here because Beta PDFs become Delta PDFs
    for zero or very high variances
    """
    def testBetaPDF1(self):
        print "\n Beta PDF 1: Zero Variance"

        ZPoints = 5
        ZmeanPoints = 1
        ZvarPoints = 1
        
        ZMin = 0
        ZMax = 1
        ZmeanMin = 0.25
        ZmeanMax = ZmeanMin
        ZvarMin = 0
        ZvarMax = ZvarMin
                
        Nodes = 50

        # create arrays of type "double *"
        Z = np.linspace(ZMin, ZMax, ZPoints)
        Zmean = np.linspace(ZmeanMin, ZmeanMax, ZmeanPoints)
        Zvar = np.linspace(ZvarMin, ZvarMax, ZvarPoints)
        
        # create instances of PDF class
        b = pdf.BetaPDF(Zmean, Zvar) 
        bPdfValM = matrix3d.Matrix3D(ZvarPoints, ZmeanPoints, ZPoints)
        
        # expected PDF values
        PDF = np.zeros(ZPoints)
        PDF[1] = 1 * (ZPoints-1)

        # calculate PDF
        test = b.pdfVal(Z, bPdfValM)
        PDFCalc = np.zeros(ZPoints)

        # test
        for k in range(ZPoints):
            PDFCalc[k] = bPdfValM.GetVal(0,0,k)
            self.assertAlmostEqual(PDF[k], PDFCalc[k])

        # create Integrators
        Trapz = integrator.Trapz()
        Quadr = integrator.GLQuad(Nodes)

        # create Filtered Data Matrices
        postTrapz  = matrix.Matrix(ZvarPoints, ZmeanPoints)
        postQuadr  = matrix.Matrix(ZvarPoints, ZmeanPoints)

        # create matrix for printing
        filterTrapz = np.zeros(ZmeanPoints)
        filterQuadr = np.zeros(ZmeanPoints)

        # create test data
        testData = np.ones(ZPoints)

        # calculate filtered reaction rates
        c = convolute.convVal_func(Z, testData, bPdfValM, postTrapz, Trapz)
        c = convolute.convVal_func(Z, testData, bPdfValM, postQuadr, Quadr)


        for j in range(ZmeanPoints):
            filterTrapz[j] = postTrapz.GetVal(0,j)
            filterQuadr[j] = postQuadr.GetVal(0,j)
            self.assertEqual(filterTrapz[j], 1)
            self.assertAlmostEqual(filterQuadr[j], 1, 1)


    def testBetaPDF2(self):
        print "\n Beta PDF 2: Infinite at Zmin/Zmax"

        Points = 6
        ZPoints = 101
        ZmeanPoints = 1
        ZvarPoints = 1
        
        ZMin = 0
        ZMax = 1
        ZmeanMin = 0.2
        ZmeanMax = ZmeanMin
        ZvarMin = 0.1
        ZvarMax = ZvarMin
                
        Nodes = 10

        # create arrays of type "double *"
        Z = np.linspace(ZMin, ZMax, ZPoints)
        Zmean = np.linspace(ZmeanMin, ZmeanMax, ZmeanPoints)
        Zvar = np.linspace(ZvarMin, ZvarMax, ZvarPoints)
        
        # create instances of PDF class
        b = pdf.BetaPDF(Zmean, Zvar) 
        bPdfValM = matrix3d.Matrix3D(ZvarPoints, ZmeanPoints, ZPoints)
        bPDF = np.zeros(Points)        

        # expected PDF values
        PDF = np.zeros(Points)
        PDF[0] = 5.93
        PDF[1] = 0.475
        PDF[2] = 0.300
        PDF[3] = 0.259
        PDF[4] = 0.288
        PDF[5] = 1.13

        # calculate PDF
        bTest = b.pdfVal(Z, bPdfValM)

        # test
        for k in range(Points):
            bPDF[k] = bPdfValM.GetVal(0,0,20*k)
        """
        print "PDF[0] = inf, bPDF[0] = " + str(bPDF[0])
        print "PDF[1] = " + str(PDF[1]) + ", bPDF[1] = " + str(bPDF[1])
        print "PDF[2] = " + str(PDF[2]) + ", bPDF[2] = " + str(bPDF[2])
        print "PDF[3] = " + str(PDF[3]) + ", bPDF[3] = " + str(bPDF[3])
        print "PDF[4] = " + str(PDF[4]) + ", bPDF[4] = " + str(bPDF[4])
        print "PDF[5] = inf, bPDF[5] = " + str(bPDF[5])
        """

        self.assertLess(np.abs(bPDF[1]-PDF[1]),0.2)
        self.assertLess(np.abs(bPDF[2]-PDF[2]),0.2)
        self.assertLess(np.abs(bPDF[3]-PDF[3]),0.2)
        self.assertLess(np.abs(bPDF[4]-PDF[4]),0.2)
        self.assertEqual(bTest, 0)

        # create Integrators
        Trapz = integrator.Trapz()
        Quadr = integrator.GLQuad(Nodes)

        # create Filtered Data Matrices
        postTrapz  = matrix.Matrix(ZvarPoints, ZmeanPoints)
        postQuadr  = matrix.Matrix(ZvarPoints, ZmeanPoints)

        # create matrix for printing
        filterTrapz = np.zeros(ZmeanPoints)
        filterQuadr = np.zeros(ZmeanPoints)

        # create test data
        testData = np.ones(ZPoints)

        # calculate filtered reaction rates
        c = convolute.convVal_func(Z, testData, bPdfValM, postTrapz, Trapz)
        c = convolute.convVal_func(Z, testData, bPdfValM, postQuadr, Quadr)

        for j in range(ZmeanPoints):
            filterTrapz[j] = postTrapz.GetVal(0,j)
            filterQuadr[j] = postQuadr.GetVal(0,j)
            self.assertLess(np.abs(filterTrapz[j]-1), 0.5)
            self.assertLess(np.abs(filterQuadr[j]-1), 0.5)


    def testBetaPDF3(self):
        print "\n Beta PDF 3: Symmetric"

        Points = 6
        ZPoints = 101
        ZmeanPoints = 1
        ZvarPoints = 1
        
        ZMin = 0
        ZMax = 1
        ZmeanMin = 0.5
        ZmeanMax = ZmeanMin
        ZvarMin = 0.05
        ZvarMax = ZvarMin
                
        Nodes = 10

        # create arrays of type "double *"
        Z = np.linspace(ZMin, ZMax, ZPoints)
        Zmean = np.linspace(ZmeanMin, ZmeanMax, ZmeanPoints)
        Zvar = np.linspace(ZvarMin, ZvarMax, ZvarPoints)
        
        # create instances of PDF class
        b = pdf.BetaPDF(Zmean, Zvar) 
        bPdfValM = matrix3d.Matrix3D(ZvarPoints, ZmeanPoints, ZPoints)
        bPDF = np.zeros(Points)        
        # expected PDF values
        PDF = np.zeros(ZPoints)
        PDF[0] = 0
        PDF[1] = 0.96
        PDF[2] = 1.44
        PDF[3] = 1.44
        PDF[4] = 0.96
        PDF[5] = 0

        # calculate PDF
        bTest = b.pdfVal(Z, bPdfValM)

        # test
        for k in range(Points):
            bPDF[k] = bPdfValM.GetVal(0,0,20*k)
        """
        print "PDF[0] = inf, bPDF[0] = " + str(bPDF[0])
        print "PDF[1] = " + str(PDF[1]) + ", bPDF[1] = " + str(bPDF[1])
        print "PDF[2] = " + str(PDF[2]) + ", bPDF[2] = " + str(bPDF[2])
        print "PDF[3] = " + str(PDF[3]) + ", bPDF[3] = " + str(bPDF[3])
        print "PDF[4] = " + str(PDF[4]) + ", bPDF[4] = " + str(bPDF[4])
        print "PDF[5] = inf, bPDF[5] = " + str(bPDF[5])
        """
        self.assertLess(np.abs(bPDF[1]-PDF[1]),0.2)
        self.assertLess(np.abs(bPDF[2]-PDF[2]),0.2)
        self.assertLess(np.abs(bPDF[3]-PDF[3]),0.2)
        self.assertLess(np.abs(bPDF[4]-PDF[4]),0.2)
        self.assertEqual(bTest, 0)


        # create Integrators
        Trapz = integrator.Trapz()
        Quadr = integrator.GLQuad(Nodes)

        # create Filtered Data Matrices
        postTrapz  = matrix.Matrix(ZvarPoints, ZmeanPoints)
        postQuadr  = matrix.Matrix(ZvarPoints, ZmeanPoints)

        # create matrix for printing
        filterTrapz = np.zeros(ZmeanPoints)
        filterQuadr = np.zeros(ZmeanPoints)

        # create test data
        testData = np.ones(ZPoints)

        # calculate filtered reaction rates
        c = convolute.convVal_func(Z, testData, bPdfValM, postTrapz, Trapz)
        c = convolute.convVal_func(Z, testData, bPdfValM, postQuadr, Quadr)

        for j in range(ZmeanPoints):
            filterTrapz[j] = postTrapz.GetVal(0,j)
            filterQuadr[j] = postQuadr.GetVal(0,j)
            self.assertLess(np.abs(filterTrapz[j]-1), 0.01)
            self.assertLess(np.abs(filterQuadr[j]-1), 0.01)


if __name__ == '__main__':
    unittest.main()
