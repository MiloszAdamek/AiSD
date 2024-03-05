class Matrix: 

    def __init__(self, data = [], rows = 0, cols = 0):\
    
        if rows == 0 and cols == 0:

            self.data = data

        elif rows != 0 and cols != 0: #macierz zer o podanych wymiarach

            self.data = data

            for i in range(rows):
                self.data.append([])
                current_row = self.data[i]
                for j in range(cols):
                    current_row.append(0)
            

    def __add__(m1, m2):

        if isinstance(m1,Matrix) and isinstance(m2, Matrix):
            if m1.size()[0] == m2.size()[0] and m1.size()[1] == m2.size()[1]:
                
                m3 = Matrix(rows=m1.size()[0], cols=m1.size()[1])

                for i in range(m1.size()[0]):
                    current_row_m1 = m1[i]
                    current_row_m2 = m2[i] 
                    current_row_m3 = m2[i]

                    for j in range(m1.size()[1]):
                        current_row_m3.append(current_row_m1[j] + current_row_m2[j])
                        
                return m3

            else: print('Matrix has to be squared!')

    # def __mul__(m1, m2):

    #     if isinstance(m1,Matrix) and isinstance(m2, Matrix):
    #         if m1.size()[0] == m2.size[0] and m1.size[1] == m2.size[1]:
    #             pass
    #         else: print('!')

    def __getitem__(self, row_num: int, col_num: int):

        rows, cols = Matrix.size(self)

        for row in range(rows):
            if row == row_num:
                selected_row = self.data[row_num]
                break

        for col in range(cols):
            if col == col_num:
                cell_value = selected_row[col_num]
        
        return cell_value
    
    def size(self):

        rows = len(self.data)
        cols = len(self.data[0])

        return rows,cols

    def __str__(self):

        rows, cols = Matrix.size(self)

        for i in range(rows):
            print('|', end='')
            for j in range(cols):
                print(f" {Matrix.__getitem__(self,i,j)} ", end='')
                if j != rows: print('\t',end='')
            print('|\n', end='')

def main():

    m1 = Matrix([[1, 0, 2],
                [-1, 3, 1]])
    
    m3 = Matrix([[1, 0, 2],
            [-1, 3, 1]])
    
    m2 = Matrix([[3, 1],
                [2, 1],
                [1, 0]])     
      
    # print(m1.size())
    # print(m1.__getitem__(0,0))
    # print(m1.__str__())

    # empty_matrix = Matrix(rows = 2, cols = 3)
    # print(empty_matrix.size())
    # print(empty_matrix.__str__())

    m3 = Matrix.__add__(m1,m2)
    print(m3.__str__())

    # print(m1)
    # print('\n\n\n')
    # print(m2)

    # m3 = [[3, 1],
    # [2, 1],
    # [1, 0]]

main()