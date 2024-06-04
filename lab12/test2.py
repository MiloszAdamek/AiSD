import time

# Wczytanie pliku i przekształcenie do ciągu znaków
with open("lab12\lotr.txt", encoding='utf-8') as f:
    text = f.readlines()

S = ' '.join(text).lower()

# Implementacja metody naiwnej
def naive(S, W):
    t_start = time.perf_counter()
    pattern_num = 0
    compare_num = 0
    m = 0

    while m <= len(S) - len(W):
        match = True
        for i in range(len(W)):
            compare_num += 1
            if S[m + i] != W[i]:
                match = False
                break
        if match:
            pattern_num += 1
        m += 1

    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
    return pattern_num, compare_num

# Implementacja funkcji haszującej
def hash_function(word, d=256, q=101):
    hw = 0
    for i in range(len(word)):
        hw = (hw * d + ord(word[i])) % q
    return hw

# Implementacja metody Rabina-Karpa
def rabin_karp(S, W):
    t_start = time.perf_counter()

    compare_num = 0
    pattern_num = 0
    M = len(S)
    N = len(W)
    hW = hash_function(W)

    for m in range(M - N + 1):
        hS = hash_function(S[m:m + N])
        compare_num += 1
        if hS == hW:
            if S[m:m + N] == W:
                pattern_num += 1

    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
    return pattern_num, compare_num

# Implementacja metody Rabina-Karpa z rolling hash
def rabin_karp_rolling_hash(S, W):
    t_start = time.perf_counter()

    compare_num = 0
    pattern_num = 0
    M = len(S)
    N = len(W)
    d = 256
    q = 101
    hW = hash_function(W, d, q)
    hS = hash_function(S[:N], d, q)
    h = 1

    for i in range(N - 1):
        h = (h * d) % q

    collisions = 0

    for m in range(M - N + 1):
        if hS == hW:
            if S[m:m + N] == W:
                pattern_num += 1
            else:
                collisions += 1
        if m < M - N:
            hS = (d * (hS - ord(S[m]) * h) + ord(S[m + N])) % q
            if hS < 0:
                hS += q
        compare_num += 1

    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
    return pattern_num, compare_num, collisions

# Testowanie metod
print("Naive Method Results:", naive(S, "time."))
print("Rabin-Karp Method Results:", rabin_karp(S, "time."))
print("Rabin-Karp Rolling Hash Results:", rabin_karp_rolling_hash(S, "time."))
