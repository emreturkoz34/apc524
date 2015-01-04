#!/usr/bin/env python

import numpy as np
import unittest

import sys
sys.path.append('../mod')

import sorting
import matrix

class Sorting(unittest.TestCase):

    def testBubbleSort(self):
        print "\ntest Bubble sort simple case"
        filesmatC = []
        filesmatC.append([10, 20, 30, 40, 30, 20, 10])
        filesmatC.append([1, 2, 3, 4, 5, 6, 7])
        sorter = sorting.bubble_sort(filesmatC)
        sorter.SetRefColNum(0)
        sorter.SetSortEndIndex(7)
        sorter.generateIndexArray()
        sorter.extractRefCol()
        sorter.sort_data()
        



if __name__ == '__main__':
    unittest.main()
