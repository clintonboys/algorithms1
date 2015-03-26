# -*- coding: utf-8 -*-
"""
Created on Tue Nov 18 16:03:32 2014

@author: cboys
"""
import math

def EuclideanDistance(x,y):
    return math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)


def ClosestSplitPair(Px, Py, delta):
    x_bar = Px[len(Px)/2][0]
    Sy = []
    for i in range(0,len(Py)):
        if (Py[i][0] > (x_bar - delta)) and (Py[i][0] < (x_bar + delta)):
            Sy.append(Py[i])
    best = delta
    best_pair = [0,0]
    for i in range(0,len(Sy)-7):
        for j in range(0,6):
            p = Sy[i]
            q = Sy[i+1]
            if EuclideanDistance(p,q) < best:
                best = EuclideanDistance(p,q)
                best_pair = [p,q]
    return best_pair[0], best_pair[1]
