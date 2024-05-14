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
    
    def __mul__(self, other):
        result = AdjacencyMatrix()
        
        self_rows = self.size[0]
        self_cols = self.size[1]
        other_cols = self.size[1]
        result.matrix = [[0 for _ in range(self_rows)] for _ in range(self_cols)]
        
        if self_rows == other_cols:
            for i in range(self_rows):
                for j in range(other_cols):
                    for k in range(self_cols):
                        result[i][j] += self[i][k] * other[k][j]
        return result
        
    def transpose(self):
        result = AdjacencyMatrix()
        rows = self.size()[0]
        cols = self.size()[1]
        result.matrix = [[0 for _ in range(rows)] for _ in range(cols)]
        for i in range(rows):
            for j in range(cols):
                result[j][i] = self[i][j]
        return result

    def __eq__(self, other):
        pass

    def __getitem__(self, item):
        return self.matrix[item]
    
    def size(self):
        rows = len(self.matrix)
        cols = len(self.matrix[0])
        return rows,cols
    
    def ullmann(self, used, current_row=0):
        if current_row == self.size()[0]:
            print(self.matrix)
            return
        for c in range(self.size()[1]):
            if c not in used:
                used.add(c)
                for i in range(self.size()[1]):
                    self[current_row][i] = 0
                self[current_row][c] = 1
                self.ullmann(used, current_row+1)
                used.remove(c)
    
def printGraph(g):
    print("------GRAPH------")
    for v in g.vertices():
        print(v, end = " -> ")
        for (n, w) in g.neighbours(v):
            print(n, w, end=";")
        print()
    print("-------------------")
    
def main():

    graph_G = [('A','B',1), ('B','F',1), ('B','C',1), ('C','D',1), ('C','E',1), ('D','E',1)]
    graph_P = [('A','B',1), ('B','C',1), ('A','C',1)]

    g_P = AdjacencyMatrix()
    g_G = AdjacencyMatrix()

    for elem in graph_G:
        x1, x2, weight = elem
        v1 = Vertex(x1)
        v2 = Vertex(x2)
        g_G.insert_vertex(v1)
        g_G.insert_vertex(v2)
        g_G.insert_edge(v1, v2, weight)

    for elem in graph_P:
        x1, x2, weight = elem
        v1 = Vertex(x1)
        v2 = Vertex(x2)
        g_P.insert_vertex(v1)
        g_P.insert_vertex(v2)
        g_P.insert_edge(v1, v2, weight)

    print(g_P.matrix)
    print(g_G.matrix)

    M = AdjacencyMatrix()
    for i in range(len(g_P.matrix)):
        M.matrix.append([])
        current_row = M.matrix[i]
        for j in range(len(g_G.matrix[0])):
            current_row.append(0)
    print(M.matrix)
    used = set([])
    M.ullmann(used=used)

main()