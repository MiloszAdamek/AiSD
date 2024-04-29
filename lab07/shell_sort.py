import random
import time

def insertion_sort(data):
    for i in range(1, len(data)):
        temp = data[i]
        j = i-1
        while(j>=0 and data[j] > temp):
            data[j+1] = data[j]
            j -= 1
        data[j+1] = temp

def shell_sort(data):
    h = len(data) // 2
    while h < len(data) / 3:
        h = 3 * h + 1
    while h >= 1:
        for i in range(h, len(data)):
            temp = data[i]
            j = i
            while j >= h and data[j - h] > temp:
                data[j] = data[j - h]
                j -= h
            data[j] = temp
        h //= 3

def time_test():
    random_data = [int(random.random() * 100) for _ in range(10000)]

    random_insertion = random_data.copy()

    t_start = time.perf_counter()
    insertion_sort(random_insertion)
    t_stop = time.perf_counter()
    print(f"\nInsert sort. Time:", "{:.7f}".format(t_stop - t_start))

    shell_insertion = random_data.copy()

    t_start = time.perf_counter()
    shell_sort(shell_insertion)
    t_stop = time.perf_counter()
    print(f"Shell sort. Time:", "{:.7f}".format(t_stop - t_start))


def is_stable(original, sorted_arr):
    for i in range(len(sorted_arr) - 1):
        if sorted_arr[i] == sorted_arr[i + 1]:
            original_index_i = original.index(sorted_arr[i])
            original_index_iplus1 = original.index(sorted_arr[i + 1])
            if original_index_i > original_index_iplus1:
                return False
    return True

data = [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]

insertion = data.copy()
shell = data.copy()

insertion_sort(insertion)
print('\nSorted data. Insertion:')
print(insertion)
print("Stability insertion:", is_stable(data, insertion))

shell_sort(shell)
print('\nSorted data. Shell:')
print(shell)
print("Stability Shell:", is_stable(data, shell))

time_test()
