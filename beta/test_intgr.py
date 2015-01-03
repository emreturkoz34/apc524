#!/usr/bin/env python

import numpy as np

import sys
sys.path.append('./mod')

import integrator

#####################################################
# Modify these values ONLY
#####################################################

ZPoints = 1001
ZMin = 0
ZMax = 1

# Gauss Legendre Quadrature
Nodes = 50

#####################################################
# Creates all arrays needed
#####################################################

# create array of type "double *"
Z = np.linspace(ZMin, ZMax, ZPoints)

# create integrand array 
f = np.linspace(4,8,ZPoints)


#####################################################
# Performs integration
#####################################################

trapz = integrator.trapz(f,Z)
simps = integrator.simpson(f,Z)
quadr = integrator.glquad(f,Z, Nodes)

#####################################################
# Prints results
#####################################################

# Set print options
np.set_printoptions(precision=2, suppress=True)

# Print results
print "Trapz integral = " + str(trapz)
print "Simps integral = " + str(simps)
print "GLQuad integral = " + str(quadr)
