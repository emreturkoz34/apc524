#!/usr/bin/env python

import numpy as np
import unittest

import sys
sys.path.append('../mod')

import matrix3d
import pdf

class PDF(unittest.TestCase):
    np.set_printoptions(precision=2, suppress=True)
    
    def testDeltaPDF1(self):
        print "\n test Delta PDF 1:"
        ZPoints = 6
        ZmeanPoints = 1
        ZvarPoints = 1
        
        ZMin = 0
        ZMax = 1
        ZmeanMin = 0.2
        ZmeanMax = ZmeanMin
        ZvarMin = 0
        ZvarMax = ZvarMin
                
        # create arrays of type "double *"
        Z = np.linspace(ZMin, ZMax, ZPoints)
        Zmean = np.linspace(ZmeanMin, ZmeanMax, ZmeanPoints)
        Zvar = np.linspace(ZvarMin, ZvarMax, ZvarPoints)
        
        # create instances of PDF class
        d = pdf.DeltaPDF(Zmean) 
        dPdfValM = matrix3d.Matrix3D(ZvarPoints, ZmeanPoints, ZPoints)
        
        # expected PDF values
        PDF = np.zeros(ZPoints)
        PDF[1] = ZPoints-1

        # calculate PDF
        test = d.pdfVal(Z, dPdfValM)
        PDFCalc = np.zeros(ZPoints)

        # test
        for k in range(ZPoints):
            PDFCalc[k] = dPdfValM.GetVal(0,0,k)
            self.assertAlmostEqual(PDF[k], PDFCalc[k])

    def testDeltaPDF2(self):
        print "\n test Delta PDF 2:"
        ZPoints = 6
        ZmeanPoints = 1
        ZvarPoints = 1
        
        ZMin = 0
        ZMax = 1
        ZmeanMin = 0.25
        ZmeanMax = ZmeanMin
        ZvarMin = 0
        ZvarMax = ZvarMin
                
        # create arrays of type "double *"
        Z = np.linspace(ZMin, ZMax, ZPoints)
        Zmean = np.linspace(ZmeanMin, ZmeanMax, ZmeanPoints)
        Zvar = np.linspace(ZvarMin, ZvarMax, ZvarPoints)
        
        # create instances of PDF class
        d = pdf.DeltaPDF(Zmean) 
        dPdfValM = matrix3d.Matrix3D(ZvarPoints, ZmeanPoints, ZPoints)
        
        # expected PDF values
        PDF = np.zeros(ZPoints)
        PDF[1] = 0.75 * (ZPoints-1)
        PDF[2] = 0.25 * (ZPoints-1)

        # calculate PDF
        test = d.pdfVal(Z, dPdfValM)
        PDFCalc = np.zeros(ZPoints)

        # test
        for k in range(ZPoints):
            PDFCalc[k] = dPdfValM.GetVal(0,0,k)
            self.assertAlmostEqual(PDF[k], PDFCalc[k])

    def testBetaPDF1(self):
        print "\n test Beta PDF 1: Var = 0 --> Delta PDF"
        ZPoints = 6
        ZmeanPoints = 1
        ZvarPoints = 1
        
        ZMin = 0
        ZMax = 1
        ZmeanMin = 0.25
        ZmeanMax = ZmeanMin
        ZvarMin = 0
        ZvarMax = ZvarMin
                
        # create arrays of type "double *"
        Z = np.linspace(ZMin, ZMax, ZPoints)
        Zmean = np.linspace(ZmeanMin, ZmeanMax, ZmeanPoints)
        Zvar = np.linspace(ZvarMin, ZvarMax, ZvarPoints)
        
        # create instances of PDF class
        b = pdf.BetaPDF(Zmean, Zvar) 
        bPdfValM = matrix3d.Matrix3D(ZvarPoints, ZmeanPoints, ZPoints)
        bPDF = np.zeros(ZPoints)        

        # expected PDF values
        d = pdf.DeltaPDF(Zmean) 
        dPdfValM = matrix3d.Matrix3D(ZvarPoints, ZmeanPoints, ZPoints)
        dPDF = np.zeros(ZPoints)

        # calculate PDF
        bTest = b.pdfVal(Z, bPdfValM)
        dTest = d.pdfVal(Z, dPdfValM)

        # test
        for k in range(ZPoints):
            bPDF[k] = bPdfValM.GetVal(0,0,k)
            dPDF[k] = dPdfValM.GetVal(0,0,k)
            self.assertAlmostEqual(bPDF[k], dPDF[k])
        self.assertEqual(bTest, 0)
        self.assertEqual(dTest, 0)

    def testBetaPDF2(self):
        print "\n test Beta PDF 2: Mean = ZMin --> Delta PDF"
        ZPoints = 6
        ZmeanPoints = 1
        ZvarPoints = 1
        
        ZMin = 0
        ZMax = 1
        ZmeanMin = ZMin
        ZmeanMax = ZmeanMin
        ZvarMin = 0.2
        ZvarMax = ZvarMin
                
        # create arrays of type "double *"
        Z = np.linspace(ZMin, ZMax, ZPoints)
        Zmean = np.linspace(ZmeanMin, ZmeanMax, ZmeanPoints)
        Zvar = np.linspace(ZvarMin, ZvarMax, ZvarPoints)
        
        # create instances of PDF class
        b = pdf.BetaPDF(Zmean, Zvar) 
        bPdfValM = matrix3d.Matrix3D(ZvarPoints, ZmeanPoints, ZPoints)
        bPDF = np.zeros(ZPoints)        

        # expected PDF values
        d = pdf.DeltaPDF(Zmean) 
        dPdfValM = matrix3d.Matrix3D(ZvarPoints, ZmeanPoints, ZPoints)
        dPDF = np.zeros(ZPoints)

        # calculate PDF
        bTest = b.pdfVal(Z, bPdfValM)
        dTest = d.pdfVal(Z, dPdfValM)

        # test
        for k in range(ZPoints):
            bPDF[k] = bPdfValM.GetVal(0,0,k)
            dPDF[k] = dPdfValM.GetVal(0,0,k)
            self.assertAlmostEqual(bPDF[k], dPDF[k])
        self.assertEqual(bTest, 0)
        self.assertEqual(dTest, 0)

    def testBetaPDF3(self):
        print "\n test Beta PDF 3: Mean = ZMax --> Delta PDF"
        ZPoints = 6
        ZmeanPoints = 1
        ZvarPoints = 1
        
        ZMin = 0
        ZMax = 1
        ZmeanMin = ZMax
        ZmeanMax = ZmeanMin
        ZvarMin = 0.2
        ZvarMax = ZvarMin
                
        # create arrays of type "double *"
        Z = np.linspace(ZMin, ZMax, ZPoints)
        Zmean = np.linspace(ZmeanMin, ZmeanMax, ZmeanPoints)
        Zvar = np.linspace(ZvarMin, ZvarMax, ZvarPoints)
        
        # create instances of PDF class
        b = pdf.BetaPDF(Zmean, Zvar) 
        bPdfValM = matrix3d.Matrix3D(ZvarPoints, ZmeanPoints, ZPoints)
        bPDF = np.zeros(ZPoints)        

        # expected PDF values
        d = pdf.DeltaPDF(Zmean) 
        dPdfValM = matrix3d.Matrix3D(ZvarPoints, ZmeanPoints, ZPoints)
        dPDF = np.zeros(ZPoints)

        # calculate PDF
        bTest = b.pdfVal(Z, bPdfValM)
        dTest = d.pdfVal(Z, dPdfValM)

        # test
        for k in range(ZPoints):
            bPDF[k] = bPdfValM.GetVal(0,0,k)
            dPDF[k] = dPdfValM.GetVal(0,0,k)
            self.assertAlmostEqual(bPDF[k], dPDF[k])
        self.assertEqual(bTest, 0)
        self.assertEqual(dTest, 0)

    def testBetaPDF4(self):
        print "\n test Beta PDF 4: Var >= Mean * (1 - Mean) --> Double Delta PDF"
        ZPoints = 6
        ZmeanPoints = 1
        ZvarPoints = 1
        
        ZMin = 0
        ZMax = 1
        ZmeanMin = 0.25
        ZmeanMax = ZmeanMin
        ZvarMin = 0.2
        ZvarMax = ZvarMin
                
        # create arrays of type "double *"
        Z = np.linspace(ZMin, ZMax, ZPoints)
        Zmean = np.linspace(ZmeanMin, ZmeanMax, ZmeanPoints)
        Zvar = np.linspace(ZvarMin, ZvarMax, ZvarPoints)
        
        # create instances of PDF class
        b = pdf.BetaPDF(Zmean, Zvar) 
        bPdfValM = matrix3d.Matrix3D(ZvarPoints, ZmeanPoints, ZPoints)
        bPDF = np.zeros(ZPoints)        

        # expected PDF values
        dPDF = np.zeros(ZPoints)
        dPDF[0] = 0.75 * (ZPoints-1)
        dPDF[ZPoints-1] = 0.25 * (ZPoints-1)

        # calculate PDF
        bTest = b.pdfVal(Z, bPdfValM)

        # test
        for k in range(ZPoints):
            bPDF[k] = bPdfValM.GetVal(0,0,k)
            self.assertAlmostEqual(bPDF[k], dPDF[k])
        self.assertEqual(bTest, 0)

    def testBetaPDF5(self):
        print "\n test Beta PDF 5: Infinite Min/Max"
        ZPoints = 101
        ZmeanPoints = 1
        ZvarPoints = 1
        
        ZMin = 0
        ZMax = 1
        ZmeanMin = 0.2
        ZmeanMax = ZmeanMin
        ZvarMin = 0.1
        ZvarMax = ZvarMin
                
        # create arrays of type "double *"
        Z = np.linspace(ZMin, ZMax, ZPoints)
        Zmean = np.linspace(ZmeanMin, ZmeanMax, ZmeanPoints)
        Zvar = np.linspace(ZvarMin, ZvarMax, ZvarPoints)
        
        # create instances of PDF class
        b = pdf.BetaPDF(Zmean, Zvar) 
        bPdfValM = matrix3d.Matrix3D(ZvarPoints, ZmeanPoints, ZPoints)
        bPDF = np.zeros(ZPoints)        
        # expected PDF values
        PDF = np.zeros(ZPoints)
        PDF[0] = 5.93
        PDF[1] = 0.475
        PDF[2] = 0.300
        PDF[3] = 0.259
        PDF[4] = 0.288
        PDF[5] = 1.13

        # calculate PDF
        bTest = b.pdfVal(Z, bPdfValM)

        # test
        for k in range(ZPoints):
            bPDF[k] = bPdfValM.GetVal(0,0,20*k)
        """
        print "PDF[0,0] = inf, bPDF[0,0] = " + str(bPDF[0,0])
        print "PDF[0,1] = " + str(PDF[0,1]) + ", bPDF[0,1] = " + str(bPDF[0,20])
        print "PDF[0,2] = " + str(PDF[0,2]) + ", bPDF[0,2] = " + str(bPDF[0,40])
        print "PDF[0,3] = " + str(PDF[0,3]) + ", bPDF[0,3] = " + str(bPDF[0,60])
        print "PDF[0,4] = " + str(PDF[0,4]) + ", bPDF[0,4] = " + str(bPDF[0,80])
        print "PDF[0,5] = inf, bPDF[0,5] = " + str(bPDF[0,100])
        """
        self.assertLess(np.abs(bPDF[1]-PDF[1]),0.01)
        self.assertLess(np.abs(bPDF[2]-PDF[2]),0.01)
        self.assertLess(np.abs(bPDF[3]-PDF[3]),0.01)
        self.assertLess(np.abs(bPDF[4]-PDF[4]),0.01)
        self.assertEqual(bTest, 0)


    def testBetaPDF6(self):
        print "\n test Beta PDF 6: Skewed"
        ZPoints = 101
        ZmeanPoints = 1
        ZvarPoints = 1
        
        ZMin = 0
        ZMax = 1
        ZmeanMin = 0.1
        ZmeanMax = ZmeanMin
        ZvarMin = 0.01
        ZvarMax = ZvarMin
                
        # create arrays of type "double *"
        Z = np.linspace(ZMin, ZMax, ZPoints)
        Zmean = np.linspace(ZmeanMin, ZmeanMax, ZmeanPoints)
        Zvar = np.linspace(ZvarMin, ZvarMax, ZvarPoints)
        
        # create instances of PDF class
        b = pdf.BetaPDF(Zmean, Zvar) 
        bPdfValM = matrix3d.Matrix3D(ZvarPoints, ZmeanPoints, ZPoints)
        bPDF = np.zeros(ZPoints)        

        # expected PDF values
        PDF = np.zeros(ZPoints)
        PDF[0] = 5.93
        PDF[1] = 1.43
        PDF[2] = 0.209
        PDF[3] = 0.01557
        PDF[4] = 0
        PDF[5] = 0

        # calculate PDF
        bTest = b.pdfVal(Z, bPdfValM)

        # test
        for k in range(ZPoints):
            bPDF[k] = bPdfValM.GetVal(0,0,20*k)
        """
        print "PDF[0] = inf, bPDF[0] = " + str(bPDF[0])
        print "PDF[1] = " + str(PDF[1]) + ", bPDF[1] = " + str(bPDF[1])
        print "PDF[2] = " + str(PDF[2]) + ", bPDF[2] = " + str(bPDF[2])
        print "PDF[3] = " + str(PDF[3]) + ", bPDF[3] = " + str(bPDF[3])
        print "PDF[4] = " + str(PDF[4]) + ", bPDF[4] = " + str(bPDF[4])
        print "PDF[5] = " + str(PDF[5]) + ", bPDF[4] = " + str(bPDF[5])
        print "PDF[6] = inf, bPDF[5] = " + str(bPDF[6])
        """
        self.assertLess(np.abs(bPDF[1]-PDF[1]),0.01)
        self.assertLess(np.abs(bPDF[2]-PDF[2]),0.01)
        self.assertLess(np.abs(bPDF[3]-PDF[3]),0.01)
        self.assertLess(np.abs(bPDF[4]-PDF[4]),0.01)
        self.assertLess(np.abs(bPDF[5]-PDF[5]),0.01)
        self.assertEqual(bTest, 0)

    def testBetaPDF7(self):
        print "\n test Beta PDF 7: Symmetric"
        ZPoints = 101
        ZmeanPoints = 1
        ZvarPoints = 1
        
        ZMin = 0
        ZMax = 1
        ZmeanMin = 0.5
        ZmeanMax = ZmeanMin
        ZvarMin = 0.05
        ZvarMax = ZvarMin
                
        # create arrays of type "double *"
        Z = np.linspace(ZMin, ZMax, ZPoints)
        Zmean = np.linspace(ZmeanMin, ZmeanMax, ZmeanPoints)
        Zvar = np.linspace(ZvarMin, ZvarMax, ZvarPoints)
        
        # create instances of PDF class
        b = pdf.BetaPDF(Zmean, Zvar) 
        bPdfValM = matrix3d.Matrix3D(ZvarPoints, ZmeanPoints, ZPoints)
        bPDF = np.zeros(ZPoints)        
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
        for k in range(ZPoints):
            bPDF[k] = bPdfValM.GetVal(0,0,20*k)
        """
        print "PDF[0] = " + str(PDF[0]) + ", bPDF[0] = " + str(bPDF[0])
        print "PDF[1] = " + str(PDF[1]) + ", bPDF[1] = " + str(bPDF[1])
        print "PDF[2] = " + str(PDF[2]) + ", bPDF[2] = " + str(bPDF[2])
        print "PDF[3] = " + str(PDF[3]) + ", bPDF[3] = " + str(bPDF[3])
        print "PDF[4] = " + str(PDF[4]) + ", bPDF[4] = " + str(bPDF[4])
        print "PDF[5] = " + str(PDF[5]) + ", bPDF[5] = " + str(bPDF[5])
        """
        self.assertLess(np.abs(bPDF[1]-PDF[1]),0.1)
        self.assertLess(np.abs(bPDF[2]-PDF[2]),0.1)
        self.assertLess(np.abs(bPDF[3]-PDF[3]),0.1)
        self.assertLess(np.abs(bPDF[4]-PDF[4]),0.1)
        self.assertLess(np.abs(bPDF[5]-PDF[5]),0.1)
        self.assertEqual(bTest, 0)


if __name__ == '__main__':
    unittest.main()




