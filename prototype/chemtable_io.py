#!/usr/bin/env python

import numpy as np
import iofuncs as iof
import findprogvar as fpv

# read input file
fin1 = open('chemtable_inputs')
inputs = [line.strip().split('\t') for line in fin1]
datafiles = iof.read_input("data files:", inputs)
testspecies = iof.read_input("test species:", inputs, 0)
if testspecies == []: # add default value
    testspecies = ["Y-CO2","Y-CO","Y-H2O"]
    print "WARNING: no species specified, using Y-CO2, Y-CO, Y-H2O"

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
Zvar_max = iof.read_input("Zvar_max:", inputs)
Zvar_grid = iof.read_input("Zvar_grid:", inputs)
Zpdf = iof.read_input("Zvar_grid:", inputs)

Zvar = np.linspace(0, float(Zvar_max[0]), int(Zvar_grid[0]))
Zmean = np.genfromtxt(datafiles[0], unpack=False, skiprows=2, delimiter = "\t", usecols = 0)
# call C++ function to generate PDFmatrix (inputs: Zvar, Zmean, Zpdf)

# obtain relevant Yi and reaction rates from each file
for kk in filesmatrix[:,1]:
    file = datafiles[int(kk)]
    # data will be extracted from this file and sent to the C++ function Convolute

# Then, the C++ function FitToGrid will be called to generate the final output data
# Contour plots will be used to visualize this data

# Future functionality
    # command line changes to arguments
    # make possibility of default settings general

