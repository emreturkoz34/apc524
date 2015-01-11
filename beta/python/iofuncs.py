import numpy as np
import matrix
import lininterp

## @package iofuncs
# Module containing text file processing functions used by other python scripts 

## Function that extracts input options from a text file
#
# Searches for a row in the text file beginning with the string specified by INPUTNAME. 
# Raises an error if this string appears on multiple lines.
#
# Writes the rest of that line (delimited by tabs) as a vector of strings into INPUTSARRAY.
#
# Raises an error if fewer than MINARGS tab delimited elements are found on the input line.
#
# If INPUTNAME is not found, writes returns DEFAULT to INPUTSARRAY, otherwise raises an error.
def read_input(inputname, inputsarray, minargs = 1, default = None):
    flag = 0
    readinput = []
    for kk in range(len(inputsarray)):
        if inputsarray[kk][0] == inputname:
            if len(inputsarray[kk]) < minargs + 1:
                raise IOError("must specify at least %d input values for %s" % (minargs,inputname))
            if flag == 1:
                raise IOError("cannot specify input %s on multiple lines" % inputname)
            readinput = inputsarray[kk][1:len(inputsarray[kk])]
            flag = 1
    if (flag == 0) | (readinput == []):
        if default != None:
            readinput[:] = default[:]
            print "using default input for %s" % inputname
            print default
        else:
            raise IOError("input %s not specified in input file and no default given, syntax is <%s\t file1\t file2\t ...>" % (inputname, inputname))
    return readinput

## Function that creates a vector containing information about a progress variable
#
# returns [progvarlocsFULL, progvarnames, index]
#
# progvarnames: strings of species for a given PROGVARVEC, eg [0, 1, 0, 0, 1] --> ['Y-CH4', 'Y-O2'] 
# for TESTSPECIES = ['Y-CO', 'Y-CH4', 'Y-H2', 'Y-CO2', 'Y-O2']
#
# progvarlocsFull: a vector containing all elements of LOCS corresponding to non-zero elements of PROGVARVEC,
# eg [2, 5] for LOCS = [1 2 3 4 5] in the above example.
#
# index: INDEX unchanged
def get_progvar(progvarvec, testspecies, locs, index = 1):
    progvarlocsFULL = [] #column indices of species in full data file
    progvarnames = [] #species names (strings)
    for j in range(len(progvarvec)):
        if progvarvec[j] == 1:
            progvarlocsFULL.append(int(locs[j]))
            progvarnames.append(testspecies[j])
    return [progvarlocsFULL, progvarnames, index]

class ProcFile(object):
    """Class for processing .kg datafiles, including extracting column headers and interpolating a row of data."""

    ## The Constructor
    #
    # SFILE: a string contiaining the name of the data file to be processed or path to that file
    def __init__(self, sfile):
        self._sfile = sfile

    ## Function that returns a vector containing the column headers in the 2nd row of the data file
    #
    # Ignores 1st row, returns contents of 2nd row as elements of a vector (assuming datafile is tab delimited).
    def gettitles(self):
        fin = open(self._sfile)
        l1 = fin.readline()
        l2 = fin.readline()
        titles = l2.strip().split('\t')
        fin.close()
        return titles

    ## Interpolate function extracts/interpolates a row of data in the data file at 
    # the specified value in the first column
    #
    # Read the columns of the data file with headers matching the strings in the INPUTVARS vector.
    #
    # Write the column numbers corresponding to these column headers into LOCS vector.
    #
    # Interpolate to find values of each column corresponding to INTERPVAL in the 1st column, 
    # using interpolation method specified by the INTERPMETHOD string.
    # 
    # Write interpolated values to DATAVEC.
    def interpolate(self, inputvars, locs, datavec, interpval = 0.27, interpmethod = 'linear'):
        
        locations = range(len(inputvars)+2)
        jj=2
        
        # search for the column locations of the desired variables
        for inputvar in inputvars: 
            ii = 0
            flag = 0
            for title in self.gettitles():
                if title == inputvar:
                    locations[jj] = ii
                    flag = 1
                ii = ii+1
            if flag == 0:
                raise IOError("user specified column header %s not found in specified data file %s" % (inputvar, self._sfile))
            jj = jj+1
        locs[:] = locations[2:]
        
        # generate data matrix
        dataPy = np.genfromtxt(self._sfile, unpack=False, skip_header=2, delimiter = "\t", usecols = locations)
        norows = dataPy.shape[0]
        nocols = dataPy.shape[1]
        datavec1 = np.zeros((nocols))
        data = matrix.Matrix(norows, nocols)
        for i in range(norows):
            for j in range(nocols):
                data.SetVal(i,j,dataPy[i,j])
        if interpmethod == 'linear':
            interp = lininterp.LinInterp()
        else:
            raise IOError("Specified interpolation method: %s not supported, use <linear>" % interpmethod)
        flag = 0
        flag = interp.Interp(data, 0, interpval, datavec1)
        if flag == 1:
            raise RuntimeError("Interpolation failed: interpolation value out of bounds")
        datavec[:] = datavec1[1:]
        return 0 




