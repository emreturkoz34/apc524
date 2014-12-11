#!/usr/bin/env python

import numpy as np
import iofuncs as iof
import findprogvar as fpv

import matrix

# read input file
fin1 = open('chemtable_inputs')
inputs = [line.strip().split('\t') for line in fin1]
datafiles = iof.read_input("data files:", inputs)
testspecies = iof.read_input("test species:", inputs, 0, ["Y-CO2","Y-CO","Y-H2O"])

# find best progress variable
bestC = []
nofiles = len(datafiles)
filesmatrix = np.zeros((nofiles,2)) # define more generally
fpv.findC(datafiles, testspecies, bestC, filesmatrix)
print filesmatrix
print bestC

# sort FILESMATRIX by progress variable
# will add connectivity to C++ sort later
print "sorting FILESMATRIX by C"

# Calculate PDF matrix
Z_grid = iof.read_input("Z_grid:", inputs, default = 'Zmean') # if no Z_grid is specified, Z and Zmean will be equivalent 
Zvar_max = iof.read_input("Zvar_max:", inputs)
Zvar_grid = iof.read_input("Zvar_grid:", inputs)
Zpdf = iof.read_input("Zpdf:", inputs)

ZvarPy = np.linspace(0, float(Zvar_max[0]), int(Zvar_grid[0]))
ZmeanPy = np.genfromtxt(datafiles[0], unpack=False, skiprows=2, delimiter = "\t", usecols = 0)
if "".join(Z_grid) == 'Zmean':
    ZPy = ZmeanPy
else:
    ZPy = np.linspace(0,1,int(Z_grid[0]))

# call C++ function to generate PDFmatrix (inputs: Zvar, Zmean, Zpdf)

# find locations of columns of reaction rate data for species in the best progress variable
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

# obtain relevant Yi and reaction rates from each file
for kk in filesmatrix[:,1]:
    file = datafiles[int(kk)]
    massfracs = np.genfromtxt(file, unpack=False, skiprows=2, delimiter = "\t", usecols = bestC[0])
    rxnrates = np.genfromtxt(file, unpack=False, skiprows=2, delimiter = "\t", usecols = rxn_rate_locs)
    # data will be extracted from this file and sent to the C++ function Convolute

# Then, the C++ function FitToGrid will be called to generate the final output data
# Contour plots will be used to visualize this data

# Future functionality
    # command line changes to arguments

