# -*- coding: utf-8 -*-
"""
Closest pair
Created on Tue Nov 18 13:46:58 2014

@author: cboys
"""
import math
from merge_sort import MergeSort

def EuclideanDistance(x,y):
    return math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)
    
def SortPoints(points):
    Px = MergeSort(points)
    swapped_points = []
    for i in range(0,len(points)):
        swapped_points.append([points[i][1],points[i][0]])
    prePy = MergeSort(swapped_points)
    Py = []
    for i in range(0,len(prePy)):
        Py.append([prePy[i][1],prePy[i][0]])
    return Px, Py

def ClosestPairSorted(Px,Py):
    
    def ClosestSplitPair(Px, Py, delta):
        x_bar = Px[len(Px)/2][0]
        Sy = []
        for i in range(0,len(Py)):
            if (Py[i][0] > (x_bar - delta)) and (Py[i][0] < (x_bar + delta)):
                Sy.append(Py[i])
        best = delta
        best_pair = None
        for i in range(0,len(Sy)-7):
            for j in range(0,6):
                p = Sy[i]
                q = Sy[i+1]
                if EuclideanDistance(p,q) < best:
                    best = EuclideanDistance(p,q)
                    best_pair = [p,q]
        if best_pair is not None:
            return best_pair[0], best_pair[1]
        else:
            return None
    
    if (len(Px) == 2):
        return Px[0], Px[1]
    elif (len(Px) == 3):
        candidates = [[Px[0],Px[1]], [Px[0],Px[2]], [Px[1], Px[2]]]
        return min(candidates, key=lambda p: EuclideanDistance(p[0],p[1]))[0], min(candidates, key=lambda p: EuclideanDistance(p[0],p[1]))[1]
    else:
        Qx = Px[0:len(Px)/2]
        Rx = Px[len(Px)/2:len(Px)]
        Qy = Py[0:len(Py)/2]
        Ry = Py[len(Py)/2:len(Py)]
        p1, q1 = ClosestPairSorted(Qx,Qy)
        p2, q2 = ClosestPairSorted(Rx,Ry)
        delta = min(EuclideanDistance(p1,q1), EuclideanDistance(p2,q2))
        if ClosestSplitPair(Px,Py,delta) == None:
            return min([[p1,q1],[p2,q2]], key = lambda p: EuclideanDistance(p[0],p[1]))[0], min([[p1,q1],[p2,q2]], key = lambda p: EuclideanDistance(p[0],p[1]))[1]
        else:
            p3, q3 = ClosestSplitPair(Px,Py,delta)
            candidates = [[p1,q1], [p2,q2], [p3,q3]]
            return min(candidates, key=lambda p: EuclideanDistance(p[0],p[1]))[0], min(candidates, key=lambda p: EuclideanDistance(p[0],p[1]))[1]
        
def ClosestPair(points):
    return ClosestPairSorted(SortPoints(points)[0], SortPoints(points)[1])