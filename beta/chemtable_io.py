#!/usr/bin/env python

import sys
sys.path.append('./mod')
sys.path.append('./python')

import numpy as np
import iofuncs as iof
import findprogvar as fpv
import glob
import os

import matrix
import matrix3d
import matrix4d
import pdf
import integrator
import sorting
import interpolator
import fittogrid
import convolute
import matplotlib.pyplot as plt
import matplotlib.cm as cm

## @package chemtable_io
# Executable Python script for chemtable generation, including calling findprogvar 
# to determine the best progress variable 
#
# Inputs:
# - chemtable_inputs: text file containing user options. Each option is written on it's 
# own line, and if multiple values are required they should be seperated by tabs. Details 
# of the chemtable_inputs file and it's required contents can be found in the README.
# -  .kg (FlameMaster output) data files: in a directory specified by the user in chemtable_inputs.
# All files must be unique. 
#
# Outputs:
# - /output/textfile (name specified by user in chemtable_inputs): 
# 4 columns of data, representing Cmean, Zmean, Zvar, and the Chemical Source Term
# - /output/contour_zvar_XXX.pdf *10: 10 contour plots of chemical source term vs. Zmean and Cmean
# at the values of Zvar specified in the filenames. If the user specifies taht less than 10 values
# of Zvar should be calculated, then that number of contour plots is generates
# - /output/CvsTemp.pdf: plot of the best progress variable (and others if the user desries) vs. 
# Temperature
#
# Note: this Python script relies on C++ functions connected through SWIG, which must generate the 
# following modules:
# - matrix, matrix3D, matrix4D
# - pdf
# - integrator
# - convolute
# - sorting
# - interpolator
# - fittogrid


# Create directory for outputs if one does not alreayd exist
try:
    os.stat('output')
except:
    os.mkdir('output')

# read input file
print " "
fin1 = open('chemtable_inputs')
inputs = [line.strip().split('\t') for line in fin1]
datafiledir = iof.read_input("data file directory:", inputs, default=['data'])
datafiles = glob.glob("".join(["".join(datafiledir), "/*.kg"])) #vector of paths of all files in specified directory
testspecies = iof.read_input("test species:", inputs, minargs=0, default=["Y-CO2","Y-CO","Y-H2O"])
options = {} #dictionary stores options
options["sort method"] = iof.read_input("sort method:", inputs, default = ['bubble'])
options["Zpdf"] = iof.read_input("Zpdf:", inputs)
options["Zmean grid"] = iof.read_input("Zmean_grid:", inputs, minargs = 0, default = ['Z'])
options["StoichMassFrac"] = iof.read_input("StoichMassFrac:", inputs, minargs=0, default=[0.055])
options["InterpMethod"] = iof.read_input("interp method:", inputs, minargs=0, default=['linear'])
options["MaxSlopeTest"] = iof.read_input("max slope test:", inputs, minargs=0, default=['linear regression'])
options["Integrator"] = iof.read_input("integrator:", inputs, minargs=0, default=['trapezoid'])
options["LCgrid"] = iof.read_input("length Cgrid:", inputs, minargs=0, default=[20])
options["OutputFile"] = iof.read_input("output file name:", inputs, minargs=0, default=['data_output'])
options["PlotAllC"] = iof.read_input("plot all progress variables:", inputs, minargs=0, default=['yes'])
options["SkipProgVar"] = iof.read_input("skip progress variable optimization:", inputs, minargs=0, default=['no'])
options["nothreads"] = iof.read_input("number of threads:", inputs, minargs=0, default=[1])
options["lnmcheck"] = iof.read_input("least nonmonotonic check:", inputs, minargs=0, default=['simple'])

# find best progress variable
bestC = []
nofiles = len(datafiles)  # Check to see if used later and maybe move
filesmatC = fpv.findC(datafiles, testspecies, bestC, options)

# sort FILESMATRIX by progress variable
if options["sort method"][0] == 'bubble':
    sorter = sorting.bubble_sort(filesmatC)
elif options["sort method"][0] == 'standard':
    sorter = sorting.standard_sort(filesmatC)
elif options["sort method"][0] == 'brute': # has speed issues
    sorter = sorting.brute_sort(filesmatC)
else:
    raise IOError("invalid sorting method (%s) specified, instead use <bubble> sort" % sortmethod)
sorter.SetRefColNum(0)
sorter.sort_data()
print "\nSorting filesmatrix by C using %s sort" % options["sort method"][0]

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
integ = options["Integrator"][0]
if integ == 'trapezoid':
    Intgr = integrator.Trapz()
elif integ == 'simpson':
    Intgr = integrator.Simpson()
elif integ == 'glquad':
    NumberNodes = iof.read_input("glq Number of Nodes:", inputs, minargs=0, default=[50])
    Intgr = integrator.GLQuad(int(NumberNodes[0]))
else:
    raise IOError("inavlid integrator type (%s) specified, instead use <trapezoid>, <simpson>, or <glquad>" % integ)
print "Convoluting using %s integration" % integ
convolutedC = [0] * nofiles
convolutedST = [0] * nofiles

maxC = 0
maxRate = 0
for kk in range(nofiles): ### future verisons: add loop over [C ST Y1 Y2 etc]
    file = datafiles[int(filesmatC.GetVal(kk,1))]
    massfracs = np.genfromtxt(file, unpack=False, skip_header=2, delimiter = "\t", usecols = bestC[0])
    rxnrates = np.genfromtxt(file, unpack=False, skip_header=2, delimiter = "\t", usecols = rxn_rate_locs)
    if  len(massfracs) != ZPoints:
        raise IOError("All file lengths must be the same, file %s does not match" % file)
    progvar = np.zeros(ZPoints)
    rxnRates = np.zeros(ZPoints)
    if len(bestC[0]) == 1:
        progvar[:] = massfracs[:]
        rxnRates[:] = rxnrates[:]
    else:
        for i in range(len(massfracs)):
            progvar[i] = massfracs[i,:].sum()
            rxnRates[i] = rxnrates[i,:].sum()
    if progvar.max() > maxC:
        maxC = progvar.max()
    if rxnRates.max() > maxRate:
        maxRate = rxnRates.max()
    convolutedC[kk] = matrix.Matrix(ZvarPoints, ZmeanPoints)
    convolutedST[kk] = matrix.Matrix(ZvarPoints, ZmeanPoints)
    ConvReturn =  convolute.convVal_func(Z, progvar, pdfValM, convolutedC[kk], Intgr)
    ConvReturn =  convolute.convVal_func(Z, rxnRates, pdfValM, convolutedST[kk], Intgr)
print "Convolution completed"
print "Maximum value of progress variable is:", maxC

# Run the fit to grid function to generate final data
    # Setup
dim1 = 2    # w~ and c~
dim2 = ZmeanPoints    # dimension of z~
dim3 = ZvarPoints    # dimension of z_v
dim4 = nofiles   # number of files
lcgrid = int(options["LCgrid"][0]); # length of cgrid 
cgrid = np.linspace(0.0, maxC*1.5, lcgrid)
interpmethod = options["InterpMethod"][0] 
if interpmethod == 'linear': # add more interpolation options later
    interp = interpolator.LinInterp()
elif interpmethod == 'hermite':
    interp = interpolator.HermiteInterp()
elif interpmethod == 'cubic':
    interp = interpolator.CubicInterp()
else:
    raise IOError("Specified interpolation method: %s not supported, use <linear>" % interpmethod)
datain = matrix4d.Matrix4D(dim1, dim2, dim3, dim4)
dataout = matrix3d.Matrix3D(dim2, dim3, lcgrid)
print "Fitting final data to grid using %s interpolation" % interpmethod
for i in range(2):
    for l in range(nofiles):
        for j in range(ZmeanPoints):
            for k in range(ZvarPoints):
                if i == 0:
                    datain.SetVal(i,j,k,l,convolutedST[l].GetVal(k,j))
                if i == 1:
                    datain.SetVal(i,j,k,l,convolutedC[l].GetVal(k,j))

# Run fit to grid and print results
f2gflag = fittogrid.fittogrid_func(datain, cgrid, interp, dataout, int(options["nothreads"][0]))
if f2gflag == 1:
    print("WARNING: extrapolating to fit to cgrid")
FinalData = np.zeros((lcgrid, dim2, dim3))
f = open("".join(["output/",options["OutputFile"][0]]),'w')
f.write('C        \tZmean      \tZvar      \tSourceTerm \n')
for j in range(lcgrid):
    for i in range(dim2):
        for k in range(dim3):
            FinalData[j,i,k] = dataout.GetVal(i,k,j)
            f.write('%8.5g\t %8.5g\t %8.5g\t %g\n' % (cgrid[j], Zmean[i], Zvar[k], FinalData[j,i,k]))
f.close()
print "\nFinal data written to file: output/%s" % options["OutputFile"][0]

# Create contour plots of the chemical source term
noplots = 10
if ZvarPoints > (noplots + 1):
    plots = range(noplots)
    noplots = 10
elif ZvarPoints > 1:
    plots = range(ZvarPoints - 2)
    noplots = ZvarPoints - 2
else:
    plots = [-1]
    noplots = 1
for j in plots: 
    i = int((j+1)*ZvarPoints/(noplots+2))
    X, Y = np.meshgrid(Zmean, cgrid)
    plt.figure()
    levels=np.linspace(-1, maxRate, 50)
    CS = plt.contourf(X, Y, FinalData[:,:,i], levels)
    plt.title('Source term (kg/m^3-s) vs. Zmean and C for Zvar = %5.3g' % Zvar[i])
    plt.xlabel('Zmean')
    plt.ylabel('C')
    grid = pow(10,np.floor(np.log10(maxRate))-1) * np.ceil(maxRate / pow(10,np.floor(np.log10(maxRate))))
    plt.colorbar(CS, ticks=np.arange(0,maxRate,grid))
    plt.savefig('output/contour_zvar_%.3g.pdf' % Zvar[i])
print "%d contour plots created in output directory \n" % noplots

