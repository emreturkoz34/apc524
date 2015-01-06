import numpy as np
import combinations as cs
import iofuncs as iof

import matrix
import sorting
import monocheck
import maxslope
import leastnonmono

def findC(datafiles, testspecies, bestC, options): 

    # Interpolate each datafile, generate a matrix from interpolated data
    nofiles = len(datafiles)
    nocols = len(testspecies)+1
    locs = np.zeros(nocols-1)
    interpdata = np.zeros((nofiles,nocols))
    filesmatrix = np.zeros((nofiles,3))
    for ii in range(nofiles): # interpolate for each file
        dataobj = iof.ProcFile(datafiles[ii])
        if ii == 0:
            titles = dataobj.gettitles() 
        else:
            titles1 = dataobj.gettitles()
            np.testing.assert_array_equal(titles1,titles) # Verify that all data files have the same column headers
        dataobj.interpolate(testspecies, locs, interpdata[ii,:], interpval=float(options["StoichMassFrac"][0]), interpmethod="".join(options["InterpMethod"]))
    filesmatrix[:,0] = interpdata[:,0]
    filesmatrix[:,2] = interpdata[:,0] # filesmatrix stores (row1) stoich prog var (row2) file indices (row3) stoich Temps
    filesmatrix[:,1] = range(nofiles)
    filesmatC = matrix.Matrix(nofiles,3)
    for i in range(nofiles):
        for j in range(3):
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
    sortmethod = options["sort method"][0]
    print "Sorting PROGVARS by temperature using %s sort" % sortmethod
    for i in [progVar, filesmatC]:
        if sortmethod  == 'bubble':
            sorter = sorting.bubble_sort(i)
        elif sortmethod == 'standard': # need to test
            sorter = sorting.standard_sort(i)
        elif sortmethod == 'brute':
            sorter = sorting.brute_sort(i)
        else:
            raise IOError("invalid sorting method (%s) specified, instead use <bubble> sort" % sortmethod)
        sorter.SetRefColNum(0)
        sorter.SetSortEndIndex(nofiles-1)
        sorter.SetSortStartIndex(0)
        sorter.generateIndexArray()
        sorter.extractRefCol()
        sorter.sort_data()
    print "Sorting FILESMATRIX by temperature"

    # Test monotonicity of PROGVARS
    print "Testing monotonicity \n"
    length = progvars.shape[1]
    monoAry = np.zeros(length, dtype=np.int32)

    checker = monocheck.MonoCheck(progVar) # Create MonoCheck object
    assert checker.CheckStrictMonoticity(monoAry, 0) == 0, "CheckStrictMonoticity ran unsuccessfully.\n" 
    # ^ Check which columns of progVar are strictly increasing or strictly decreasing and store result in monoAry

    # Test for maximum slope if multiple monotonic progress variables are returned
    checksum = np.sum(monoAry)
    if checksum % 3 != 0:
        raise RuntimeError("Incorrect values in monoAry vector, check monotonicity function.\n")
    if checksum > 3:
        maxslopetest = options["MaxSlopeTest"][0]
        print "Testing max slope using %s" % maxslopetest
        if maxslopetest == 'linear regression':
            maxchecker = maxslope.LinRegression(progVar)
        elif maxslopetest == 'end point slope':
            maxchecker = maxslope.EndPointSlope(progVar)
        else:
            raise IOError("invalid maximum slope test (%s) specified, instead use <linear regression>" % maxslopetest)
        assert maxchecker.MostMonotonic(monoAry, 0) == 0, "MostMonotonic ran unsuccessfully.\n" 
        # ^ Distinguish the best monotonic progress variables
    elif checksum == 0:
        # Least non-monotonic tests to be implemented in beta version
        print "Finding least non-monotonic progress variable"
        lnm_check = leastnonmono.SimpleLNM(progVar)
        assert lnm_check.LeastNonMonotonic(monoAry, 0) == 0, "LeastNonMonotonic ran unsuccessfully.\n"

    # Print results
    monoAryflag = 0 
    for i in range(length): 
        if monoAry[i] == 3.0: # Print best monotonic progress variable if it exists
            if monoAryflag != 0:
                raise RuntimeError("Error in contents of monoAry vector: multiple best selected.\n")
            monoAryflag = 2
            bestC[:] = iof.get_progvar(combosmatrix[1:,i], testspecies, locs, i)
            print 'The best strictly monotonic progress variable is C = %s' % bestC[1][0], 
            for j in bestC[1][1:]:
                print "+ %s" % j,
            print '\nThe column numbers of these species are ', bestC[0],', respectively.\n'
        elif monoAry[i] == 1.0: # Otherwise print least non-monotonic progress variable
            if monoAryflag != 0:
                raise RuntimeError("Error in contents of monoAry vector.\n")
            monoAryflag = 1
            bestC[:] = iof.get_progvar(combosmatrix[1:,i], testspecies, locs, i)
            print 'WARNING: no monotonic progress variables found, but proceeding with best alternative.\n'
            print 'The least non-monotonic progress variable is C = %s' % bestC[1][0], 
            for j in bestC[1][1:]: 
                print "+ %s" % j,
            print '\nThe column numbers of these species are', bestC[0],', respectively.\n'
    
    for i in range(length): # Print/identify other monotonic progress variables 
        if monoAry[i] == 2.0:
            if monoAryflag < 2:
                raise RuntimeError("Error in contents of monoAry vector.\n")
            elif monoAryflag == 2:
                print "Other candidate monotonic progress variables are:"
            otherC = iof.get_progvar(combosmatrix[1:,i], testspecies, locs, i)
            print 'C = %s' % otherC[1][0], 
            for j in otherC[1][1:]: 
                print "+ %s" % j,
            print "\n",
            monoAryflag = 3

    if monoAryflag < 1: # Give error if no best progress variable is found
        raise RuntimeError("Error: no best progress variable selected.")

    # Write results
    for i in range(nofiles):
        filesmatC.SetVal(i,0,progVar.GetVal(i,bestC[2]))
    return filesmatC
