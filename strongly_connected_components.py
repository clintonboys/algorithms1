# -*- coding: utf-8 -*-
"""
Created on Sun Nov 30 15:54:47 2014

@author: cboys
"""

import copy





def ReadGraph(file):
    with open(file) as f:
        pregraph = f.readlines()
    edge_list = []
    for i in range(0,len(pregraph)):
        edge_list.append(pregraph[i].split(' '))
        edge_list[i][1] = edge_list[i][1][:-1]
    return edge_list
    
def RemoveDups(array):
    x = []
    for i in range(0,len(array)):
        if array[i] not in x:
            x.append(array[i])
    return x
    
def GraphToAdjList(graph):
    # assume ReadGraph has processed file
    adj_list = [[x[0],[]] for x in graph] + [[x[1],[]] for x in graph]    
    adj_list = RemoveDups(adj_list)
    vertices = [x[0] for x in adj_list]
    for i in range(0,len(graph)):
        adj_list[vertices.index(graph[i][0])][1].append(graph[i][1])
    adj_list.sort()
    return adj_list
    
def GraphToDict(graph):
    graph_dict = {}
    vertices = [x[0] for x in graph] + [x[1] for x in graph]    
    vertices = RemoveDups(vertices)
    for vertex in vertices:
        graph_dict[vertex] = []
    for i in range(0,len(graph)):
        graph_dict[graph[i][0]].append(graph[i][1])
    return graph_dict
    
def ReverseGraph(ingraph):
    graph = copy.deepcopy(ingraph)
    newgraph = [[x[0],[]] for x in graph]
    vertices = [x[0] for x in newgraph]
    for i in range(0,len(ingraph)):
        for j in range(0,len(ingraph[i][1])):
            newgraph[vertices.index(ingraph[i][1][j])][1].append(ingraph[i][0])
    return newgraph
    
def DFSLoop(ingraph, is_reversed = False): 
    # make sure we take as input the grpah as an adj_list, not a dict
    graph = copy.deepcopy(ingraph)
    graph = GraphToDict(graph)
    if is_reversed:
        graph_rev = copy.deepcopy(ingraph)
        for i in range(0,len(graph_rev)):
            graph_rev[i][0], graph_rev[i][1] = graph_rev[i][1], graph_rev[i][0]
        graph = GraphToDict(graph_rev)
    leader = [0]*len(graph)    
    fin_time = [0]*len(graph)
    t = 0
    s = None
    travelled = [[key, False] for key in graph.keys()]
    
    def DFS(graph, vertex):
        travelled[graph.keys().index(vertex)][1] = True
        leader[travelled.index([vertex,True])] = s
        for j in range(0,len(graph[vertex])):
            if not travelled[graph.keys().index(graph[vertex][j])][1]:
                DFS(graph, graph[vertex][j])
        t+=1
        fin_time[graph.keys().index(vertex)] = t

    for i in range(0,len(graph)):
        if not travelled[len(graph)-i-1][1]:
            s = graph.keys()[len(graph)-i-1]
            DFS(graph, graph.keys()[len(graph)-i-1])
    
    return fin_time, leader
    
def GraphReorder(ingraph, f): 
    # take in graph as list
    graph = copy.deepcopy(ingraph)
    

def Kosaraju(ingraph):
    graph = copy.deepcopy(ingraph)
    fins,_ = DFSLoop(graph, True)    
    _, leads = DFSLoop(GraphReorder(graph, fins), False)
    return leads
    
    