#!/usr/bin/env python

import numpy as np
import unittest

import sys
sys.path.append('../mod')

import sorting
import matrix



length = 15
n = matrix.Matrix(length,2)
for i in range(length):
    n.SetVal(i,0,-i*(i-length-1))
for i in range(length):
    n.SetVal(i,1,i)


def non_decreasing(array):
    return all(x<=y for x, y in zip(array, array[1:]))

class Sorting(unittest.TestCase):


    def testBubbleSort(self):
        print "\ntest Bubble sort simple case"
        m = n
        sorter = sorting.bubble_sort(m)
        sorter.SetRefColNum(0)
        sorter.sort_data()
        arr = []
        for i in range(length):
            arr.append(m.GetVal(i,0))
        self.assertTrue(non_decreasing(arr))

        
    def testStandardSort(self):
        print "\ntest Standard sort simple case"
        m = n
        sorter = sorting.standard_sort(m)
        sorter.SetRefColNum(0)
        sorter.sort_data()
        arr = []
        for i in range(length):
            arr.append(m.GetVal(i,0))
        self.assertTrue(non_decreasing(arr))

        

    def testBruteSort(self):
        print "\ntest Brute sort simple case"
        m = n
        sorter = sorting.brute_sort(m)
        sorter.SetRefColNum(0)
        sorter.sort_data()
        arr = []
        for i in range(length):
            arr.append(m.GetVal(i,0))
        self.assertTrue(non_decreasing(arr))


if __name__ == '__main__':
    unittest.main()
