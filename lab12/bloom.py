import numpy as np
import time

n = 20
P = 0.001

b = int(-n * np.log(P) / (np.log(2)**2))
k = int((b / n) * np.log(2))

def hash(word, d, b):
    hw = 0
    for i in range(len(word)):
        hw = (hw * d + ord(word[i])) % b
    return hw

d_values = [31, 37, 41]
bloom_filter = np.zeros(b, dtype=int)

def add_to_bloom_filter(pattern):
    for d in d_values:
        hw = hash(pattern, d, b)
        bloom_filter[hw] = 1

def check_bloom_filter(word):
    for d in d_values:
        hw = hash(word, d, b)
        if bloom_filter[hw] == 0:
            return False
    return True

def rabin_karp_bloom(S, patterns, d=256, q=101):
    t_start = time.perf_counter()

    compare_num = 0
    false_results = 0
    found_patterns = {pattern: 0 for pattern in patterns}
    M = len(S)
    N = len(patterns[0])

    for pattern in patterns:
        add_to_bloom_filter(pattern)

    for m in range(M - N + 1):
        word = S[m:m+N]
        if check_bloom_filter(word):
            compare_num += 1
            if word in patterns:
                found_patterns[word] += 1
            else:
                false_results += 1

    t_stop = time.perf_counter()
    print("Time:", "{:.7f}".format(t_stop - t_start))
    
    return found_patterns, compare_num, false_results

with open("lab12\lotr.txt", encoding='utf-8') as f:
        text = f.readlines()

S = ' '.join(text).lower()
patterns = ['gandalf', 'looking', 'blocked', 'comment', 'pouring', 'finally', 'hundred', 'hobbits', 'however', 'popular', 'nothing', 'enjoyed', 'stuffed', 'relaxed', 'himself', 'present', 'deliver', 'welcome', 'baggins', 'further']

found_patterns, compare_num, false_results = rabin_karp_bloom(S, patterns)
print(found_patterns)
print(rf"Compares: f{compare_num}")
print(rf"False results: f{false_results}")
