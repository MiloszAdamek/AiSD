class Matrix: 

    def __init__(self, data = None, rows = 0, cols = 0, default_value = 0):
    
        if rows == 0 and cols == 0 and data is not None:
            self._data = data
            self.rows = self.size()[0]
            self.cols = self.size()[1]

        elif rows != 0 and cols != 0: #macierz zer o podanych wymiarach

            self._data = []
            self.rows = rows
            self.cols = cols
            
            for i in range(rows):
                self._data.append([])
                current_row = self._data[i]
                for j in range(cols):
                    current_row.append(default_value)
                
    def __add__(A, B):

        if isinstance(A,Matrix) and isinstance(B, Matrix):

            if A.size() == B.size():
                
                result = Matrix(rows=A.rows, cols=A.cols)

                for i in range(A.rows):
                    current_row_A = A[i]
                    current_row_B = B[i] 
                    current_row_result = result[i]

                    for j in range(A.cols):
                        cell_value = current_row_A[j] + current_row_B[j]
                        current_row_result[j] = cell_value
                        
                return result

            else: print('Matrices must have equal dimensions')

    def __mul__(A, B):

        if isinstance(A, Matrix) and isinstance(B, Matrix): # A o wymiarach (n x m), B o wymiarach (m x n)

            result = Matrix(rows=A.rows, cols=B.cols)

            if A.size()[0] == B.size()[1]:

                for i in range(A.rows):
                    for j in range(B.cols):
                        for k in range(A.cols):
                            result[i][j] += A[i][k] * B[k][j]
                return result
            
        if isinstance(A, Matrix) and isinstance(B, float):
            result = Matrix(rows=A.rows, cols=A.cols)
            for i in range(A.rows):
                for j in range(A.cols):
                    result[i][j] += A[i][j] * B

            return result

        else: print('Numerous of columns in A has to be equal to numerous of columns in B!')

    def __getitem__(self, item):

        return self._data[item]

    def size(self):

        rows = len(self._data)
        cols = len(self._data[0])

        return rows,cols

    def __str__(self):

        rows, cols = self.size()
        matrix_str = ""

        for i in range(rows):
            matrix_str += '|'
            for j in range(cols):
                matrix_str += f" {self._data[i][j]}"
            matrix_str += ' |\n'

        return matrix_str
    
    def det_sarrus(self):
        return (self[0][0] * self[1][1]) - (self[0][1] * self[1][0])

def transpose(A: Matrix):
    result = Matrix(rows=A.cols, cols=A.rows)
    for i in range(A.rows):
        for j in range(A.cols):
            result[j][i] = A[i][j]
    return result

def reduce_matrix(A: Matrix):
    r, c = A.size()
    data = []

    for i in range(r - 1):
        new_row = []
        for j in range(c - 1):
            m = Matrix([[A[0][0], A[0][j+1]], [A[i+1][0], A[i+1][j+1]]])
            new_row.append(m.det_sarrus())
        data.append(new_row)
    result = Matrix(data)
    return result


def chio_det(A: Matrix, mul=1):
    
    if A.rows == A.cols:
        n = A.rows
        new_mul = mul * (1 /(A[0][0] ** (n - 2)))
        if n > 2:
            A = reduce_matrix(A)
            return chio_det(A, new_mul)
        else: 
            det = mul * A.det_sarrus()
            return det
    else: print('Matrix has to be squared!')

def main():

    A = Matrix([[5 , 1 , 1 , 2 , 3],

                [4 , 2 , 1 , 7 , 3],

                [2 , 1 , 2 , 4 , 7],

                [9 , 1 , 0 , 7 , 0],

                [1 , 4 , 7 , 2 , 2] ])
    det_A = chio_det(A)
    print(det_A)

main()