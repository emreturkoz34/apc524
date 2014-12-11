import vector
import matrix
import matrix3d
import deltaPDF
import betaPDF
import convolute
import trapz

import helper
import numpy as np

ZPoints = 11
ZMin = 0
ZMax = 1
ZPy = helper.Line()
ZPy = np.linspace(ZMin, ZMax, ZPoints)
Z = vector.Vector(ZPoints)
helper.copy_py_to_vector(ZPy, Z)
"""
print 'ZPy'
helper.print_py(ZPy)
print 'Z'
"""
"""
for i in range(0, ZPoints):
    s =  'Z[' + repr(i) + '] = ' + repr(Z.GetVal(i))
    print s
"""

ZmeanPoints = ZPoints
ZmeanMin = 0
ZmeanMax = 1
ZmeanPy = helper.Line()
ZmeanPy = np.linspace(ZmeanMin, ZmeanMax, ZmeanPoints)
Zmean = vector.Vector(ZmeanPoints)
helper.copy_py_to_vector(ZmeanPy, Zmean)
"""
print 'ZmeanPy'
helper.print_py(ZmeanPy)
"""

ZvarPoints = 6
ZvarMin = 0
ZvarMax = 0.25
ZvarPy = helper.Line()
ZvarPy = np.linspace(ZvarMin, ZvarMax, ZvarPoints)
Zvar = vector.Vector(ZvarPoints)
helper.copy_py_to_vector(ZvarPy, Zvar)
"""
print 'ZvarPy'
helper.print_py(ZvarPy)
print 'Zvar'
for i in range(0, ZvarPoints):
    s = 'Zvar[' + repr(i) + '] = ' + repr(Zvar.GetVal(i))
    print s
"""

pdfValMPy = helper.Line()
pdfValMPy = np.empty(ZvarPoints * ZmeanPoints)
pdfValM = matrix3d.Matrix3D(ZvarPoints, ZmeanPoints, ZPoints)

d = betaPDF.BetaPDF(Z, ZPoints)
for i in range(0, ZvarPoints):
    for j in range(0, ZmeanPoints):
        for k in range(0, ZPoints):
            pdfValM.SetVal(i, j, k, 0)
pdfValReturn = d.pdfVal(Zvar, Zmean, pdfValM)
"""
for i in range(0, ZvarPoints):
    for j in range(0, ZmeanPoints):
        for k in range(0, ZPoints):
            s = 'pdfValM[var = ' + repr(Zvar.GetVal(i)) + '][mean = ' + repr(Zmean.GetVal(j)) + '][Z = ' + repr(Z.GetVal(k)) + '] = ' + repr(pdfValM.GetVal(i, j, k))
            print s
"""

TrapzIntgr = trapz.Trapz(Z, ZPoints)
Conv = convolute.Convolute(ZPoints)

DataSize = 2
DataPy = helper.Line()
DataPy = np.zeros(DataSize * ZPoints)
Data = vector.Vector(ZPoints)
"""Reaction Rates"""
DataPy[0:ZPoints] = np.linspace(-1, 5, ZPoints)
"""Progress Variables"""
DataPy[ZPoints:2*ZPoints] = np.linspace(0, 0.3, ZPoints)

PostConvValM = matrix.Matrix(ZvarPoints, ZmeanPoints)
PostConvValPy = helper.Line()
PostConvValPy = np.zeros(DataSize * ZmeanPoints * ZvarPoints)

for i in range(0,DataSize):
    if i == 0:
        print "All filtered rxn rates"
    else:
        print "All filtered progress variables"
    helper.copy_py_to_vector(DataPy[i*ZPoints:(i+1)*ZPoints], Data)
    ConvReturn = Conv.convVal(pdfValM, Data, PostConvValM, TrapzIntgr)
    helper.copy_matrix_to_py(PostConvValM, PostConvValPy[i*ZmeanPoints*ZvarPoints:(i+1)*ZmeanPoints*ZvarPoints])
    for j in range(0, ZvarPoints):
        for k in range(0, ZmeanPoints):
            s = 'Zmean = ' + repr(round(Zmean.GetVal(k),2)) + ', Zvar = ' + repr(round(Zvar.GetVal(j),2)) + ', Var = ' + repr(round(PostConvValM.GetVal(j,k),2))
            print s


""" Print out PDF, Data, and Convoluted Data at Zmean and Zvar """
ZmeanPrint = 4
ZvarPrint = 3
print ''
print 'Zmean = ' + repr(Zmean.GetVal(ZmeanPrint))
print 'Zvar  = ' + repr(Zvar.GetVal(ZvarPrint))
print ''
print 'PDF'
for i in range(0, ZPoints):
    s = 'Z = ' + repr(round(Z.GetVal(i),2)) + ', pdfValM = ' + repr(pdfValM.GetVal(ZvarPrint, ZmeanPrint, i))
    print s

print ''
print 'Data'
print 'Src Terms'
for i in range(0, ZPoints):
    s = 'Z = ' + repr(round(Z.GetVal(i),2)) + ', omega = ' + repr(round(DataPy[i],2))
    print s
print 'Prog Var'
for i in range(0, ZPoints):
    s = 'Z = ' + repr(round(Z.GetVal(i),2)) + ', C     = ' + repr(round(DataPy[ZPoints+i],2))
    print s
"""
print 'Data convoluted against PDF'
print 'All rxn rates filtered from PostConvValM'
for i in range(0, ZvarPoints):
    for j in range(0, ZmeanPoints):
        s = 'Zmean = ' + repr(round(Zmean.GetVal(j),2)) + ', Zvar = ' + repr(round(Zvar.GetVal(i),2)) + ', Omega = ' + repr(PostConvValM.GetVal(i,j))
        print s
print 'All prog var filtered from PostConvValM'
for i in range(0, ZvarPoints):
    for j in range(0, ZmeanPoints):
        s = 'Zmean = ' + repr(round(Zmean.GetVal(j),2)) + ', Zvar = ' + repr(round(Zvar.GetVal(i),2)) + ', Cfilt = ' + repr(PostConvValM.GetVal(i,j))
        print s
"""
