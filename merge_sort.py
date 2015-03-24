# -*- coding: utf-8 -*-
"""
Merge sort
Created on Sun Nov 16

@author: cboys
"""

        
def Merge(array_pair):
    n = len(array_pair[0])+len(array_pair[1])
    array = [0]*n
    i = 0
    j = 0
    for k in range (0,n):
        if (i < len(array_pair[0])) and ((j >= len(array_pair[1])) or (array_pair[0][i] < array_pair[1][j])):
            array[k] = array_pair[0][i]
            i = i+1
        else:
            array[k] = array_pair[1][j]
            j = j+1
    return array

def MergeSort(array):
    n = len(array)
    if n == 1:
        return array
    else:
        left_array = MergeSort(array[0:n/2])
        right_array = MergeSort(array[n/2:n])
        return Merge([left_array, right_array])