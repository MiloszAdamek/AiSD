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

def transpose(A: Matrix):
    result = Matrix(rows=A.cols, cols=A.rows)
    for i in range(A.rows):
        for j in range(A.cols):
            result[j][i] = A[i][j]
    return result

def main():

    m1 = Matrix([[1, 0, 2],
                [-1, 3, 1]])
 
    m2 = Matrix(rows=2, cols=3, default_value=1)

    m3 = Matrix([[3, 1],
                [2, 1],
                [1, 0]]) 
    
    print(transpose(m1))
    print(m1 + m2)
    print(m1 * m3)

main()