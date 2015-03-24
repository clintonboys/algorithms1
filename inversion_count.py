# -*- coding: utf-8 -*-
"""
Inversion count
Created on Mon Nov 17 12:22:35 2014

@author: cboys
"""

def SplitInvCount(array_pair):
    n = len(array_pair[0])+len(array_pair[1])
    array = [0]*n
    i = 0
    j = 0
    split_inv_count = 0
    for k in range (0,n):
        if (i < len(array_pair[0])) and ((j >= len(array_pair[1])) or (array_pair[0][i] < array_pair[1][j])):
            array[k] = array_pair[0][i]
            i = i+1
        else:
            array[k] = array_pair[1][j]
            j = j+1
            split_inv_count = split_inv_count + len(array_pair[0]) - i 
    return array, split_inv_count
                    
def InversionCount(array):
    if len(array) <= 1:
        return array, 0
    middle = len(array)/2
    left, a = InversionCount(array[:middle])
    right, b = InversionCount(array[middle:])
    result, c = SplitInvCount([left, right])
    return result, (a + b + c)