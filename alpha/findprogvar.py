import numpy as np
import combinations as cs
import iofuncs as iof

import matrix
import bubble_sort

import vector
import monocheck
import linregression
import endpointslope
import helper

def findC(datafiles, testspecies, bestC): 

    # Interpolate each datafile, generate a matrix from interpolated data
    nofiles = len(datafiles)
    nocols = len(testspecies)+1
    locs = np.zeros(nocols-1)
    interpdata = np.zeros((nofiles,nocols))
    filesmatrix = np.zeros((nofiles,2))

    for ii in range(nofiles):
        dataobj = iof.ProcFile(datafiles[ii])
        if ii == 0:
            titles = dataobj.gettitles() 
        else:
            titles1 = dataobj.gettitles()
            np.testing.assert_array_equal(titles1,titles) # Verify that all data files have the same column headers
        dataobj.interpolate(testspecies, locs, interpdata[ii,:])
    filesmatrix[:,0] = interpdata[:,0]
    filesmatrix[:,1] = range(nofiles)
    filesmatC = matrix.Matrix(nofiles,2)
    for i in range(nofiles):
        for j in range(2):
            filesmatC.SetVal(i,j,filesmatrix[i,j])

    # Generate combinations matrix
    combosmatrix = np.zeros((nocols,cs.totnumcoms(nocols-1)+1))
    combosmatrix[0,0] = 1
    cs.combination_mat(combosmatrix[1:,1:])

    # Calculate progress variables
    progvars = np.dot(interpdata,combosmatrix)

    # Generate progress variable matrix
    progVar = matrix.Matrix(nofiles, cs.totnumcoms(nocols-1)+1) 
    for i in range (nofiles):
        for j in range(cs.totnumcoms(nocols-1)+1):
            progVar.SetVal(i,j,progvars[i,j])

    # Sort PROGVARS and FILESMATRIX by temperature
    print "Sorting PROGVARS by temperature:\n"
    sortmethod = 'bubble'
    if "".join(sortmethod) == 'bubble':
        sorter = bubble_sort.bubble_sort(progVar)
    sorter.SetRefColNum(0)
    sorter.SetSortEndIndex(nofiles)
    sorter.SetSortStartIndex(0)
    sorter.generateIndexArray()
    sorter.extractRefCol()
    sorter.sort_data()


    print "Sorting FILESMATRIX by temperature:\n"
    sortmethod = 'bubble'
    if "".join(sortmethod) == 'bubble':
        sorter = bubble_sort.bubble_sort(filesmatC)
    sorter.SetRefColNum(0)
    sorter.SetSortEndIndex(nofiles)
    sorter.SetSortStartIndex(0)
    sorter.generateIndexArray()
    sorter.extractRefCol()
    sorter.sort_data()

    # Test monotonicity of PROGVARS
    print "Testing monotonicity:\n"
    length = progvars.shape[1]
    monoAryPy = np.zeros(length)
    monoAry = vector.Vector(length)
    helper.copy_py_to_vector(monoAryPy, monoAry)

    checker = monocheck.MonoCheck(progVar) # Create MonoCheck object
    assert checker.CheckStrictMonoticity(0, monoAry) == 0, "CheckStrictMonoticity ran unsuccessfully.\n" # Check which columns of progVar are strictly increasing or strictly decreasing and store result in monoAry

    checksum = 0
    for i in range(length):
        checksum += monoAry.GetVal(i)

    if checksum % 3 != 0:
        raise RuntimeError("Incorrect values in monoAry vector, check monotonicity function.\n")
    if checksum > 3:
        print "Testing max slope:"
        maxchecker = linregression.LinRegression(progVar)
        #maxchecker = endpointslope.EndPointSlope(progVar)
        assert maxchecker.MostMonotonic(0, monoAry) == 0, "MostMonotonic ran unsuccessfully.\n" # Distinguish the best monotonic progress variables
    elif checksum == 0:
        # Least non-monotonic tests to be implemented in beta version
        print "Finding least non-monotonic:"
        monoAry[0] = 1

    # Print results
    monoAryflag = 0 
    for i in range(length): 
        if monoAry.GetVal(i) == 3.0: # Find best monotonic progress variable if it exists
            if monoAryflag != 0:
                raise RuntimeError("Error in contents of monoAry vector: multiple best selected.\n")
            monoAryflag = 2
            bestC[:] = iof.get_progvar(combosmatrix[1:,i], testspecies, locs, i)
            print 'The best strictly monotonic progress variable is C = %s' % bestC[1][0], 
            for j in bestC[1][1:]:
                print "+ %s" % j
            print '\nThe column numbers of these species are ', bestC[0],', respectively.\n'
        elif monoAry.GetVal(i) == 1.0: # Otherwise find least non-monotonic progress variable
            if monoAryflag != 0:
                raise RuntimeError("Error in contents of monoAry vector.\n")
            monoAryflag = 1
            bestC[:] = iof.get_progvar(combosmatrix[1:,i], testspecies, locs, i)
            print 'WARNING: no monotonic progress variables found, but proceeding with best alternative.\n'
            print 'The least non-monotonic progress variable is C = %s' % bestC[1][0], 
            for j in bestC[1][1:]: 
                print "+ %s" % j
            print '\nThe column numbers of these species are', bestC[0],', respectively.\n'
    for i in range(length): # Identify other monotonic progress variables 
        if monoAry.GetVal(i) == 2.0:
            if monoAryflag < 2:
                raise RuntimeError("Error in contents of monoAry vector.\n")
            else:
                print "Other candidate monotonic progress variables are:"
            otherC = iof.get_progvar(combosmatrix[1:,i], testspecies, locs, i)
            print 'C = %s' % otherC[1][0], 
            for j in otherC[1][1:]: 
                print "+ %s" % j,
            print "\n"
            monoAryflag = 3

    if monoAryflag < 1: # Give error if no best progress variable is found
        raise RuntimeError("Error: no best progress variable selected.")

    # Plot results
    iof.plotCvT(progvars[:,0],progvars[:,bestC[2]])

    # Write results
    for i in range(nofiles):
        filesmatC.SetVal(i,0,progvars[i,bestC[2]])
    return filesmatC
