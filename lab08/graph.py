#lista sasiedztwa na słownikach - najpierw
#macierz sasiedztwa na tablicy tablic

#graf to słownik wierzchołków, gdzie w slowniku każdemu wierzchołkowi jest przypisany słownik jego sąsaidów

#Trzy klasy: 1. wierzchołek (3 metody + dane) 2. graf lista sasiedztwa 3. graf macierz sasiedztwa
# 4. klasa krawedz - dziś nie potrzebna. W liscie sasiedztwa krotka - sąsiad to jest krotka wierzchołek + informacja o krawędzi łączącej
# None, bo za tydzien bedziemy coś wsadzać zamiast None - lista krotek, a w zasadzie slownik
#klucz wierzchołek wartość none, a w przyszłości waga krawedzi
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
        
    def neighbours(self, vertex):
        return self.vertex_dict[vertex].items()
    
    def vertices(self):
        return self.vertex_dict.keys()
    
    def get_vertex(self, vertex_id):
        return vertex_id

class AdjacencyMatrix: 
    #indexy można wyszukiwać liniowo w liście wierzchołków
    #index znalezionego by sięgnąć do macierzy

    def __init__(self) -> None:
        pass

    def is_empty():
        pass

    def insert_vertex(vertex: Vertex):
        pass

    def insert_edge(vertex1: Vertex, vertex2: Vertex, edge):
        pass

    def delete_vertex(vertex):
        pass

    def delete_edge(vertex1: Vertex, vertex2: Vertex):
        pass

def main():
    vertices = [Vertex('Z'), Vertex('G'), Vertex('N'), Vertex('B'),
                Vertex('F'), Vertex('P'), Vertex('C'), Vertex('E'),
                Vertex('W'), Vertex('L'), Vertex('D'), Vertex('O'),
                Vertex('S'), Vertex('T'), Vertex('K'), Vertex('R')]
    
    graph_list = AdjacencyList()

    for vertex in vertices:
        graph_list.insert_vertex(vertex)

    for edge in polska.graf:
        graph_list.insert_edge(Vertex(edge[0]), Vertex(edge[1]))

    graph_list.delete_vertex(Vertex('K'))
    graph_list.delete_edge(Vertex('W'), Vertex('E'))
    polska.draw_map(graph_list)



main()

