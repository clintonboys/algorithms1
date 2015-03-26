# -*- coding: utf-8 -*-
"""
Quicksort
Created on Wed Nov 19 11:07:19 2014

@author: cboys
"""

def QuickSort(array, method):
    
    if (method not in ['first', 'final', 'median']) or (method == 'first'):
        choose_func = ChoosePivotFirst
    elif method == 'final':
        choose_func = ChoosePivotFinal
    elif method == 'median':
        choose_func = ChoosePivotMedian

    def RecurSort(array):
        array_copy = array[:]
        n = len(array_copy)
        if n <= 1:
            return array_copy
        else:
            p = choose_func(array_copy)
            array_copy[array_copy.index(p)], array_copy[0] = array_copy[0], array_copy[array_copy.index(p)]
            array_copy = Partition(array_copy, 0, n)
            array_copy[0:array_copy.index(p)] = RecurSort(array_copy[0:array_copy.index(p)])
            array_copy[array_copy.index(p)+1:n] = RecurSort(array_copy[array_copy.index(p)+1:n])
            return array_copy
            
    return RecurSort(array)

def Partition(array,left,right):
    p = array[left]
    i = left + 1
    for j in range(left + 1, right):
        if array[j] < p:
            array[j], array[i] = array[i], array[j]
            i = i+1
    array[left], array[i-1] = array[i-1], array[left]
    return array
    
def ChoosePivotFirst(array):
    return array[0]

def ChoosePivotFinal(array):
    return array[-1]
    
def ChoosePivotMedian(array):
    candidates = [array[0], array[len(array)/2], array[-1]]
    candidates.remove(max(candidates))
    candidates.remove(min(candidates))
    return candidates[0]