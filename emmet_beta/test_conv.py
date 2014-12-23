#!/usr/bin/env python
import numpy as np

import sys
sys.path.append('./mod')

import integrator
import convolute
import matrix3d
import matrix
import pdf

#####################################################
# Modify these values ONLY
#####################################################

ZPoints = 215
ZmeanPoints = 20
ZvarPoints = 6 # Delta PDF used if ZvarPoints == 1

ZMin = 0
ZMax = 1
ZmeanMin = 0
ZmeanMax = 1
ZvarMin = 0
ZvarMax = 0.25

# Mock data
RxnMin = -1
RxnMax = 5
ProgMin = 0
ProgMax = 0.3

# Gauss Legendre Quadrature
Nodes = 25

#####################################################
# Creates all arrays and objects needed
#####################################################

# create arrays
Z = np.linspace(ZMin, ZMax, ZPoints)
Zmean = np.linspace(ZmeanMin, ZmeanMax, ZmeanPoints)
Zvar = np.linspace(ZvarMin, ZvarMax, ZvarPoints)

# create PDF
if ZvarPoints == 1:
    d = pdf.DeltaPDF(Z) 
    print "delta PDF created"
else:
    d = pdf.BetaPDF(Z)
    print "beta PDF created"
pdfValM = matrix3d.Matrix3D(ZvarPoints, ZmeanPoints, ZPoints)
c = d.pdfVal(Zvar, Zmean, pdfValM)
print "PDF calculated"

# create Mock Data
rxnRates = np.linspace(RxnMin, RxnMax, ZPoints)
progVar  = np.linspace(ProgMin, ProgMax, ZPoints)
print "Mock data created"

# create Integrators
Trapz = integrator.Trapz()
Simps = integrator.Simpson()
Quadr = integrator.GLQuad(Nodes)
print "Integrators created"

# create Filtered Data Matrices
postTrapzRxn  = matrix.Matrix(ZvarPoints, ZmeanPoints)
postSimpsRxn  = matrix.Matrix(ZvarPoints, ZmeanPoints)
postQuadrRxn  = matrix.Matrix(ZvarPoints, ZmeanPoints)
postTrapzProg = matrix.Matrix(ZvarPoints, ZmeanPoints)
postSimpsProg = matrix.Matrix(ZvarPoints, ZmeanPoints)
postQuadrProg = matrix.Matrix(ZvarPoints, ZmeanPoints)
print "Filtered data matrices created"

# create matrix for printing
filtered = np.zeros((ZvarPoints, ZmeanPoints))

#####################################################
# Perform convolution
#####################################################

# calculate filtered reaction rates
c = convolute.convVal_func(Z, rxnRates, pdfValM, postTrapzRxn, Trapz)
c = convolute.convVal_func(Z, rxnRates, pdfValM, postSimpsRxn, Simps)
c = convolute.convVal_func(Z, rxnRates, pdfValM, postQuadrRxn, Quadr)
print "Filtered reaction rates calculated"

# calculate filtered progress variables
c = convolute.convVal_func(Z, progVar, pdfValM, postTrapzProg, Trapz)
c = convolute.convVal_func(Z, progVar, pdfValM, postSimpsProg, Simps)
c = convolute.convVal_func(Z, progVar, pdfValM, postQuadrProg, Quadr)
print "Filtered progress variables calculated"

#####################################################
# Print results
#####################################################

# Set print options
np.set_printoptions(precision=4, suppress=True)

# Reaction Rates:
for i in range(ZvarPoints):
    for j in range(ZmeanPoints):
        filtered[i,j] = postTrapzRxn.GetVal(i,j)
print "Trapz, RxnRates:"
print filtered
for i in range(ZvarPoints):
    for j in range(ZmeanPoints):
        filtered[i,j] = postSimpsRxn.GetVal(i,j)
print "Simps, RxnRates:"
print filtered
for i in range(ZvarPoints):
    for j in range(ZmeanPoints):
        filtered[i,j] = postQuadrRxn.GetVal(i,j)
print "Quadr, RxnRates:"
print filtered

# Progress Variables:
for i in range(ZvarPoints):
    for j in range(ZmeanPoints):
        filtered[i,j] = postTrapzProg.GetVal(i,j)
print "Trapz, ProgVar:"
print filtered
for i in range(ZvarPoints):
    for j in range(ZmeanPoints):
        filtered[i,j] = postSimpsProg.GetVal(i,j)
print "Simps, ProgVar:"
print filtered
for i in range(ZvarPoints):
    for j in range(ZmeanPoints):
        filtered[i,j] = postQuadrProg.GetVal(i,j)
print "Quadr, ProgVar:"
print filtered
