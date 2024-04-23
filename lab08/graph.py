#lista sasiedztwa na słownikach - najpierw
#macierz sasiedztwa na tablicy tablic

#graf to słownik wierzchołków, gdzie w slowniku każdemu wierzchołkowi jest przypisany słownik jego sąsaidów

#Trzy klasy: 1. wierzchołek (3 metody + dane) 2. graf lista sasiedztwa 3. graf macierz sasiedztwa
# 4. klasa krawedz - dziś nie potrzebna. W liscie sasiedztwa krotka - sąsiad to jest krotka wierzchołek + informacja o krawędzi łączącej
# None, bo za tydzien bedziemy coś wsadzać zamiast None - lista krotek, a w zasadzie slownik
#klucz wierzchołek wartość none, a w przyszłości waga krawedzi
import polska

class Vertex:
    def __init__(self, key, edge=None) -> None:
        self.key = key
        self.edge = edge

    def __hash__(self):
        return hash(self.key)
    
class AdjacencyList:

    def __init__(self):
        self.vertex_dict = {}

    def insert_vertex(self, vertex: Vertex):
        if vertex not in self.vertex_dict:
            self.vertex_dict[vertex] = {}

    def is_empty(self):
        if self.vertex_dict is None:
            return True

    def insert_edge(self, vertex1: Vertex, vertex2: Vertex, edge=None):
        if vertex1 not in self.vertex_dict:
            self.insert_vertex(vertex1)
        if vertex2 not in self.vertex_dict:
            self.insert_vertex(vertex1)

        self.vertex_dict[vertex1][vertex2] = edge

    def delete_vertex(self, vertex: Vertex):
    
        self.vertex_dict[vertex] = None

        for v in self.vertex_dict:
            neighbours_list = self.neighbours(v)
            if vertex in neighbours_list:
                self.vertex_dict[v][vertex] = None

    def delete_edge(self, vertex1: Vertex, vertex2: Vertex):
        self.vertex_dict[vertex1][vertex2] = None
        self.vertex_dict[vertex2][vertex1] = None
        
    def neighbours(self, vertex):
        return self.vertex_dict[vertex].items()
    
    def vertices(self):
        return self.vertex_dict.keys()

class AdjacencyMatrix: 
    #indexy można wyszukiwać liniowo w liście wierzchołków
    #index znalezionego by sięgnąć do macierzy

    def __init__(self) -> None:
        pass

    def is_empty():
        pass

    def insert_vertex(vertex: Vertex):
        pass

    def insert_edge(verex1: Vertex, vertex2: Vertex, edge):
        pass

    def delete_vertex(vertex):
        pass

    def delete_edge(verex1: Vertex, vertex2: Vertex):
        pass

def main():
    vertices = [Vertex('Z'), Vertex('G'), Vertex('N'), Vertex('B'),
                Vertex('F'), Vertex('P'), Vertex('C'), Vertex('E'),
                Vertex('W'), Vertex('L'), Vertex('D'), Vertex('O'),
                Vertex('S'), Vertex('T'), Vertex('K'), Vertex('R')]
    
    edges = [('Z','G'), ('Z', 'P'), ('Z', 'F'),
       ('G','Z'), ('G', 'P'), ('G', 'C'), ('G', 'N'),
       ('N','G'), ('N', 'C'), ('N', 'W'), ('N', 'B'),
       ('B','N'), ('B', 'W'), ('B', 'L'), 
       ('F','Z'), ('F', 'P'), ('F', 'D'), 
       ('P','F'), ('P', 'Z'), ('P', 'G'), ('P', 'C'), ('P','E'), ('P', 'O'), ('P', 'D'),        
       ('C','P'), ('C', 'G'), ('C', 'N'), ('C', 'W'), ('C','E'),        
       ('E','P'), ('E', 'C'), ('E', 'W'), ('E', 'T'), ('E','S'), ('E', 'O'),        
       ('W','C'), ('W', 'N'), ('W', 'B'), ('W', 'L'), ('W','T'), ('W', 'E'),        
       ('L','W'), ('L', 'B'), ('L', 'R'), ('L', 'T'),
       ('D','F'), ('D', 'P'), ('D', 'O'), 
       ('O','D'), ('O', 'P'), ('O', 'E'), ('O', 'S'),
       ('S','O'), ('S', 'E'), ('S', 'T'), ('S', 'K'),
       ('T','S'), ('T', 'E'), ('T', 'W'), ('T', 'L'), ('T','R'), ('T', 'K'),        
       ('K','S'), ('K', 'T'), ('K', 'R'), 
       ('R','K'), ('R', 'T'), ('R', 'L')]
    
    graph_list = AdjacencyList()

    for vertex in vertices:
        graph_list.insert_vertex(vertex)

    for edge in edges:
        graph_list.insert_edge(Vertex(edge[0]), Vertex(edge[1]))

    polska.draw_map(graph_list.vertex_dict)

    # graph_list.delete_vertex(Vertex('K'))

main()

