#!/usr/bin/env python
import numpy as np

import sys
sys.path.append('./mod')

import matrix
import monocheck
import linregression
import endpointslope

def printMat(mat): 
	"Print contents of a Matrix object"
	for i in range(0, mat.GetNumRows()): 
		for j in range(0, mat.GetNumCols()): 
			print "%6.3f" % mat.GetVal(i, j),
		print ""

#***Initialize test matrix progVar with sample progress variable values***
rows = 5 #Num rows in progVar
cols = 4 #Num cols in progVar
count = 0 #Variable used to populate progVar with values
progVar = matrix.Matrix(rows, cols); #Create Matrix object

for i in range(rows-1):
    for j in range(cols-1):
        progVar.SetVal(i, j, count)
        count += 1

for j in range(cols-1):
    progVar.SetVal(rows-1, j, 21.0)

for i in range(rows):
    progVar.SetVal(i, cols-1, count)
    count -= 5

#***Print out matrix progVar to ensure proper initialization of values***
print("Test matrix:\n")
printMat(progVar)

#***Initial monotonicity check***
checker = monocheck.MonoCheck(progVar) #Create MonoCheck object
monoAry = np.linspace(0, 0, cols)

assert checker.CheckStrictMonoticity(monoAry, cols, 0) == 0, "CheckStrictMonoticity ran unsuccessfully.\n" #Check which columns of progVar are strictly increasing or strictly decreasing and store result in monoAry

print("Strictly monotonic progress variables marked:\n")
for j in range(cols):
        print "%6.3f" % monoAry[j], #Print output array filled with 3s or 0s
print("\n")

#***Max slope testing commences***
monoAryCpy = np.linspace(0, 0, cols) #monoAryCpy is a copy of monoAry
for j in range(cols):
    monoAryCpy[j] = monoAry[j]

maxchecker = linregression.LinRegression(progVar) #Create LinRegression object
assert maxchecker.MostMonotonic(monoAry, cols, 0) == 0, "MostMonotonic ran unsuccessfully.\n" #Distinguish the best monotonic progress variables

print("Best C by linear regression method indicated:\n")
for j in range(cols):
        print "%6.3f" % monoAry[j], #Print output array filled with 3s, 2s, and 0s
print("\n")

maxchecker2 = endpointslope.EndPointSlope(progVar) #Create EndPointSlope object
assert maxchecker2.MostMonotonic(monoAryCpy, cols, 0) == 0, "MostMonotonic ran unsuccessfully.\n" #Distinguish the best monotonic progress variables

print("Best C by endpoint slope method indicated:\n")
for j in range(cols):
        print "%6.3f" % monoAryCpy[j], #Print output array filled with 3s, 2s, and 0s
print("\n")
