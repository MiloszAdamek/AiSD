import numpy as np

def string_compare_recur(P: str, T: str, i: int, j:int):
    
    if i == 0:
        return j
    if j == 0:
        return i
    zamian = string_compare_recur(P,T,i-1,j-1) + (P[i] != T[j])
    wstawień = string_compare_recur(P,T,i,j-1) + 1
    usunięć = string_compare_recur(P,T,i-1,j) + 1

    min_cost = min(zamian,wstawień,usunięć)

    return min_cost

def string_compare_PD(P: str, T: str, i: int, j: int):

    D = np.zeros((len(P) + 1, len(T) + 1)).astype('int')
    for x in range(len(T) + 1):
        D[0][x] = x
    for y in range(len(P) + 1):
        D[y][0] = y

    Parrents = np.chararray((len(P) + 1, len(T) + 1))
    for k in range(len(P) + 1):
        for l in range(len(T) + 1):
            Parrents[k][l] = 'X'
    for k in range(1, len(P) + 1):
        Parrents[k][0] = 'D'
    for l in range(1, len(T) + 1):
        Parrents[0][l] = 'I'

    for k in range(1, i + 1):
        for l in range(1, j + 1):
            zamian = D[k-1][l-1] + int(P[k-1] != T[l-1])
            wstawień = D[k][l-1] + 1
            usunięć = D[k-1][l] + 1

            min_cost = min(zamian, wstawień, usunięć)
            D[k][l] = min_cost

            if zamian <= wstawień and zamian <= usunięć:
                if P[k-1] == T[l-1]:
                    Parrents[k][l] = 'M'
                else:
                    Parrents[k][l] = 'S'
            elif wstawień < zamian and wstawień < usunięć:
                Parrents[k][l] = 'I'
            else:
                Parrents[k][l] = 'D'

    return D[i][j], Parrents

def path_reconstruction(Parents: np.ndarray):
    result = []
    i = Parents.shape[0]
    j = Parents.shape[1]
    curr = Parents[i][j]
    while curr != 'X':

        if curr == 'M':
            i -= 1
            j -= 1

        elif curr == 'S':
            i -= 1
            j -= 1

        elif curr == "D":
            i -= 1

        else: 
            j -= 1

        result.append(curr)
        curr = Parents[i][j]
        
    return result.reverse()




def main():
    P1 = ' kot'
    T1 = ' koń'

    P2 = ' kot'
    T2 = ' pies'

    print(string_compare_recur(P1, T1, 3, 3))
    print(string_compare_recur(P2, T2, 3, 4))
    min_cost, Parents = string_compare_PD(P1,T1,len(P1),len(T1))
    print(min_cost)
    min_cost, Parents = string_compare_PD(P2,T2,len(P2),len(T2))
    print(min_cost)

    path_reconstruction(Parents)
main()