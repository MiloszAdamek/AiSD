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

def search_pattern_PD(P, T, i, j):

    D = np.zeros((len(P), len(T))).astype('int')
    for x in range(len(T)):
        D[0][x] = 0
    for y in range(len(P)):
        D[y][0] = y

    Parents = np.chararray((len(P), len(T)))
    for k in range(len(P)):
        for l in range(len(T)):
            Parents[k][l] = 'X'
    Parents = Parents.astype("U256")
    for k in range(1, len(P)):
        Parents[k][0] = 'D'

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
    k = 0
    j = 0

    while k < len(T):
        if D[i][k] < D[i][j]:
            j = k
        k += 1

    return j - len(P) + 2

def longest_common_pattern_PD(P: str, T: str, i: int, j: int):

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

            if P[k] != T[l]:
                zamian = D[k-1][l-1] + 500000
            else:
                zamian = D[k-1][l-1]
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

def longest_sequention_reconstruction(P, Parents):
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

        elif curr == 'D':
            i -= 1

        else: 
            j -= 1
        
        if curr == 'M':
            result.append(P[i+1])
        curr = Parents[i][j]

    result.reverse()
    result = ''.join(result)
    return result

def main():
    P1 = ' kot'
    T1 = ' koń'

    P2 = ' kot'
    T2 = ' pies'

    P8 = ' biały autobus'
    T8 = ' czarny autokar'
    # print(string_compare_recur(P1, T1, 3, 3))
    print(string_compare_recur(P2, T2, 3, 4))
    # min_cost, Parents = string_compare_PD(P1,T1,len(P1) - 1,len(T1) - 1)
    # print(min_cost)
    # min_cost, Parents = string_compare_PD(P2,T2,len(P2) - 1,len(T2) - 1)
    # print(min_cost)
    min_cost, Parents = string_compare_PD(P8,T8,len(P8) - 1,len(T8) - 1)
    print(min_cost)

    P3 = ' thou shalt not'
    T3 = ' you should not'

    min_cost, Parents = string_compare_PD(P3, T3, len(P3) - 1, len(T3) - 1)
    print(path_reconstruction(Parents))

    P4 = ' ban'
    T4 = ' mokeyssbanana'
    print(search_pattern_PD(P4,T4,len(P4) - 1,len(T4) - 1))

    P5 = ' bin'
    print(search_pattern_PD(P5,T4,len(P5) - 1,len(T4) - 1))

    P6 = ' democrat'
    T6 = ' republican'
    _, Parents = longest_common_pattern_PD(P6,T6,len(P6) - 1, len(T6) - 1)
    result = longest_sequention_reconstruction(P6, Parents)
    print(result)

    P7 = ' 243517698'
    T7 = "".join(sorted(P7))
    _, Parents = longest_common_pattern_PD(P7,T7,len(P7) - 1, len(T7) - 1)
    result = longest_sequention_reconstruction(P7, Parents)
    print(result)
    
main()