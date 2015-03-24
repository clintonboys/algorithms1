# -*- coding: utf-8 -*-
"""
Created on Thu Nov 27 17:55:00 2014

@author: cboys
"""

import random
import copy

def ReadGraph(file):
    with open(file, 'rb') as f:
        graph = f.readlines()
    for i in range(0,len(graph)):
        graph[i] = graph[i].split('\t')[:-1]
    graph_dict = {}
    for i in range(0,len(graph)):
        graph_dict[graph[i][0]] = graph[i][1:]
    return graph_dict
    
def RemoveDups(array):
    x = []
    for i in range(0,len(array)):
        if array[i] not in x:
            x.append(array[i])
    return x
     
def Merge(ingraph, u, v):
    graph = copy.deepcopy(ingraph)
    graph[str(u)+','+str(v)] = graph.pop(u)
    for i in range(0,len(graph[v])):
        graph[str(u)+','+str(v)].append(graph[v][i])
    del graph[v]    
    for i in range(0,len(graph)):
        if v in graph.values()[i]:
            graph.values()[i][graph.values()[i].index(v)] = str(u)+','+str(v)
        if u in graph.values()[i]:
            graph.values()[i][graph.values()[i].index(u)] = str(u)+','+str(v)
    for i in range(0,len(graph)):
        graph[graph.keys()[i]] = RemoveDups(graph.values()[i])
    for i in range(0,len(graph)):
        if graph.keys()[i] in graph.values()[i]:
            graph.values()[i].remove(graph.keys()[i])
    return graph

def FindCutFromTwoVertices(ingraph,u,v):
    first_half = u.split(',')
    second_half = v.split(',')
    edge_count = 0
    for i in range(0,len(first_half)):
        for j in ingraph[first_half[i]]:
            if j in second_half:
                edge_count = edge_count + 1
    return edge_count
    

def FindMinCut(ingraph):
    graph = copy.deepcopy(ingraph)
    vertex_list = graph.keys() 
    while len(vertex_list) > 2:
        start_vert = random.choice(vertex_list)
        end_vert = random.choice(graph[start_vert])
        graph = Merge(graph, start_vert, end_vert)
        vertex_list = graph.keys()
    return vertex_list
    
def GetMinCuts(graph,times):
    first_pass = FindMinCut(graph)
    count = FindCutFromTwoVertices(graph, first_pass[0], first_pass[1])
    times_run = 0
    while times_run < times:
        p = FindMinCut(graph)
        b = FindCutFromTwoVertices(graph, p[0], p[1])
        if b < count:
            count = b
        times_run = times_run + 1
    return count
    