#!/usr/bin/env python

import numpy as np

fin1 = open('chemtable_inputs')
inputs = [line.strip().split('\t') for line in fin1]

filesflag = 0
speciesflag = 0
for kk in range(len(inputs)):
    if inputs[kk][0] == "data files:":
        if len(inputs[kk]) < 2:
            raise IOError("must specify at least 1 datafile")
        if filesflag == 1:
            raise IOError("cannot specify data files on multiple lines")
        datafiles = inputs[kk][1:len(inputs[kk])]
        filesflag = 1
        print datafiles #####
    if inputs[kk][0] == "test species:":
        if len(inputs[kk]) < 2:
            raise IOError("must specify at least 1 species")
        if speciesflag == 1:
            raise IOError("cannot specify progress variable species on multiple lines")
        testspecies = inputs[kk][1:len(inputs[kk])]
        speciesflag = 1
        print testspecies #####
if filesflag == 0:
    raise IOError("data files not specified in input file, syntax is <datafile:\t file1\t file2\t ...>")
if speciesflag == 0: 
    raise IOError("species to be tested in progress variable calculations not specified in input file, syntax is <testspecies:\t species1\t species2\t ...>") 

sfile = datafiles[0]
inputvars = testspecies

fin = open(sfile)
l1 = fin.readline()
l2 = fin.readline()
titles = l2.strip().split('\t')
fin.close()

locations = range(len(inputvars)+2)
print locations #####
jj=2
for inputvar in inputvars:
    ii = 0
    flag = 0
    for title in titles:
        if title == inputvar:
            locations[jj] = ii
            flag = 1
        ii = ii+1
    if flag == 0:
        raise IOError("user specified column header %s not found in specified data file %s" % (inputvar, sfile))
    jj = jj+1
print locations ####

data = np.genfromtxt(sfile, unpack=False, skiprows=2, delimiter = "\t", usecols = locations)

print data #####

# test to see if all input data files are the same
