# -*- coding: utf-8 -*-
"""
Randomised selection
Created on Wed Nov 19 19:21:57 2014

@author: cboys
"""

import random
from quicksort_comparecount import Partition

def RSelect(array, i):
    n = len(array)
    if n == 1:
        return array[0]
    else:
        pivot = random.choice(array)
        array[array.index(pivot)], array[0] = array[0], array[array.index(pivot)]
        Partition(array, 0, n)
        j = array.index(pivot)
        print array, pivot
        if j == i-1: 
            return pivot
        elif j > i:
            return RSelect(array[:j],i)
        else:
            return RSelect(array[j:],i-j)
    