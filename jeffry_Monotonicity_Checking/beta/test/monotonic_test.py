#!/usr/bin/env python

import numpy as np
import unittest

import sys
sys.path.append('../mod')

import monocheck
import matrix

class MonoCheck(unittest.TestCase):
    np.set_printoptions(precision=2, suppress=True)
    

if __name__ == '__main__':
    unittest.main()
