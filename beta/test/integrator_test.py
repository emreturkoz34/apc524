#!/usr/bin/env python

import numpy as np
import unittest

import sys
sys.path.append('../mod')

import integrator

class Integrator(unittest.TestCase):

    def testTrapzLin(self):
        print "\ntest Trapezoid rule: linear function"
        f = lambda x : 2 * x
        domain = np.linspace(0,2,101)
        integrand = f(domain)
        r = integrator.trapz(integrand, domain)
        self.assertAlmostEqual(r, 4)

    def testTrapzQuadratic(self):
        print "\ntest Trapezoid rule: quadratic function"
        f = lambda x : x**2 - 1
        domain = np.linspace(0,1,101)
        integrand = f(domain)
        r = integrator.trapz(integrand, domain)
        self.assertAlmostEqual(r, -0.6667, 3)

    def testTrapzNonLinDomain(self):
        print "\ntest Trapezoid rule: nonlinear domain"
        f = lambda x : 2 * x
        domain = np.logspace(0,1,100)
        integrand = f(domain)
        r = integrator.trapz(integrand, domain)
        self.assertAlmostEqual(r, 99)


    def testSimpsLin(self):
        print "\ntest Simpson rule: linear function"
        f = lambda x : 2 * x
        domain = np.linspace(0,2,101)
        integrand = f(domain)
        r = integrator.simpson(integrand, domain)
        self.assertAlmostEqual(r, 4)

    def testSimpsQuadratic(self):
        print "\ntest Simpson rule: quadratic function"
        f = lambda x : x**2 - 1
        domain = np.linspace(0,1,101)
        integrand = f(domain)
        r = integrator.simpson(integrand, domain)
        self.assertAlmostEqual(r, -0.6667, 3)


    def testGLQuadLin(self):
        print "\ntest Gauss Legendre Quadrature rule: linear function"
        f = lambda x : 2 * x
        domain = np.linspace(0,2,101)
        integrand = f(domain)
        r = integrator.glquad(integrand, domain, 10)
        self.assertAlmostEqual(r, 4)

    def testGLQuadQuadratic(self):
        print "\ntest Gauss Legendre Quadrature rule: quadratic function"
        f = lambda x : x**2 - 1
        domain = np.linspace(0,1,101)
        integrand = f(domain)
        r = integrator.glquad(integrand, domain, 40)
        self.assertAlmostEqual(r, -0.6667, 3)

    def testGLQuadNonLinDomain(self):
        print "\ntest Gauss Legendre Quadrature rule: nonlinear domain"
        f = lambda x : 2 * x
        domain = np.logspace(0, 1, 100)
        integrand = f(domain)
        r = integrator.glquad(integrand, domain, 30)
        self.assertAlmostEqual(r, 99)

if __name__ == '__main__':
    unittest.main()
