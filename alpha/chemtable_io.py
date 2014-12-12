#!/usr/bin/env python

import numpy as np
import iofuncs as iof
import findprogvar as fpv

import vector
import matrix
import matrix3d
import matrix4d
import deltaPDF
import convolute
import trapz
import helper
import bubble_sort
import lininterp
import fittogrid

# read input file
fin1 = open('chemtable_inputs')
inputs = [line.strip().split('\t') for line in fin1]
datafiles = iof.read_input("data files:", inputs)
testspecies = iof.read_input("test species:", inputs, 0, ["Y-CO2","Y-CO","Y-H2O"])

# find best progress variable
bestC = []
nofiles = len(datafiles)
filesmatC = fpv.findC(datafiles, testspecies, bestC) # change so don't have to pre-initialize here

# sort FILESMATRIX by progress variable
sortmethod = iof.read_input("sort method:", inputs, default = 'bubble')
if "".join(sortmethod) == 'bubble': #only bubble sort supported for this version
    sorter = bubble_sort.bubble_sort(filesmatC)
sorter.SetRefColNum(0)
sorter.SetSortEndIndex(nofiles)
sorter.SetSortStartIndex(0)
sorter.generateIndexArray()
sorter.extractRefCol()
sorter.sort_data()
print "\nSorting filesmatrix by C"

# Calculate PDF matrix
    # Get user inputs
ZPy = np.genfromtxt(datafiles[0], unpack=False, skip_header=2, delimiter = "\t", usecols = 0)
Zmean_grid = iof.read_input("Zmean_grid:", inputs, minargs = 0, default = 'Z') # if no Z_grid is specified, Z and Zmean will be equivalent 
if "".join(Zmean_grid) == 'Z':
    ZmeanPy = ZPy
else:
    ZmeanPy = np.linspace(0,1,int(Zmean_grid[0]))
Zpdf = iof.read_input("Zpdf:", inputs)
if Zpdf[0] == "delta": # delta pdf has variance 0
    Zvar_grid = [1]
    Zvar_max = [0]
elif Zpdf[0] == "beta": # must include user specified variances for beta pdf # currently not supported
    Zvar_max = iof.read_input("Zvar_max:", inputs)
    Zvar_grid = iof.read_input("Zvar_grid:", inputs)
ZvarPy = np.linspace(0, float(Zvar_max[0]), int(Zvar_grid[0]))

    # Copy to C++ readable vectors
ZPoints = len(ZPy)
ZvarPoints = len(ZvarPy)
ZmeanPoints = len(ZmeanPy)
Z = vector.Vector(ZPoints)
Zmean = vector.Vector(ZmeanPoints)
Zvar = vector.Vector(ZvarPoints)
helper.copy_py_to_vector(ZPy, Z)
helper.copy_py_to_vector(ZmeanPy, Zmean)
helper.copy_py_to_vector(ZvarPy, Zvar)

    # generate PDF matrix
print "Generating PDF matrix"
pdfValM = matrix3d.Matrix3D(ZvarPoints, ZmeanPoints, ZPoints)
for i in range(ZvarPoints):
    for j in range(ZmeanPoints):
        for k in range(ZPoints):
            pdfValM.SetVal(i, j, k, 0)
d = deltaPDF.DeltaPDF(Z, ZPoints) # currently only supports delta pdf
pdfValReturn = d.pdfVal(Zvar, Zmean, pdfValM)

# Find locations of columns of reaction rate data for species in the best progress variable
dataobj = iof.ProcFile(datafiles[0])
titles = dataobj.gettitles()
rxn_rate_locs = range(len(bestC[0]))
for ii in range(len(rxn_rate_locs)):
    locflag = 0
    species = list(bestC[1][ii])
    speciesprodrate = species[2:]
    speciesprodrate = "".join(speciesprodrate)
    speciesprodrate = "".join(["ProdRate",speciesprodrate," [kg/m^3s]"])
    for jj in range(len(titles)):
        if titles[jj] == speciesprodrate:
            rxn_rate_locs[ii] = jj
            locflag = 1
    if locflag == 0:
        raise IOError("Production rate data for %s is missing" % speciesprodrate)

# Obtain relevant Yi and reaction rates from each file, and convolute
TrapzIntgr = trapz.Trapz(Z, ZPoints)
Conv = convolute.Convolute(ZPoints)
convolutedC = [0] * nofiles
convolutedST = [0] * nofiles

for kk in range(nofiles): ### future verisons: add loop over [C ST Y1 Y2 etc]
    file = datafiles[int(filesmatC.GetVal(kk,1))]
    massfracs = np.genfromtxt(file, unpack=False, skip_header=2, delimiter = "\t", usecols = bestC[0])
    rxnrates = np.genfromtxt(file, unpack=False, skip_header=2, delimiter = "\t", usecols = rxn_rate_locs)
    if  len(massfracs) != ZPoints:
        raise IOError("All file lengths must be the same")
    progvarsPy = np.zeros(ZPoints)
    sourcetermPy = np.zeros(ZPoints)
    progvar = vector.Vector(ZPoints)
    sourceterm = vector.Vector(ZPoints)
    for i in range(len(massfracs)):
        progvarsPy[i] = massfracs[i,:].sum()
        sourcetermPy[i] = rxnrates[i,:].sum()
    helper.copy_py_to_vector(progvarsPy,progvar)
    helper.copy_py_to_vector(sourcetermPy,sourceterm)
    convolutedC[kk] = matrix.Matrix(ZvarPoints, ZmeanPoints)
    convolutedST[kk] = matrix.Matrix(ZvarPoints, ZmeanPoints)
    ConvReturn = Conv.convVal(pdfValM, progvar, convolutedC[kk], TrapzIntgr)
    ConvReturn = Conv.convVal(pdfValM, sourceterm, convolutedST[kk], TrapzIntgr)
    #for i in range(ZvarPoints):
    #    for j in range(ZmeanPoints):
    #        print convolutedC[kk].GetVal(i,j),
print "Convolution completed"

# Run the fit to grid function to generate final data
    # Setup
dim1 = 2    # w~ and c~
dim2 = ZmeanPoints    # dimension of z~
dim3 = ZvarPoints    # dimension of z_v
dim4 = nofiles   # number of files
lcgrid = 10; # length of cgrid ######## Add user input
cgrid = np.linspace(0.0, 0.15, lcgrid)
interp = lininterp.LinInterp() # use linear interpolator ### add options for interpolator later
datain = matrix4d.Matrix4D(dim1, dim2, dim3, dim4)
dataout = matrix3d.Matrix3D(dim2, dim3, lcgrid)
print "Fitting final data to grid"
for i in range(2):
    for l in range(nofiles):
        for j in range(ZmeanPoints):
            for k in range(ZvarPoints):
                if i == 0:
                    datain.SetVal(i,j,k,l,convolutedST[l].GetVal(k,j))
                if i == 1:
                    datain.SetVal(i,j,k,l,convolutedC[l].GetVal(k,j))

# Run fit to grid and print results
f2gflag = fittogrid.fittogrid_func(datain, cgrid, interp, dataout)
if f2gflag == 1:
    print("WARNING: extrapolating to fit to cgrid")
FinalData = np.zeros((dim2, lcgrid))
for i in range(dim2):
    for j in range(lcgrid):
        FinalData[i,j] = dataout.GetVal(i,0,j)
print "\nFinal Data: \n", FinalData

del convolutedC
del convolutedST

# Contour plots will be used to visualize this data in the beta version

# Future functionality
    # command line changes to arguments

