class Element:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

    def __le__(self, other):
        return self.priority <= other.priority

    def __eq__(self, other):
        return self.priority == other.priority

    def __str__(self):
        return f"({self.priority}, '{self.value}')"

class Queue:
    def __init__(self, n=None, data_to_sort=None):
        self.Tab = []
        self.n = 0
        if data_to_sort is not None:
            self.Tab = data_to_sort
            self.n = len(self.Tab)
            self.heapsort()
        self.print_tab()

    def heapsort(self):
        # Budowanie kopca
        for i in range(self.n // 2 - 1, -1, -1):
            self.downheap(i)
        # Sortowanie
        for i in range(self.n - 1, 0, -1):
            # Zamień korzeń z ostatnim elementem nieposortowanej części tablicy
            self.Tab[0], self.Tab[i] = self.Tab[i], self.Tab[0]
            # Napraw kopiec w nieposortowanej części tablicy
            self.n -= 1
            self.downheap(0)

    def is_empty(self):
        return self.n == 0
    
    def is_leaf(self, index):
        if self.left(index) >= self.n or self.right(index) >= self.n:
            return False
        else:
            return True

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.Tab[0]

    def left(self, index):
        return 2 * index + 1

    def right(self, index):
        return 2 * index + 2

    def parent(self, index):
        return (index - 1) // 2

    def dequeue(self): #nie usuwać elementów z tablicy tylko przesuwać na koniec
        if self.is_empty():
            return None
        min_elem = self.Tab[0]
        self.Tab[0] = self.Tab[self.n-1]

        # #SWAP
        # self.Tab[self.n-1] = min_elem
        
        self.n -= 1 #rozmiar kopca
        self.downheap(0)
        return min_elem

    def enqueue(self, elem):
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
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < self.n and self.Tab[left] > self.Tab[largest]:
            largest = left
        if right < self.n and self.Tab[right] > self.Tab[largest]:
            largest = right

        if largest != index:
            # Zamień elementy
            self.Tab[index], self.Tab[largest] = self.Tab[largest], self.Tab[index]
            # Napraw kopiec dla nowej pozycji 'largest'
            self.downheap(largest)


    def print_tree(self, idx, lvl):
        if idx < self.n:
            self.print_tree(self.right(idx), lvl + 1)
            print(2 * lvl * ' ', self.Tab[idx] if self.Tab[idx] else None)
            self.print_tree(self.left(idx), lvl + 1)

    def print_tab(self):
        print('{', end=' ')
        print(*self.Tab[:self.n], sep=', ', end=' ')
        print('}')

# Przykładowe użycie:
data = [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]
heapsort = [Element(value, key) for key, value in data]
heap = Queue(data_to_sort=heapsort)
