import numpy as np
from copy import deepcopy
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
        self_rows = self.size()[0]
        self_cols = self.size()[1]
        other_cols = self.size()[1]
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
        return self.matrix == other.matrix

    def __getitem__(self, item):
        return self.matrix[item]
    
    def size(self):
        rows = len(self.matrix)
        cols = len(self.matrix[0])
        return rows,cols
    
    def ullmann_1(self, used, P, G, current_row=0, num_izomorphisms=0, recursive_calls=0):
        recursive_calls += 1 

        if current_row == len(self.matrix):
            M_matrix = np.array(self.matrix)
            P_matrix = np.array(P.matrix)
            G_matrix = np.array(G.matrix)
            if (P_matrix == (M_matrix @ G_matrix @ M_matrix.T)).all():
                num_izomorphisms += 1
            return num_izomorphisms, recursive_calls

        for c in range(self.size()[1]):
            if c not in used:
                used.add(c)
                self.matrix[current_row] = [0] * self.size()[1]
                self.matrix[current_row][c] = 1
                num_izomorphisms, recursive_calls = self.ullmann_1(used, P, G, current_row + 1, num_izomorphisms, recursive_calls)
                used.remove(c)
                
        return num_izomorphisms, recursive_calls

    def ullmann_2(self, used, P, G, current_row=0, num_izomorphisms=0, recursive_calls=0):
        recursive_calls += 1 

        if current_row == len(self.matrix):
            M_matrix = np.array(self.matrix)
            P_matrix = np.array(P.matrix)
            G_matrix = np.array(G.matrix)
            if (P_matrix == (M_matrix @ G_matrix @ M_matrix.T)).all():
                num_izomorphisms += 1
            return num_izomorphisms, recursive_calls

        M0_copy = deepcopy(self)

        for c in range(M0_copy.size()[1]):
            if c not in used and self[current_row][c] != 0:
                used.add(c)
                M0_copy.matrix[current_row] = [0] * M0_copy.size()[1]
                M0_copy.matrix[current_row][c] = 1
                num_izomorphisms, recursive_calls = AdjacencyMatrix.ullmann_2(M0_copy, used, P, G, current_row + 1, num_izomorphisms, recursive_calls)
                used.remove(c)
                
        return num_izomorphisms, recursive_calls
    
    def ullmann_3(self, used, P, G, current_row=0, num_izomorphisms=0, recursive_calls=0):
        recursive_calls += 1 

        if current_row == len(self.matrix):
            M_matrix = np.array(self.matrix)
            P_matrix = np.array(P.matrix)
            G_matrix = np.array(G.matrix)
            if (P_matrix == (M_matrix @ G_matrix @ M_matrix.T)).all():
                num_izomorphisms += 1
            return num_izomorphisms, recursive_calls

        M0_copy = deepcopy(self)
        M0_copy.prune(P, G)
        
        for c in range(M0_copy.size()[1]):
            if c not in used and self[current_row][c] != 0:
                used.add(c)
                M0_copy.matrix[current_row] = [0] * M0_copy.size()[1]
                M0_copy.matrix[current_row][c] = 1
                num_izomorphisms, recursive_calls = AdjacencyMatrix.ullmann_2(M0_copy, used, P, G, current_row + 1, num_izomorphisms, recursive_calls)
                used.remove(c)
                
        return num_izomorphisms, recursive_calls

    def prune(self, P, G):
        is_changed = True
        
        while is_changed:
            is_changed = False
            for i in range(self.size()[0]):
                for j in range(self.size()[1]):
                    if self[i][j] == 1:
                        is_neighbour = False
                        for x in range(P.size()[1]):
                            for y in range(G.size()[1]):
                                if self[x][y] == 1:
                                    is_neighbour = True
                                    break
                        if not is_neighbour:
                            self[i][j] = 0
                            is_changed = True
                            break

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

    #ullmann 1.0
    M = AdjacencyMatrix()
    for i in range(len(g_P.matrix)):
        M.matrix.append([])
        current_row = M.matrix[i]
        for j in range(len(g_G.matrix[0])):
            current_row.append(0)
    used = set([])
    print(M.ullmann_1(used=used, G=g_G, P=g_P))

    #ullmann 2.0
    M0 = AdjacencyMatrix()
    for i in range(len(g_P.matrix)):
        M0.matrix.append([])
        current_row = M0.matrix[i]
        for j in range(len(g_G.matrix[0])):
            current_row.append(0)
    for i in range(g_P.size()[0]):
        p_len = np.sum(g_P.matrix[i])
        for j in range(g_G.size()[0]):
            g_len = np.sum(g_G.matrix[j])
            if p_len <= g_len:
                M0[i][j] = 1
    used = set([])
    print(M0.ullmann_2(used=used, G=g_G, P=g_P))

    #ullmann 3.0
    M0 = AdjacencyMatrix()
    for i in range(len(g_P.matrix)):
        M0.matrix.append([])
        current_row = M0.matrix[i]
        for j in range(len(g_G.matrix[0])):
            current_row.append(0)
    for i in range(g_P.size()[0]):
        p_len = np.sum(g_P.matrix[i])
        for j in range(g_G.size()[0]):
            g_len = np.sum(g_G.matrix[j])
            if p_len <= g_len:
                M0[i][j] = 1
    used = set([])
    print(M0.ullmann_3(used=used, G=g_G, P=g_P))

main()