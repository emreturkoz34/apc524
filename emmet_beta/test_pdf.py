#!/usr/bin/env python


import numpy as np

import sys
sys.path.append('./mod')

import matrix3d
import pdf

#####################################################
# Modify these values ONLY
#####################################################

ZPoints = 215
ZmeanPoints = 20
ZvarPoints = 1 # delta PDF used if ZvarPoints == 1

ZMin = 0
ZMax = 1
ZmeanMin = 0
ZmeanMax = 1
ZvarMin = 0
ZvarMax = 0.25


#####################################################
# Creates all arrays and objects needed
#####################################################

# create arrays of type "double *"
Z = np.linspace(ZMin, ZMax, ZPoints)
Zmean = np.linspace(ZmeanMin, ZmeanMax, ZmeanPoints)
Zvar = np.linspace(ZvarMin, ZvarMax, ZvarPoints)

# create instances of PDF class
if ZvarPoints == 1:
    d = pdf.DeltaPDF(Z) 
    print "delta PDF created"
else:
    d = pdf.BetaPDF(Z)
    print "beta PDF created"

pdfValM = matrix3d.Matrix3D(ZvarPoints, ZmeanPoints, ZPoints)
print "3D Matrix created"

# matrix for printing
PDF = np.zeros((ZmeanPoints, ZPoints))

#####################################################
# Calculates PDF
#####################################################

test = d.pdfVal(Zvar, Zmean, pdfValM)
print "PDF calculated"

#####################################################
# Prints results
#####################################################

# Set print options
np.set_printoptions(precision=2, suppress=True)

# Print results
for i in range(ZvarPoints):
    for j in range(ZmeanPoints):
        for k in range(ZPoints):
            PDF[j,k] = pdfValM.GetVal(i,j,k)
    print "\nvar = " + str(Zvar[i]) + ":"
    print PDF
