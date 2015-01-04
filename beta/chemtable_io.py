#!/usr/bin/env python

import sys
sys.path.append('./mod')
sys.path.append('./python')

import numpy as np
import iofuncs as iof
import findprogvar as fpv
import glob

import matrix
import matrix3d
import matrix4d
import pdf
import integrator
import sorting
import lininterp
import fittogrid
import convolute

# read input file
print " "
fin1 = open('chemtable_inputs')
inputs = [line.strip().split('\t') for line in fin1]
datafiledir = iof.read_input("data file directory:", inputs)
datafiles = glob.glob("".join(["".join(datafiledir), "/*.kg"])) #vector of paths of all files in specified directory
testspecies = iof.read_input("test species:", inputs, minargs=0, default=["Y-CO2","Y-CO","Y-H2O"])
options = {} #dictionary stores options
options["sort method"] = iof.read_input("sort method:", inputs, default = 'bubble')
options["Zpdf"] = iof.read_input("Zpdf:", inputs)
options["Zmean grid"] = iof.read_input("Zmean_grid:", inputs, minargs = 0, default = 'Z')
options["StoichMassFrac"] = iof.read_input("StoichMassFrac:", inputs, minargs=0, default=[0.055])

# find best progress variable
bestC = []
nofiles = len(datafiles)  # Check to see if used later and maybe move
filesmatC = fpv.findC(datafiles, testspecies, bestC)

# sort FILESMATRIX by progress variable
if options["sort method"][0] == 'bubble': #only bubble sort supported for this version
    sorter = sorting.bubble_sort(filesmatC)
sorter.SetRefColNum(0)
sorter.SetSortEndIndex(nofiles)
sorter.SetSortStartIndex(0)
sorter.generateIndexArray()
sorter.extractRefCol()
sorter.sort_data()
print "\nSorting filesmatrix by C using %s sort" % options["sort method"][0]

# Plot sorted stoich progress variable vs. stoich temperature
Cst = [0] * nofiles
Tst = [0] * nofiles
for ii in range(nofiles):
    Cst[ii] = filesmatC.GetVal(ii,0)
    Tst[ii] = filesmatC.GetVal(ii,2)
iof.plotCvT(Tst,Cst)

# Calculate PDF matrix
    # Get user inputs
Z = np.genfromtxt(datafiles[0], unpack=False, skip_header=2, delimiter = "\t", usecols = 0)
# if no Z_grid is specified, Z and Zmean will be equivalent 
if options["Zmean grid"][0] == 'Z':
    Zmean = Z
else:
    Zmean = np.linspace(0,1,int(options["Zmean grid"][0]))
Zpdf = options["Zpdf"]

    # Generate pdf objects
print "Generating PDF matrix with", Zpdf[0], "PDF"
if Zpdf[0] == "delta": # delta pdf has variance 0
    Zvar_grid = [1]
    Zvar_max = [0]
    Zvar = np.linspace(0, float(Zvar_max[0]), int(Zvar_grid[0]))
    d = pdf.DeltaPDF(Zmean) 
elif Zpdf[0] == "beta": # must include user specified variances for beta pdf # currently not supported
    Zvar_max = iof.read_input("Zvar_max:", inputs)
    Zvar_grid = iof.read_input("Zvar_grid:", inputs)
    Zvar = np.linspace(0, float(Zvar_max[0]), int(Zvar_grid[0]))
    d = pdf.BetaPDF(Zmean, Zvar)
else:
    raise IOError("Incorrect PDF input %s, currently only DELTA and BETA are supported" % Zpdf[0])

    # generate PDF matrix
ZPoints = len(Z)          
ZvarPoints = len(Zvar)
ZmeanPoints = len(Zmean)
pdfValM = matrix3d.Matrix3D(ZvarPoints, ZmeanPoints, ZPoints)
for i in range(ZvarPoints):
    for j in range(ZmeanPoints):
        for k in range(ZPoints):
            pdfValM.SetVal(i, j, k, 0)
pdfValReturn = d.pdfVal(Z, pdfValM)
print "PDF calculated"


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
TrapzIntgr = integrator.Trapz()
convolutedC = [0] * nofiles
convolutedST = [0] * nofiles

for kk in range(nofiles): ### future verisons: add loop over [C ST Y1 Y2 etc]
    file = datafiles[int(filesmatC.GetVal(kk,1))]
    massfracs = np.genfromtxt(file, unpack=False, skip_header=2, delimiter = "\t", usecols = bestC[0])
    rxnrates = np.genfromtxt(file, unpack=False, skip_header=2, delimiter = "\t", usecols = rxn_rate_locs)
    if  len(massfracs) != ZPoints:
        raise IOError("All file lengths must be the same")
    progvar = np.zeros(ZPoints)
    rxnRates = np.zeros(ZPoints)
    for i in range(len(massfracs)):
        progvar[i] = massfracs[i,:].sum()
        rxnRates[i] = rxnrates[i,:].sum()
    convolutedC[kk] = matrix.Matrix(ZvarPoints, ZmeanPoints)
    convolutedST[kk] = matrix.Matrix(ZvarPoints, ZmeanPoints)
    ConvReturn =  convolute.convVal_func(Z, progvar, pdfValM, convolutedC[kk], TrapzIntgr)
    ConvReturn =  convolute.convVal_func(Z, rxnRates, pdfValM, convolutedST[kk], TrapzIntgr)
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
print "\nFinal Data: \n", FinalData, "\n "

del convolutedC
del convolutedST

# Contour plots will be used to visualize this data in the beta version

# Future functionality
    # command line changes to arguments

