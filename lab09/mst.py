import numpy as np
import graf_mst

class Vertex:

    def __init__(self, key, edge=None, colour=None) -> None:
        self.key = key
        self.edge = edge
        self.colour = colour

    def __hash__(self):
        return hash(self.key)

    def __eq__(self, other):
        return self.key == other.key
    
    def __str__(self):
        return f"{self.key}"
    
class AdjacencyList:

    def __init__(self):
        self.vertex_dict = {}
        self.intree = {}
        self.distance = {}
        self.parent = {}

    def insert_vertex(self, vertex: Vertex):
        if vertex not in self.vertex_dict:
            self.vertex_dict[vertex] = {}

        self.intree[vertex] = 0
        self.distance[vertex] = np.inf
        self.parent[vertex] = None

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

def printGraph(g):
    print("------GRAPH------")
    for v in g.vertices():
        print(v, end = " -> ")
        for (n, w) in g.neighbours(v):
            print(n, w, end=";")
        print()
    print("-------------------")

def Prim_MST(graph: AdjacencyList):
    MST = AdjacencyList()
    sum = 0

    curr_vertex = list(graph.vertices())[0]

    while graph.intree[curr_vertex] == 0:
        
        MST.insert_vertex(curr_vertex)
        graph.intree[curr_vertex] = 1

        for neighbour, weight in graph.neighbours(curr_vertex):
            if graph.intree[neighbour] == 0 and weight < graph.distance[neighbour]:
                graph.distance[neighbour] = weight
                graph.parent[neighbour] = curr_vertex

        min_dst = np.inf
        next_vertex = None
        for v in graph.vertices():
            if graph.intree[v] == 0 and graph.distance[v] < min_dst:
                min_dst = graph.distance[v]
                next_vertex = v

        if next_vertex is None:
            break

        MST.insert_edge(next_vertex, graph.parent[next_vertex], graph.distance[next_vertex])
        MST.insert_edge(graph.parent[next_vertex], next_vertex, graph.distance[next_vertex])
        sum += graph.distance[next_vertex]

        curr_vertex = next_vertex
        
    return MST, sum

def main():
    
    input_graph = AdjacencyList()

    for elem in graf_mst.graf:
        x1, x2, weight = elem

        v1 = Vertex(x1)
        v2 = Vertex(x2)

        input_graph.insert_vertex(v1)
        input_graph.insert_vertex(v2)
        input_graph.insert_edge(v1, v2, weight)
        input_graph.insert_edge(v2, v1, weight)

    MST, sum = Prim_MST(input_graph)
    printGraph(MST)

main()