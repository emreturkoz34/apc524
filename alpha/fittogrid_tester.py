import matrix
import matrix3d
import matrix4d
import numpy as np
import fittogrid
import lininterp

""" This program tests the fittogrid function. fittogrid takes a 4d matrix as input and
interpolates along a given cgrid. For clarity of presentation, in this case the 4d 
matrix will be 2-by-1-by-1-by-10, essentially a 2d matrix. The first row will be 10 
values of w~, and the second row will be 10 values of c~. fittogrid will interpolate 
to find values of w~ at values of c~ given by cgrid. """

# Set up inputs to fittogrid function
dim1 = 2;    # w~ and c~
dim2 = 1;    # dimension of z~
dim3 = 1;    # dimension of z_v
dim4 = 10;   # number of files
lcgrid = 10; # length of cgrid
datain = matrix4d.Matrix4D(dim1, dim2, dim3, dim4)
cgrid = np.zeros((lcgrid))
interp = lininterp.LinInterp() # use linear interpolator
dataout = matrix3d.Matrix3D(dim2, dim3, lcgrid)
	
# Fill datain with numbers
for i in range(0, dim4):
	datain.SetVal(0, 0, 0, i, i*i)
	datain.SetVal(1, 0, 0, i, i + 1)
	
# Fill cgrid with numbers
for i in range(0, lcgrid):
	cgrid[i] = 2.5 + i/2.0
	
# Print the input w~ and c~
dummy = "wc"
for i in range(0, 2):
	print "%c~ is:" % dummy[i]
	for j in range(0, dim4):
		print "%6.3f" % datain.GetVal(i, 0, 0, j),
	print ""

	
# Print cgrid
print "cgrid is:"
for i in range(0, lcgrid):
	print "%6.3f" % cgrid[i],
print ""
		
# Interpolate w~ along the cgrid
flag = fittogrid.fittogrid_func(datain, cgrid, interp, dataout)
if flag == 1:
	print "Interpolation failed: interpolation value out of bounds"
	exit()
	
# Print w~ values interpolated along cgrid
print "w~ inteprolated along cgrid is:"
for i in range(0, lcgrid):
	print "%6.3f " % dataout.GetVal(0, 0, i),
print ""
	
