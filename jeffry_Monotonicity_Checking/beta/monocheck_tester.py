#!/usr/bin/env python
import numpy as np

import sys
sys.path.append('./mod')

import matrix
import monocheck
import maxslope
import leastnonmono

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
monoAry = np.zeros(cols, dtype=np.int32)

assert checker.CheckStrictMonoticity(monoAry, 0) == 0, "CheckStrictMonoticity ran unsuccessfully.\n" #Check which columns of progVar are strictly increasing or strictly decreasing and store result in monoAry

print("Strictly monotonic progress variables marked:\n")
for j in range(cols):
        print "%6.3f" % monoAry[j], #Print output array filled with 3s or 0s
print("\n")

#***Max slope testing commences***
monoAryCpy = np.zeros(cols, dtype=np.int32) #monoAryCpy is a copy of monoAry
for j in range(cols):
    monoAryCpy[j] = monoAry[j]

maxchecker = maxslope.LinRegression(progVar) #Create LinRegression object
assert maxchecker.MostMonotonic(monoAry, 0) == 0, "MostMonotonic ran unsuccessfully.\n" #Distinguish the best monotonic progress variables

print("Best C by linear regression method indicated:\n")
for j in range(cols):
        print "%6.3f" % monoAry[j], #Print output array filled with 3s, 2s, and 0s
print("\n")

maxchecker2 = maxslope.EndPointSlope(progVar) #Create EndPointSlope object
assert maxchecker2.MostMonotonic(monoAryCpy, 0) == 0, "MostMonotonic ran unsuccessfully.\n" #Distinguish the best monotonic progress variables

print("Best C by endpoint slope method indicated:\n")
for j in range(cols):
        print "%6.3f" % monoAryCpy[j], #Print output array filled with 3s, 2s, and 0s
print("\n")

##########################################################
# Testing for least non-monotonic progress variable begins
##########################################################

#***Initialize test matrix progVar2 with non-monotonic progress variable values***
progVar2 = matrix.Matrix(rows, cols); #Create Matrix object

# Set column 0 (Reference column)
progVar2.SetVal(0, 0, 0.0);
progVar2.SetVal(1, 0, 1.0);
progVar2.SetVal(2, 0, 2.0);
progVar2.SetVal(3, 0, 3.0);
progVar2.SetVal(4, 0, 4.0);

# Set column 1 (progress variable 1)
progVar2.SetVal(0, 1, 5.0);
progVar2.SetVal(1, 1, 4.0);
progVar2.SetVal(2, 1, 2.0);
progVar2.SetVal(3, 1, 3.0);
progVar2.SetVal(4, 1, 5.0);

# Set column 2 (progress variable 2)
progVar2.SetVal(0, 2, 1.0);
progVar2.SetVal(1, 2, 2.0);
progVar2.SetVal(2, 2, 3.0);
progVar2.SetVal(3, 2, 4.0);
progVar2.SetVal(4, 2, 3.0);

# Set column 3 (progress variable 3)
progVar2.SetVal(0, 3, 6.0);
progVar2.SetVal(1, 3, 7.0);
progVar2.SetVal(2, 3, 5.0);
progVar2.SetVal(3, 3, 3.0);
progVar2.SetVal(4, 3, 4.0);

#***Print out matrix progVar2 to ensure proper initialization of values***
print("Test matrix:\n")
printMat(progVar2)

#***Initial monotonicity check***
checker2 = monocheck.MonoCheck(progVar2) #Create MonoCheck object
monoAry2 = np.zeros(cols, dtype=np.int32)

assert checker2.CheckStrictMonoticity(monoAry2, 0) == 0, "CheckStrictMonoticity ran unsuccessfully.\n" #Check which columns of progVar2 are strictly increasing or strictly decreasing and store result in monoAry2

print("Strictly monotonic progress variables marked:\n")
for j in range(cols):
        print "%6.3f" % monoAry2[j], #Print output array filled with 0s
print("\n")

#***Least non-monotonic testing commences***
monoAryCpy2 = np.zeros(cols, dtype=np.int32) #monoAryCpy is a copy of monoAry2
for j in range(cols):
    monoAryCpy2[j] = monoAry2[j]

lnmchecker = leastnonmono.SimpleLNM(progVar2) #Create SimpleLNM object
assert lnmchecker.LeastNonMonotonic(monoAry2, 0) == 0, "LeastNonMonotonic ran unsuccessfully.\n" #Distinguish the least non-monotonic progress variable

print("Best C by simple least non-monotonic method indicated:\n")
for j in range(cols):
        print "%6.3f" % monoAry2[j], #Print output array filled with 0s and one 1
print("\n")

#lnmchecker2 = leastnonmono.AdvancedLNM(progVar2) #Create AdvancedLNM object
#assert lnmchecker2.LeastNonMonotonic(monoAryCpy2, 0) == 0, "LeastNonMonotonic ran unsuccessfully.\n" #Distinguish the least non-monotonic progress variable

#print("Best C by advanced least non-monotonic method indicated:\n")
#for j in range(cols):
#        print "%6.3f" % monoAryCpy2[j], #Print output array filled with 0s and one 1
#print("\n")
