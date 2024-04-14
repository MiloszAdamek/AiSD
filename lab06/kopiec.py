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
    def __init__(self, n=None):
        self.Tab = []
        self.n = 0
    
    def is_empty(self):
        return self.n == 0
    
    def peek(self):#zwraca element o najwyższym priorytecie -> wierzchołek kopca
        if self.is_empty(): return True
        else: return self.Tab[0] 
    
    def left(self, index):#na podstawie indexu węzła zwraca index lewego potomka
        return 2*index + 1

    def right(self, index):
        return 2*index + 2

    def parent(self, index): #na podstawie indexu węzła zwraca index jego rodzica
        return int((index - 1)/2)

    def dequeue(self):
        if self.is_empty():
            return None
        min_elem = self.Tab[0]
        self.Tab[0] = self.Tab[-1]
        self.Tab.pop()
        self.n -= 1 #rozmiar kopca
        self.downheap(0)
        return min_elem

    def enqueue(self, elem: Element):
        self.Tab.append(elem)
        self.upheap(self.n)
        self.n += 1 #rozmiar kopca

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

def main():
    heap = Queue()
    priority = [7,5,1,2,5,3,4,8,9]
    data = "GRYMOTYLA"

    for i, p in enumerate(priority):
        heap.enqueue(Element(dane=data[i],priorytet=p))

    heap.print_tab()
    print('\n')
    heap.print_tree(0,0)
    first_elem = heap.dequeue()
    print('\n')
    print(heap.peek())
    print('\n')
    heap.print_tab()
    print('\n')
    print(first_elem)
    print('\n')
    while not heap.is_empty():
        elem = heap.dequeue()
        print(elem)
    print('\n')
    heap.print_tab()

main()

#usuwając z kopca nie usuwać z tablicy, tablica może być większa od kopca
#trzeba pamietać rozmiar kopca niezależnie od rozmiaru tablicy
#przy wstawianiu nie wystarczy append/pop tylko trzeba porównywać 
#jesli rozmiar tablicy == rozmiar kopca -> append
#jesli nie to wykorzystujemy wolne miejsce