import matplotlib.pyplot as plt
import numpy as np

class ProcFile(object):
    """returns interpolated data (in datavec) from the given file 
    for the species given in inputvars. Also returns all columen headers
    from the datafile in titles"""

    def __init__(self, sfile):
        # Initialize class that will process the file indicated by the sfile input
        self._sfile = sfile

    def gettitles(self):
        # generatre a vector containing the column headers in the 2nd row of the data file
        fin = open(self._sfile)
        l1 = fin.readline()
        l2 = fin.readline()
        titles = l2.strip().split('\t')
        fin.close()
        return titles

    def interpolate(self, inputvars, locs, datavec, interpval = 0.055, interpmethod = 'linear'):
        # read the columns of the data file corresponding to inputvars,
        # write the column numbers of these columns into locs
        # interpolate at interpval, using the interpolation method 
        # indicated by interpmethod, write interpolated values to datavec
        
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
        data = np.genfromtxt(self._sfile, unpack=False, skiprows=2, delimiter = "\t", usecols = locations)

        # Here we will carry out the interpolation using the C++ function
        # for now, a placeholder
        datavec[:] = data[4,1:]

        return 0 # maybe return 1 if fail


# define function that extracts an input from the input file data
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


# define function that gives strings of species for a given progress variable vector, eg [ 0 1 0 0 1 ] --> [Y-CH4 Y-O2]
def get_progvar(progvarvec, testspecies, locs, index = 1):
    progvarlocsFULL = [] #column indices of species in full data file
    progvarnames = [] #species names (strings)
    for j in range(len(progvarvec)):
        if progvarvec[j] == 1:
            progvarlocsFULL.append(int(locs[j]))
            progvarnames.append(testspecies[j])
    return [progvarlocsFULL, progvarnames, index]


# function to plot progress variable vs temp
def plotCvT(Tvec, Cvec, fname="CvsT"):
    plt.figure()
    plt.plot(Tvec, Cvec)
    plt.xlabel("T (K)")
    plt.ylabel("C")
    plt.title("Best Progress Variable")
    plt.savefig("%s.pdf" % fname)
    plt.clf()
