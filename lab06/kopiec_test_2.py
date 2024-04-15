class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.n = 0  # liczba elementów w kolejce

    def enqueue(self, item):
        self.heap.append(item)
        self.n += 1
        self._upheap(len(self.heap) - 1)

    def dequeue(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            self.n -= 1
            return self.heap.pop(0)
        self._swap(0, len(self.heap) - 1)
        self.n -= 1
        item = self.heap.pop()
        self._downheap(0)
        return item

    def peek(self):
        return self.heap[0] if self.heap else None

    def is_empty(self):
        return self.n == 0

    def _upheap(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.heap[index][0] < self.heap[parent][0]:
            self._swap(index, parent)
            index = parent
            parent = (index - 1) // 2

    def _downheap(self, index):
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        smallest = index
        if left_child < len(self.heap) and self.heap[left_child][0] < self.heap[smallest][0]:
            smallest = left_child
        if right_child < len(self.heap) and self.heap[right_child][0] < self.heap[smallest][0]:
            smallest = right_child
        if smallest != index:
            self._swap(index, smallest)
            self._downheap(smallest)

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def print_tree(self, idx=0, lvl=0):
        if idx < self.n:
            self.print_tree(2 * idx + 2, lvl + 1)
            print(2 * lvl * ' ', self.heap[idx] if idx < len(self.heap) else None)
            self.print_tree(2 * idx + 1, lvl + 1)

    def print_tab(self):
        print('{', end=' ')
        print(*self.heap, sep=', ', end=' ')
        print('}')


def main():
    # Utworzenie pustej kolejki
    pq = PriorityQueue()

    # Lista priorytetów
    priorities = [7, 5, 1, 2, 5, 3, 4, 8, 9]
    # Lista wartości
    values = "GRYMOTYLA"

    # Użycie w pętli enqueue do wpisania do kolejki elementów
    for priority, value in zip(priorities, values):
        pq.enqueue((priority, value))

    # Wypisanie aktualnego stanu kolejki w postaci kopca
    print("Aktualny stan kolejki w postaci kopca:")
    pq.print_tree()

    # Wypisanie aktualnego stanu kolejki w postaci tablicy
    print("Aktualny stan kolejki w postaci tablicy:")
    pq.print_tab()

    # Użycie dequeue do odczytu pierwszej danej z kolejki
    first_item = pq.dequeue()

    # Użycie peek do odczytu i wypisania kolejnej danej
    next_item = pq.peek()
    print("Następna wartość w kolejce:", next_item)

    # Wypisanie aktualnego stanu kolejki w postaci tablicy
    print("Aktualny stan kolejki po usunięciu pierwszego elementu:")
    pq.print_tab()

    # Wypisanie zapamiętanej, usuniętej pierwszej danej z kolejki
    print("Usunięta pierwsza wartość z kolejki:", first_item)

    # Opróżnienie kolejki z wypisaniem usuwanych danych
    print("Usunięte wartości z kolejki:")
    while not pq.is_empty():
        print(pq.dequeue())

    # Wypisanie opróżnionej kolejki w postaci tablicy
    print("Opróżniona kolejka w postaci tablicy:")
    pq.print_tab()


if __name__ == "__main__":
    main()
