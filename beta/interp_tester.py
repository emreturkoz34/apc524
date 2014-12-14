import matrix
import lininterp
import numpy as np


def printMat(mat): 
	"Print contents of a Matrix object"
	for i in range(0, mat.GetNumRows()): 
		for j in range(0, mat.GetNumCols()): 
			print "%6.3f" % mat.GetVal(i, j),
		print ""

def printArr(data, len): 
	"Print contents of an array. data was a const double* in C++"
	for i in range(0, len):
		print "%6.3f" % data[i],
	print ""



# Set up a matrix object
rows = 7
cols = 10
mat = matrix.Matrix(rows, cols)
	
# Fill in the matrix with numbers
for i in range(0, rows):
	for j in range(0, cols):
		mat.SetVal(i, j, i*j + 1)
	
# Print the matrix
print "The matrix is: "
printMat(mat)
	
# Set up linear interpolator
linterp = lininterp.LinInterp()
icol = 1                          # interpolation column
ival = 3                          # interpolation value
vecout = np.zeros((cols))
# double *vecout = new double[cols] # interpolated row
# ABOVE LINE IS C++ ARRAY
	
# Make sure interpolation column is within bounds
if icol < 0 or icol >= cols:
	print "Interpolation failed: interpolation column out of bounds"
	exit()
	
# Perform linear interpolation
flag = linterp.Interp(mat, icol, ival, vecout)
if flag == 1:
	print "Interpolation failed: interpolation value out of bounds"
	exit()
	
# Print the interpolated row
print "Interpolating along column %i at %.3f:" % (icol, ival)
printArr(vecout, cols)
	
#	// Free memory
#	delete mat;
#	delete linterp;
#	delete[] vecout;
	
#	return 0;
