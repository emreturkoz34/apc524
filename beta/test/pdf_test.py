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
        PDF = np.zeros((ZmeanPoints, ZPoints))
        PDF[0, 1] = ZPoints-1

        # calculate PDF
        test = d.pdfVal(Z, dPdfValM)
        PDFCalc = np.zeros((ZmeanPoints, ZPoints))

        # test
        for i in range(ZvarPoints):
            for j in range(ZmeanPoints):
                for k in range(ZPoints):
                    PDFCalc[j,k] = dPdfValM.GetVal(i,j,k)
        for k in range(ZPoints):
            self.assertAlmostEqual(PDF[0,k], PDFCalc[0,k])

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
        PDF = np.zeros((ZmeanPoints, ZPoints))
        PDF[0, 1] = 0.75 * (ZPoints-1)
        PDF[0, 2] = 0.25 * (ZPoints-1)

        # calculate PDF
        test = d.pdfVal(Z, dPdfValM)
        PDFCalc = np.zeros((ZmeanPoints, ZPoints))

        # test
        for i in range(ZvarPoints):
            for j in range(ZmeanPoints):
                for k in range(ZPoints):
                    PDFCalc[j,k] = dPdfValM.GetVal(i,j,k)
        for k in range(ZPoints):
            self.assertAlmostEqual(PDF[0,k], PDFCalc[0,k])

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
        bPDF = np.zeros((ZmeanPoints, ZPoints))        

        # expected PDF values
        d = pdf.DeltaPDF(Zmean) 
        dPdfValM = matrix3d.Matrix3D(ZvarPoints, ZmeanPoints, ZPoints)
        dPDF = np.zeros((ZmeanPoints, ZPoints))

        # calculate PDF
        bTest = b.pdfVal(Z, bPdfValM)
        dTest = d.pdfVal(Z, dPdfValM)

        # test
        for i in range(ZvarPoints):
            for j in range(ZmeanPoints):
                for k in range(ZPoints):
                    bPDF[j,k] = bPdfValM.GetVal(i,j,k)
                    dPDF[j,k] = dPdfValM.GetVal(i,j,k)
                    self.assertAlmostEqual(bPDF[j,k], dPDF[j,k])
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
        bPDF = np.zeros((ZmeanPoints, ZPoints))        

        # expected PDF values
        d = pdf.DeltaPDF(Zmean) 
        dPdfValM = matrix3d.Matrix3D(ZvarPoints, ZmeanPoints, ZPoints)
        dPDF = np.zeros((ZmeanPoints, ZPoints))

        # calculate PDF
        bTest = b.pdfVal(Z, bPdfValM)
        dTest = d.pdfVal(Z, dPdfValM)

        # test
        for i in range(ZvarPoints):
            for j in range(ZmeanPoints):
                for k in range(ZPoints):
                    bPDF[j,k] = bPdfValM.GetVal(i,j,k)
                    dPDF[j,k] = dPdfValM.GetVal(i,j,k)
                    self.assertAlmostEqual(bPDF[j,k], dPDF[j,k])
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
        bPDF = np.zeros((ZmeanPoints, ZPoints))        

        # expected PDF values
        d = pdf.DeltaPDF(Zmean) 
        dPdfValM = matrix3d.Matrix3D(ZvarPoints, ZmeanPoints, ZPoints)
        dPDF = np.zeros((ZmeanPoints, ZPoints))

        # calculate PDF
        bTest = b.pdfVal(Z, bPdfValM)
        dTest = d.pdfVal(Z, dPdfValM)

        # test
        for i in range(ZvarPoints):
            for j in range(ZmeanPoints):
                for k in range(ZPoints):
                    bPDF[j,k] = bPdfValM.GetVal(i,j,k)
                    dPDF[j,k] = dPdfValM.GetVal(i,j,k)
                    self.assertAlmostEqual(bPDF[j,k], dPDF[j,k])
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
        bPDF = np.zeros((ZmeanPoints, ZPoints))        

        # expected PDF values
        dPDF = np.zeros((ZmeanPoints, ZPoints))
        dPDF[0, 0] = 0.75 * (ZPoints-1)
        dPDF[0, ZPoints-1] = 0.25 * (ZPoints-1)

        # calculate PDF
        bTest = b.pdfVal(Z, bPdfValM)

        # test
        for i in range(ZvarPoints):
            for j in range(ZmeanPoints):
                for k in range(ZPoints):
                    bPDF[j,k] = bPdfValM.GetVal(i,j,k)
                    self.assertAlmostEqual(bPDF[j,k], dPDF[j,k])
        self.assertEqual(bTest, 0)

    def testBetaPDF4(self):
        print "\n test Beta PDF 4: Infinite Min/Max"
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
        bPDF = np.zeros((ZmeanPoints, ZPoints))        
        # expected PDF values
        PDF = np.zeros((ZmeanPoints, ZPoints))
        PDF[0, 0] = 5.93
        PDF[0, 1] = 0.475
        PDF[0, 2] = 0.300
        PDF[0, 3] = 0.259
        PDF[0, 4] = 0.288
        PDF[0, 5] = 1.13

        # calculate PDF
        bTest = b.pdfVal(Z, bPdfValM)

        # test
        for i in range(ZvarPoints):
            for j in range(ZmeanPoints):
                for k in range(ZPoints):
                    bPDF[j,k] = bPdfValM.GetVal(i,j,k)
        """
        print "PDF[0,0] = inf, bPDF[0,0] = " + str(bPDF[0,0])
        print "PDF[0,1] = " + str(PDF[0,1]) + ", bPDF[0,1] = " + str(bPDF[0,20])
        print "PDF[0,2] = " + str(PDF[0,2]) + ", bPDF[0,2] = " + str(bPDF[0,40])
        print "PDF[0,3] = " + str(PDF[0,3]) + ", bPDF[0,3] = " + str(bPDF[0,60])
        print "PDF[0,4] = " + str(PDF[0,4]) + ", bPDF[0,4] = " + str(bPDF[0,80])
        print "PDF[0,5] = inf, bPDF[0,5] = " + str(bPDF[0,100])
        """
        self.assertLess(bPDF[0,1*20]-PDF[0,1],0.2)
        self.assertLess(bPDF[0,2*20]-PDF[0,2],0.2)
        self.assertLess(bPDF[0,3*20]-PDF[0,3],0.2)
        self.assertLess(bPDF[0,4*20]-PDF[0,4],0.2)
        self.assertEqual(bTest, 0)


    def testBetaPDF6(self):
        print "\n test Beta PDF 5: Skewed"
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
        bPDF = np.zeros((ZmeanPoints, ZPoints))        
        # expected PDF values
        PDF = np.zeros((ZmeanPoints, ZPoints))
        #        PDF[0, 0] = 5.93
        PDF[0, 1] = 1.43
        PDF[0, 2] = 0.209
        PDF[0, 3] = 0.01557
        PDF[0, 4] = 0
        PDF[0, 5] = 0

        # calculate PDF
        bTest = b.pdfVal(Z, bPdfValM)

        # test
        for i in range(ZvarPoints):
            for j in range(ZmeanPoints):
                for k in range(ZPoints):
                    bPDF[j,k] = bPdfValM.GetVal(i,j,20*k)

        print "PDF[0,0] = inf, bPDF[0,0] = " + str(bPDF[0,0])
        print "PDF[0,1] = " + str(PDF[0,1]) + ", bPDF[0,1] = " + str(bPDF[0,1])
        print "PDF[0,2] = " + str(PDF[0,2]) + ", bPDF[0,2] = " + str(bPDF[0,2])
        print "PDF[0,3] = " + str(PDF[0,3]) + ", bPDF[0,3] = " + str(bPDF[0,3])
        print "PDF[0,4] = " + str(PDF[0,4]) + ", bPDF[0,4] = " + str(bPDF[0,4])
        print "PDF[0,4] = " + str(PDF[0,5]) + ", bPDF[0,4] = " + str(bPDF[0,5])
        print "PDF[0,5] = inf, bPDF[0,5] = " + str(bPDF[0,100])

        self.assertLess(bPDF[0,1]-PDF[0,1],0.2)
        self.assertLess(bPDF[0,2]-PDF[0,2],0.2)
        self.assertLess(bPDF[0,3]-PDF[0,3],0.2)
        self.assertLess(bPDF[0,4]-PDF[0,4],0.2)
        self.assertLess(bPDF[0,5]-PDF[0,5],0.2)
        self.assertEqual(bTest, 0)

    def testBetaPDF6(self):
        print "\n test Beta PDF 6: Symmetric"
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
        bPDF = np.zeros((ZmeanPoints, ZPoints))        
        # expected PDF values
        PDF = np.zeros((ZmeanPoints, ZPoints))
        PDF[0, 0] = 0
        PDF[0, 1] = 0.96
        PDF[0, 2] = 1.44
        PDF[0, 3] = 1.44
        PDF[0, 4] = 0.96
        PDF[0, 5] = 0

        # calculate PDF
        bTest = b.pdfVal(Z, bPdfValM)

        # test
        for i in range(ZvarPoints):
            for j in range(ZmeanPoints):
                for k in range(ZPoints):
                    bPDF[j,k] = bPdfValM.GetVal(i,j,20*k)
        """
        print "PDF[0,0] = " + str(PDF[0,0]) + ", bPDF[0,0] = " + str(bPDF[0,0])
        print "PDF[0,1] = " + str(PDF[0,1]) + ", bPDF[0,1] = " + str(bPDF[0,1])
        print "PDF[0,2] = " + str(PDF[0,2]) + ", bPDF[0,2] = " + str(bPDF[0,2])
        print "PDF[0,3] = " + str(PDF[0,3]) + ", bPDF[0,3] = " + str(bPDF[0,3])
        print "PDF[0,4] = " + str(PDF[0,4]) + ", bPDF[0,4] = " + str(bPDF[0,4])
        print "PDF[0,5] = " + str(PDF[0,5]) + ", bPDF[0,5] = " + str(bPDF[0,5])
        """
        self.assertLess(bPDF[0,1]-PDF[0,1],0.1)
        self.assertLess(bPDF[0,2]-PDF[0,2],0.1)
        self.assertLess(bPDF[0,3]-PDF[0,3],0.1)
        self.assertLess(bPDF[0,4]-PDF[0,4],0.1)
        self.assertLess(bPDF[0,5]-PDF[0,5],0.1)
        self.assertEqual(bTest, 0)


if __name__ == '__main__':
    unittest.main()




