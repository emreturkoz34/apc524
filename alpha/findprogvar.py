import numpy as np
import combinations as cs
import iofuncs as iof

def findC(datafiles, testspecies, bestC, filesmatrix): 

    # interpolate each datafile, generate a matrix from interpolated data
    nofiles = len(datafiles)
    nocols = len(testspecies)+1
    locs = np.zeros(nocols-1)
    interpdata = np.zeros((nofiles,nocols))

    for ii in range(nofiles):
        dataobj = iof.ProcFile(datafiles[ii])
        if ii == 0:
            titles = dataobj.gettitles() 
        else:
            titles1 = dataobj.gettitles()
            np.testing.assert_array_equal(titles1,titles) # verify that all data files have the same column headers
        dataobj.interpolate(testspecies, locs, interpdata[ii,:])
    filesmatrix[:,0] = interpdata[:,0]
    filesmatrix[:,1] = range(nofiles)

    # generate combinations matrix
    combosmatrix = np.zeros((nocols,cs.totnumcoms(nocols-1)+1))
    combosmatrix[0,0] = 1
    cs.combination_mat(combosmatrix[1:,1:])

    # calculate progress variables
    progvars = np.dot(interpdata,combosmatrix)

    # sort PROGVARS and FILESMATRIX by temperature
    # will add connectivity to C++ sort later
    print "sorting PROGVARS by temperature"
    print "sorting FILESMATRIX by temperature"

    # test monotonicity of PROGVARS
    # will add connectivity to C++ monotonicity check later
    print "testing monotonicity"
    length = progvars.shape[1]
    monocheck = np.zeros(length)
    monocheck[3] = 3 ###
    monocheck[4] = 3 ###
    checksum = monocheck.sum()
    if checksum % 3 != 0:
        raise RuntimeError("incorrect values in monocheck vector, check monotonicity function")
    if checksum > 3:
        # max slop tests in C++ to be connected
        print "testing max slope"
        monocheck[3] = 2 ###
    elif checksum == 0:
        # non monotonicity check in C++ to be connected
        print "finding least non-monotonic"
        monocheck[-1] = 1 ###

    # print results
    monocheckflag = 0

    for i in range(length): 
        if monocheck[i] == 3: # Find best monotonic progress variable if it exists
            if monocheckflag != 0:
                raise RuntimeError("error in contents of monocheck vector: multiple best selected")
            monocheckflag = 2
            bestC[:] = iof.get_progvar(combosmatrix[1:,i], testspecies, locs, i)
            print '\nThe best monotonically increasing progress variable is C = %s' % bestC[1][0], 
            for j in bestC[1][1:]:
                print "+ %s" % j
            print '\nThe column numbers of these species are', bestC[0],', respectively'

        elif monocheck[i] == 1: # otherwise find least non-monotonic progress variable
            if monocheckflag != 0:
                raise RuntimeError("error in contents of monocheck vector")
            monocheckflag = 1
            bestC[:] = iof.get_progvar(combosmatrix[1:,i], testspecies, locs, i)
            print '\nWARNING: no monotonic  progress variables found, but proceeding with best alternative'
            print 'The least non-monotonic progress variable is C = %s' % bestC[1][0], 
            for j in bestC[1][1:]: 
                print "+ %s" % j
            print '\nThe column numbers of these species are', bestC[0],', respectively'

    for i in range(length): # identify other monotonic progress variables 
        if monocheck[i] == 2:
            if monocheckflag < 2:
                raise RuntimeError("error in contents of monocheck vector")
            else:
                print "\nOther candidate monotonic progress variables are:"
            otherC = iof.get_progvar(combosmatrix[1:,i], testspecies, locs, i)
            print 'C = %s' % otherC[1][0], 
            for j in otherC[1][1:]: 
                print "+ %s" % j
            print "\n"
            monocheckflag = 3

    if monocheckflag < 1: # give error if no best progress variable is found
        raise RuntimeError("error: no best progress variable selected")

    # plot results
    iof.plotCvT(progvars[:,0],progvars[:,bestC[2]])

    # write results
    filesmatrix[:,0] = progvars[:,bestC[2]]
