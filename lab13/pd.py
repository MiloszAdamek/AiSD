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

    D = np.zeros((len(P), len(T))).astype('int')
    for x in range(len(T)):
        D[0][x] = x
    for y in range(len(P)):
        D[y][0] = y

    Parents = np.chararray((len(P), len(T)))
    for k in range(len(P)):
        for l in range(len(T)):
            Parents[k][l] = 'X'
    Parents = Parents.astype("U256")
    for k in range(1, len(P)):
        Parents[k][0] = 'D'
    for l in range(1, len(T)):
        Parents[0][l] = 'I'

    for k in range(1, i + 1):
        for l in range(1, j + 1):
            zamian = D[k-1][l-1] + int(P[k] != T[l])
            wstawień = D[k][l-1] + 1
            usunięć = D[k-1][l] + 1

            min_cost = min(zamian, wstawień, usunięć)
            D[k][l] = min_cost

            if zamian <= wstawień and zamian <= usunięć:
                if P[k] == T[l]:
                    Parents[k][l] = 'M'
                else:
                    Parents[k][l] = 'S'
            elif wstawień < zamian and wstawień < usunięć:
                Parents[k][l] = 'I'
            else:
                Parents[k][l] = 'D'

    return D[i][j], Parents

def path_reconstruction(Parents: np.ndarray):
    result = []
    i = Parents.shape[0] - 1
    j = Parents.shape[1] - 1
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

    result.reverse()
    result = ''.join(result)
    return result

def main():
    P1 = ' kot'
    T1 = ' koń'

    P2 = ' kot'
    T2 = ' pies'

    print(string_compare_recur(P1, T1, 3, 3))
    print(string_compare_recur(P2, T2, 3, 4))
    min_cost, Parents = string_compare_PD(P1,T1,len(P1) - 1,len(T1) - 1)
    print(min_cost)
    min_cost, Parents = string_compare_PD(P2,T2,len(P2) - 1,len(T2) - 1)
    print(min_cost)

    P3 = ' thou shalt not'
    T3 = ' you should not'

    min_cost, Parents = string_compare_PD(P3, T3, len(P3) - 1, len(T3) - 1)
    print(path_reconstruction(Parents))


main()