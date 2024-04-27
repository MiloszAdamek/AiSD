import polska
import turtle

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

class AdjacencyMatrix: 

    def __init__(self) -> None:
        self.matrix = [] #kolejne wiersze - dla kolejnych wierzchołków
        self.vertex_list = [] #informacje o wierzchołkach

    def is_empty(self):
        return (len(self.vertex_list) == 0)

    def insert_vertex(self, vertex: Vertex):
        if vertex not in self.vertex_list:
            self.vertex_list.append(vertex)
            for row in self.matrix:
                row.append(0)
            self.matrix.append([0] * len(self.vertex_list))

    def insert_edge(self, vertex1: Vertex, vertex2: Vertex, edge=None):
        if vertex1 in self.vertex_list and vertex2 in self.vertex_list:
            id_1 = self.vertex_list.index(vertex1)
            id_2 = self.vertex_list.index(vertex2)
            self.matrix[id_1][id_2] = edge
            self.matrix[id_2][id_1] = edge 

    def delete_vertex(self, vertex: Vertex):
        if vertex in self.vertex_list:
            index = self.vertex_list.index(vertex)
            self.vertex_list.pop(index)
            self.matrix.pop(index)
            for row in self.matrix:
                row.pop(index)

    def delete_edge(self, vertex1: Vertex, vertex2: Vertex):
        if vertex1 in self.vertex_list and vertex2 in self.vertex_list:
            index1 = self.vertex_list.index(vertex1)
            index2 = self.vertex_list.index(vertex2)
            self.matrix[index1][index2] = 0
            self.matrix[index2][index1] = 0

    def neighbours(self, vertex_id):
        if vertex_id in self.vertex_list:
            index = self.vertex_list.index(vertex_id)
            for i, edge in enumerate(self.matrix[index]):
                if edge != 0:
                    yield self.vertex_list[i], edge

    def vertices(self):
        return self.vertex_list

    def get_vertex(self, vertex_id):
        return vertex_id

def main():

    vertices = [Vertex('Z'), Vertex('G'), Vertex('N'), Vertex('B'),
                Vertex('F'), Vertex('P'), Vertex('C'), Vertex('E'),
                Vertex('W'), Vertex('L'), Vertex('D'), Vertex('O'),
                Vertex('S'), Vertex('T'), Vertex('K'), Vertex('R')]
    
    graph_list = AdjacencyList()
    graph_matrix = AdjacencyMatrix()

    for vertex in vertices:
        graph_list.insert_vertex(vertex)
        graph_matrix.insert_vertex(vertex)

    for edge in polska.graf:
        graph_list.insert_edge(Vertex(edge[0]), Vertex(edge[1]))
        graph_matrix.insert_edge(Vertex(edge[0]), Vertex(edge[1]))

    graph_list.delete_vertex(Vertex('K'))
    graph_list.delete_edge(Vertex('W'), Vertex('E'))
    polska.draw_map(graph_list)

    graph_matrix.delete_vertex(Vertex('K'))
    graph_matrix.delete_edge(Vertex('W'), Vertex('E'))
    polska.draw_map(graph_matrix)

main()

