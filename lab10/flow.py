import numpy as np

class Vertex:

    def __init__(self, key, edge=None) -> None:
        self.key = key
        self.edge = edge

    def __hash__(self):
        return hash(self.key)

    def __eq__(self, other):
        return self.key == other.key
    
    def __str__(self):
        return f"{self.key}"
    
class Edge:

    def __init__(self, capacity=0, isResidual=False) -> None:
        self.capacity = capacity #pojemność/przepustowość
        self.isResidual = isResidual #flaga
        if self.isResidual:
            self.residual = self.capacity
            self.flow = 0
        else:
            self.residual = 0
            self.flow = 0  
    
    def __repr__(self) -> str:
        str = ""
        str += f"{self.capacity} "
        str += f"{self.flow} "
        str += f"{self.residual} "
        str += f"{self.isResidual}"
        return str
        
class AdjacencyList:

    def __init__(self):
        self.vertex_dict = {}

    def insert_vertex(self, vertex: Vertex):
        if vertex not in self.vertex_dict:
            self.vertex_dict[vertex] = {}

    def is_empty(self):
        return not bool(self.vertex_dict)

    def insert_edge(self, vertex1: Vertex, vertex2: Vertex, edge=None):
        if vertex1 not in self.vertex_dict:
            self.insert_vertex(vertex1)
        if vertex2 not in self.vertex_dict:
            self.insert_vertex(vertex2)

        self.vertex_dict[vertex1][vertex2] = edge

    def delete_vertex(self, vertex: Vertex):
        if vertex in self.vertex_dict:
            del self.vertex_dict[vertex]
            for v in self.vertex_dict:
                if vertex in self.vertex_dict[v]:
                    del self.vertex_dict[v][vertex]

    def delete_edge(self, vertex1: Vertex, vertex2: Vertex):
        if vertex1 in self.vertex_dict and vertex2 in self.vertex_dict:
            if vertex2 in self.vertex_dict[vertex1]:
                del self.vertex_dict[vertex1][vertex2]
            if vertex1 in self.vertex_dict[vertex2]:
                del self.vertex_dict[vertex2][vertex1]
        
    def neighbours(self, vertex_id):
        return self.vertex_dict[vertex_id].items()
    
    def vertices(self):
        return self.vertex_dict.keys()
    
    def get_vertex(self, vertex_id):
        return vertex_id

    def BFS(self, first):
        visited = set([])
        parent = {}
        queue = []

        visited.add(first)
        queue.append(first)

        while queue:
            elem = queue[0]
            for neighbour in self.neighbours(elem):
                if neighbour not in visited and self.vertex_dict[elem][neighbour].residual > 0:
                    visited.add(neighbour)
                    parent[neighbour] = elem
                    queue.append(neighbour)
        return parent
    
    def min_capacity(self, parent: dict, first=None, last=None):

        curr_vertex = first
        min_residual = np.inf

        if curr_vertex not in parent.keys():
            return 0
        else: 
            while curr_vertex != last:
                edge = self.vertex_dict[curr_vertex][parent[curr_vertex]]
                if edge.residual < min_residual:
                    min_residual = edge.residual
                curr_vertex = parent[curr_vertex]
        return min_residual
    
    def augumenting_path(self, parent:dict, min_capacity, first, last):
        curr_vertex = first

        if curr_vertex not in parent.keys():
            return 0
        else: 
            while curr_vertex != last:
                edge1 = self.vertex_dict[curr_vertex][parent[curr_vertex]]
                edge2 = self.vertex_dict[parent[curr_vertex]][curr_vertex]

                if edge1.isResidual:
                    edge1.flow += min_capacity
                    edge1.residual -= min_capacity
                    edge2.residual += min_capacity
                else:
                    edge1.residual -= min_capacity
                    edge2.flow -= min_capacity
                    edge2.residual += min_capacity

                if edge2.isResidual:
                    edge2.flow += min_capacity
                    edge2.residual -= min_capacity
                    edge1.residual += min_capacity
                else:
                    edge2.residual -= min_capacity
                    edge1.flow -= min_capacity
                    edge1.residual += min_capacity

                curr_vertex = parent[curr_vertex]

    def ford_fulkerson(self):
        first = Vertex('s')
        last = Vertex('t')

        parent = self.BFS(first)
        min_capacity = self.min_capacity(parent, first, last)

        result = 0
        while min_capacity > 0: 
            result += min_capacity
            self.augumenting_path(parent, min_capacity, first, last)
            parent = self.BFS(first)
            self.min_capacity(parent, first, last)
        return result
        
def printGraph(g):

    print("------GRAPH------")
    for v in g.vertices():
        print(v, end = " -> ")
        for (n, w) in g.neighbours(v):
            print(n, w, end=";")
        print()
    print("-------------------")

def main():
    graf_0 = [ ('s','u',2), ('u','t',1), ('u','v',3), ('s','v',1), ('v','t',2)]
    g0 = AdjacencyList()

    for elem in graf_0:
        x1, x2, weight = elem

        v1 = Vertex(x1)
        v2 = Vertex(x2)
        g0.insert_vertex(v1)
        g0.insert_vertex(v2)

        edge12 = Edge(weight, isResidual=False)
        edge21 = Edge(isResidual=True)

        g0.insert_edge(v1, v2, edge12)
        g0.insert_edge(v2, v1, edge21)
    
    printGraph(g0)
    flow = g0.ford_fulkerson()
    printGraph(g0)
    print(flow)

main()

