#!/usr/bin/env python

import numpy as np

## @package combinations
# Module containing functions necessary for creating matrices for calculating 
# all possible combinations of elements of a vector/matrix

def numcoms(n,k):
    """Returns the number of ways k elements can be selected from a
    set of size n"""
    return np.math.factorial(n)/(np.math.factorial(k)*np.math.factorial(n-k))

def totnumcoms(n):
    """Returns the number of ways elements can be selected from a set of size n
    in any group size from 1 to n. """
    numcombos = 0
    for k in range(n):
        numcombos += numcoms(n,k+1)
    return numcombos

def combos(k,matrix):
    """returns a combinations matrix A such that for a row vector x:
    
    x*A gives a row vector y which contains all possible combinations of 
    k elements of x. For example, for x = [x1 x2 x3], k=2, then 
    x*A gives: [x1+x2 x1+x3 x2+x3]"""
    matsize = matrix.shape
    n = matsize[0]
    if k == 1:
        for i in range(n):
            matrix[i,i]=1
    elif k > 1:
        start = 0
        for i in range(n-k+1):
            numcombos = numcoms(n-i-1,k-1)
            matrix[i,start:start+numcombos] = 1
            combos(k-1,matrix[i+1:,start:start+numcombos])
            start += numcombos
    else:
        raise IOError("k must be greater than or equal to 1")

def combination_mat(matrix):
    """returns a combinations matrix A such that for a row vector x:
    
    x*A gives a row vector y which contains all possible combinations of 
    the elements of x. For example, for x = [x1 x2 x3], then x*A gives:
    [x1 x2 x3 x1+x2 x1+x3 x2+x3 x1+x2+x3]"""
    matsize = matrix.shape
    n = matsize[0]
    start = 0
    for k in range(n):
        numcombos = numcoms(n,k+1)
        combos(k+1,matrix[:,start:start+numcombos])
        start += numcombos
    return 0

