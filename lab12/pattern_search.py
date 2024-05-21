import time

with open("lab12\lotr.txt", encoding='utf-8') as f:
        text = f.readlines()

S = ' '.join(text).lower()

def naive(S, W: str):
    t_start = time.perf_counter()
    pattern_num = 0
    compare_num = 0
    m = 0
    i = 0
    while m != len(S):
            compare_num += 1
            if S[m] == W[i]:
                m += 1
                i += 1
                if i >= len(W):
                    pattern_num += 1
                    i = 0
            else: 
                i = 0
                m += 1

    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

    return pattern_num, compare_num

print(naive(S, "time."))

def hash(word):
    d = 256
    q = 101
    hw = 0
    for i in range(len(word)):  # N - to długość wzorca
        hw = (hw*d + ord(word[i])) % q  # dla d będącego potęgą 2 można mnożenie zastąpić shiftem uzyskując pewne przyspieszenie obliczeń
    return hw

def rabin_karp(S, W):
    t_start = time.perf_counter()

    compare_num = 0
    pass_num = 0
    pattern_num = 0
    M = len(S)
    N = len(W)
    hW = hash(W)

    for m in range(M-N+1):
        hS = hash(S[m:m+N])
        if hS == hW:
            pass_num += 1
            if S[m:m+N] == W:
                pattern_num += 1
        compare_num += 1

    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
    return pattern_num, compare_num, pass_num-pattern_num

print(rabin_karp(S, "time."))

def rabin_karp_rolling_hash(S, W):
    t_start = time.perf_counter()

    compare_num = 0
    pass_num = 0
    pattern_num = 0
    M = len(S)
    N = len(W)
    hW = hash(W)
    d = 256
    q = 101
    h = 1

    for i in range(N-1):  # N - jak wyżej - długość wzorca
        h = (h*d) % q 
        
    m = 0
    hS = hash(S[m:m+N])
    for m in range(M-N+1):
        if hS == hW:
            pass_num += 1
            if S[m:m+N] == W:
                pattern_num += 1
        if m + N < M:  
            hS = (d * (hS - ord(S[m]) * h) + ord(S[m + N])) % q
        compare_num += 1

    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
    return pattern_num, compare_num, pass_num-pattern_num

print(rabin_karp_rolling_hash(S, "time."))


















