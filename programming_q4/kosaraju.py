# -*- coding: utf-8 -*-
"""
Created on Mon Dec  1 16:08:48 2014

@author: cboys
"""

import copy

class Vertex(object):

    def __init__(self, vertex_id):
        self._vertex_id = vertex_id
        self.incoming = set()
        self.outgoing = set()
        self.explored = False
        self.finish_time = 0

    @property
    def vertex_id(self):
        return self._vertex_id

    def __eq__(self, another_vertex):
        return self._vertex_id == another_vertex._vertex_id

    def __hash__(self):
        return hash(self._vertex_id)

def ReadGraph(file):
    read_vertices = {}
    with open(file) as f:
        for line in f:
            this_line = line.split(' ')
            start_vertex_id, end_vertex_id = int(this_line[0]), int(this_line[1])
            if start_vertex_id in read_vertices:
                start_vertex = read_vertices[start_vertex_id]
            else:
                start_vertex = Vertex(start_vertex_id)
                read_vertices[start_vertex_id] = start_vertex

            if end_vertex_id in read_vertices:
                end_vertex = read_vertices[end_vertex_id]
            else:
                end_vertex = Vertex(end_vertex_id)
                read_vertices[end_vertex_id] = end_vertex

            start_vertex.outgoing.add(end_vertex)
            end_vertex.incoming.add(start_vertex)

    return sorted(read_vertices.values(), key=lambda vertex: vertex.vertex_id)

def Kosaraju(graph):
    # take as input list of Vertex class instances

    # start with outer DFS Loop

    finish_time = 0
    for v in reversed(graph):
        if not v.explored:
            vertex_stack = [v]
            while len(vertex_stack) > 0:
                vertex = vertex_stack[-1]
                vertex.explored = True
                pushed_new_vertex_to_stack = False
                for start_vertex in vertex.incoming:
                    if not start_vertex.explored:
                        vertex_stack.append(start_vertex)
                        pushed_new_vertex_to_stack = True
                        break
                if pushed_new_vertex_to_stack:
                    continue
                vertex_stack.pop()
                finish_time = finish_time + 1
                vertex.finish_time = finish_time

    graph.sort(key=lambda vertex: vertex.finish_time)

    for vertex in graph:
        vertex.explored = False

    # now do inner DFS loop, noting vertices are now sorted by finish time
    # from outer loop

    scc_sizes = []
    for v in reversed(graph):
        if not v.explored:
            vertex_stack = [v]
            scc_size = 0
            while len(vertex_stack) > 0:
                vertex = vertex_stack[-1]
                vertex.explored = True
                pushed_new_vertex_to_stack = False
                for end_vertex in vertex.outgoing:
                    if not end_vertex.explored:
                        vertex_stack.append(end_vertex)
                        pushed_new_vertex_to_stack = True
                        break
                if pushed_new_vertex_to_stack:
                    continue
                vertex_stack.pop()
                scc_size = scc_size + 1
            scc_sizes.append(scc_size)

    while len(scc_sizes) < 5:
        scc_sizes.append(0)

    scc_sizes.sort(reverse=True)

    print "Got sizes of 5 biggest SCCs: " + ",".join(map(str, scc_sizes[0:5]))

# def DFSLoop(ingraph):
#     graph = copy.deepcopy(ingraph)
#     leader = [0]*len(graph)
#     fin_time = [0]*len(graph)
#     t = 0
#     s = None
#     vertices = [x[0] for x in graph]
#     travelled = [[x[0], False] for x in graph]
#
#     def DFS(graph, vertex):
#         global t
#         vert_no = vertices.index(vertex)
#         travelled[vert_no][1] = True
#         leader[vert_no] = s
#
#         vert_stack = [vertex]
#         while len(vert_stack)>0:
#             v = vert_stack[-1]
#             travel
#             if
#         for j in range(0,len(graph[vert_no][1])):
#             if not travelled[vertices.index(graph[vert_no][1][j])][1]:
#                 DFS(graph, graph[vert_no][1][j])
#         t = t + 1
#         fin_time[vert_no] = t
#
#     for i in range(0,len(graph)):
#         if not travelled[len(graph)-i-1][1]:
#             s = graph[len(graph)-i-1][0]
#             DFS(graph, graph[len(graph)-i-1][0])
#
#     return fin_time, leader
#
#
#
# def RemoveDups(array):
#     x = []
#     for i in range(0,len(array)):
#         if array[i] not in x:
#             x.append(array[i])
#     return x
#
# def GraphToAdjList(graph):
#     # assume ReadGraph has processed file
#     adj_list = [[x[0],[]] for x in graph] + [[x[1],[]] for x in graph]
#     adj_list = RemoveDups(adj_list)
#     vertices = [x[0] for x in adj_list]
#     for i in range(0,len(graph)):
#         adj_list[vertices.index(graph[i][0])][1].append(graph[i][1])
#     adj_list.sort()
#     return adj_list
#
# def ReverseGraph(ingraph):
#     graph = copy.deepcopy(ingraph)
#     newgraph = [[x[0],[]] for x in graph]
#     vertices = [x[0] for x in newgraph]
#     for i in range(0,len(ingraph)):
#         for j in range(0,len(ingraph[i][1])):
#             newgraph[vertices.index(ingraph[i][1][j])][1].append(ingraph[i][0])
#     return newgraph
#
# def GraphReorder(ingraph,order):
#     graph = copy.deepcopy(ingraph)
#     newgraph = []
#     for i in range(0,len(order)):
#         newgraph.append(graph[order[i]-1])
#     return newgraph
#
# def Kosaraju(ingraph,ingraph_rev):
#     fins,_ = DFSLoop(ingraph_rev)
#     print fins
#     _, leads = DFSLoop(GraphReorder(ingraph, fins))
#     d = {x:leads.count(x) for x in leads}
#     for i in range(0,len(d)):
#         print 'Strongly connected component of size '+str(d.values()[i])
#
#
#
#
# # reverse G from adjacency list, Grev
#
# # run DFS-loop on Grev, output f(v)
#
# # reorder G by f(v)
#
# # run DFS-loop on reordered G