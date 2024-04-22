import random
import time

class Element:
    def __init__(self, dane, priorytet) -> None:
        self.__dane = dane
        self.__priorytet = priorytet
    
    def __lt__(self, other): # <
        if self.__priorytet < other.__priorytet:
            return True
        else:
            return False

    def __gt__(self, other): # > 
        if self.__priorytet > other.__priorytet:
            return True
        else:
            return False

    def __repr__(self) -> str: # print
        result = ""
        result += f"{self.__priorytet}"
        result += " : "
        result += f"{self.__dane}"
        return result

class Queue:
    def __init__(self, n=None, unsorted_data=None):
        self.Tab = []
        self.n = 0

        if unsorted_data is not None:
            for elem in unsorted_data:
                self.enqueue(elem)

    def is_empty(self):
        return self.n == 0
    
    def is_leaf(self, index):
        if self.left(index) >= self.n or self.right(index) >= self.n:
            return False
        else: return True

    def peek(self):#zwraca element o najwyższym priorytecie -> wierzchołek kopca
        if self.is_empty(): return True
        else: return self.Tab[0] 
    
    def left(self, index):#na podstawie indexu węzła zwraca index lewego potomka
        return 2*index + 1

    def right(self, index):
        return 2*index + 2

    def parent(self, index): #na podstawie indexu węzła zwraca index jego rodzica
        return int((index - 1)/2)

    def dequeue(self): #nie usuwać elementów z tablicy tylko przesuwać na koniec
        if self.is_empty():
            return None
        min_elem = self.Tab[0]
        self.Tab[0] = self.Tab[self.n-1]

        #SWAP
        self.Tab[self.n-1] = min_elem
        
        self.n -= 1 #rozmiar kopca
        self.downheap(0)
        return min_elem

    def enqueue(self, elem: Element):
        self.Tab.append(elem)
        self.n += 1
        self.upheap(self.n - 1)

    def size(self):
        return len(self.Tab)

    def upheap(self, index):
        while index > 0:
            parent_idx = self.parent(index)
            if self.Tab[parent_idx] > self.Tab[index]:
                self.Tab[parent_idx], self.Tab[index] = self.Tab[index], self.Tab[parent_idx]
                index = parent_idx
            else:
                break

    def downheap(self, index):
        smallest = index
        left = self.left(index)
        right = self.right(index)
        if left < self.n and self.Tab[left] < self.Tab[smallest]:
            smallest = left
        if right < self.n and self.Tab[right] < self.Tab[smallest]:
            smallest = right
        if smallest != index:
            self.Tab[index], self.Tab[smallest] = self.Tab[smallest], self.Tab[index]
            self.downheap(smallest)

    def print_tree(self, idx, lvl):
        if idx<self.n:           
            self.print_tree(self.right(idx), lvl+1)
            print(2*lvl*'  ', self.Tab[idx] if self.Tab[idx] else None)           
            self.print_tree(self.left(idx), lvl+1)

    def print_tab(self):
        print ('{', end=' ')
        print(*self.Tab[:self.n], sep=', ', end = ' ')
        print( '}')

def heapsort(heap_data):
    if isinstance(heap_data, tuple):
        heap_data = [Element(value, key) for key, value in heap_data]
    heap = Queue(unsorted_data=heap_data)

    for i in range(heap.n -1, -1, -1):
        heap.downheap(i)
            
    sorted_data = []
    while not heap.is_empty():
        sorted_data.append(heap.dequeue())
    return sorted_data


def swap(data):
    for i in range(len(data)):
        temp = data[i]
        j = i-1
        while(j>=0 and data[j] > temp):
            data[j+1] = data[j]
            j -= 1
        data[j+1] = temp
    return data

def shift(data):
    for i in range(len(data)):
        min_indeks = data.index(min(data[i:]))
        data.insert(i, data.pop(min_indeks))
    return data

def time_test():
    data = [int(random.random() * 100) for _ in range(10000)]

    t_start = time.perf_counter()
    heapsort(data.copy())
    t_stop = time.perf_counter()
    print(f"\nHeapsort. Time:", "{:.7f}".format(t_stop - t_start))

    t_start = time.perf_counter()
    shift(data.copy())
    t_stop = time.perf_counter()
    print(f"\nShift. Time:", "{:.7f}".format(t_stop - t_start))

    t_start = time.perf_counter()
    swap(data.copy())
    t_stop = time.perf_counter()
    print(f"\nSwap. Time:", "{:.7f}".format(t_stop - t_start))



def main():
    data = [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]
    elements = [Element(value, key) for key, value in data]

    # HEAPSORT
    queue = Queue(unsorted_data=elements)
    queue.print_tree(0, 0)
    print('\n')
    queue.print_tab()
    print('\n')

    sorted_data = []
    while not queue.is_empty():
        sorted_data.append(queue.dequeue())
    print('\nHEAPSORT')
    print(sorted_data)

    # SWAP
    data_swap = elements.copy()
    print('\nSWAP')
    sorted_data = swap(data_swap)
    print(sorted_data)

    # SHIFT
    data_shift = elements.copy()
    print('\nSHIFT')
    sorted_data = shift(data_shift)
    print(sorted_data)

    time_test()

main()