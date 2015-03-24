__author__ = 'cboys'

class Vertex(object):

    def __init__(self, vertex_id):
        self._vertex_id = vertex_id
        self.incoming = set()
        self.outgoing = set()
        self.explored = False
        self.distance = 0

    @property
    def vertex_id(self):
        return self._vertex_id

    def __eq__(self, another_vertex):
        return self._vertex_id == another_vertex._vertex_id

    def __hash__(self):
        return hash(self._vertex_id)



class Edge(object):

    def __init__(self, start_vert, end_vert, length):
        self._start_vert = start_vert
        self._end_vert = end_vert
        self._length = length

    def start_vert(self):
        return self._start_vert
    def end_vert(self):
        return self._end_vert
    def length(self):
        return self._length

    def __eq__(self, another_edge):
        return self._start_vert == another_edge._start_vert and self._end_vert == another_edge._end_vert and \
               another_edge._length == self\
            ._length


def ReadSimple(file,n):
    verts = []
    edges = []
    for i in range(0,n):
        verts.append(Vertex(i+1))
    with open(file) as f:
        for line in f:
            this_line = line.split('\t')[:-1]
            sv = Vertex(int(this_line[0]))
            for j in range(1,len(this_line)):
                ev = Vertex(int(this_line[j].split(',')[0]))
                wt = int(this_line[j].split(',')[1])
                sv.outgoing.add(ev)
                ev.incoming.add(sv)
                edges.append(Edge(sv,ev,wt))
    return [verts, edges]

def Dijkstra(graph,source_id,dest_ids):

    vert_dict = {}
    for i in range(0,len(graph[0])):
        vert_dict[graph[0][i]._vertex_id] = graph[0][i]

    X = [vert_dict[source_id]]
    vert_dict[source_id].distance = 0

    while len(X) < len(graph[0]):
        dgc = sum(edge._length for edge in graph[1])
        edges = filter(lambda edge: edge._start_vert in X and edge._end_vert not in X, graph[1])
        for i in range(0,len(edges)):
            this_dgc = vert_dict[edges[i]._start_vert._vertex_id].distance + edges[i]._length
            if this_dgc < dgc:
                dgc = this_dgc
                w_star = edges[i]._end_vert
        X.append(w_star)
        vert_dict[w_star._vertex_id].distance = dgc

    for i in range(0,len(dest_ids)):
        print "Distance from vertex "+str(source_id)+" to "+str(dest_ids[i])+" is "+str(vert_dict[dest_ids[i]]
                                                                                        .distance)

Dijkstra(ReadSimple('dijkstraData.txt',200),1,[7,37,59,82,99,115,133,165,188,197])