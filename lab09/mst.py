import turtle
import numpy as np
import graf_mst

# dla kazdego wezla sprawdzać sąsiadów i poprawić sąsiadom odległosci do jego najblizszego sąsiada
# krawędź = odlgegłość

class Vertex:

    def __init__(self, key, edge=None, colour=None) -> None:
        self.key = key
        self.edge = edge
        self.colour = colour
        self.intree = 0
        self.distance = np.float64('inf')
        self.parent = None

    def __hash__(self):
        return hash(self.key)

    def __eq__(self, other):
        return self.key == other.key
    
    def __str__(self):
        return f"{self.key}"
    
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

def printGraph(g):
    print("------GRAPH------")
    for v in g.vertices():
        print(v, end = " -> ")
        for (n, w) in g.neighbours(v):
            print(n, w, end=";")
        print()
    print("-------------------")

def Prim_MST(g: AdjacencyList):
    T_prim = AdjacencyList()
    sum = 0
    vertex = list(g.vertices())[0]
    T_prim.insert_vertex(vertex)

    while vertex.intree == 0:

        vertex.intree = 1
        for neighbour, w in g.neighbours(vertex):
            print(neighbour.edge, neighbour.distance)
            if neighbour.edge < neighbour.distance and neighbour.intree == 0:
                neighbour.distance = neighbour.edge
                vertex = neighbour.parent
        
        distance_list = []
        for v in list(T_prim.vertices()):
            if v.intree == 0:
                distance_list.append[v.distance]

        min_dst = min(distance_list)
        
        for v in list(T_prim.vertices()):
            if v.distance == min_dst:
                T_prim.insert_edge(v, v.parent, min_dst)
                sum += min_dst
                break

    return T_prim, sum

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