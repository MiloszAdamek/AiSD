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
        #self.n = None
    
    def is_empty(self):
        for i in self.Tab:
            if i == None:
                continue
            else: return False
        return True
    
    def peek(self):#zwraca element o najwyższym priorytecie -> wierzchołek kopca
        if self.is_empty: return True
        else: return self.Tab[0] 
    
    def left(self, index):#na podstawie indexu węzła zwraca index lewego potomka
        return 2*index + 1

    def right(self, index):
        return 2*index + 2

    def parent(self, index): #na podstawie indexu węzła zwraca index jego rodzica
        return (index - 1)/2

    def dequeue(self):
        if self.is_empty():
            return None
        self.Tab[0] = self.Tab[-1]
        self.n -= 1 #rozmiar kopca
        self.downheap(0)

    def enqueue(self, elem: Element):
        if self.n == len(self.Tab):
            self.Tab.append(elem)
        else: self.Tab[-1] = elem # jeśli rozmiar kopca jest mniejszy niż tablicy - zastąpienie elementu tablicy
        self.upheap(0)
        self.n += 1 #rozmiar kopca

    def size(self):
        return len(self.Tab)

    def upheap(self, index):
        key = self.Tab[index]
        parent = self.parent(key)
        while parent > 0 and self.Tab[parent] > key:
            self.Tab[index] = self.Tab[parent]
            index = parent
            parent /= 2
        self.Tab[index] = key

    def downheap(self, index):
        left = self.left(index)
        right = self.right(index)
        pass

    def print_tree(self, idx, lvl):
        if idx<self.size:           
            self.print_tree(self.right(idx), lvl+1)
            print(2*lvl*'  ', self.tab[idx] if self.tab[idx] else None)           
            self.print_tree(self.left(idx), lvl+1)

    def print_tab(self):
        print ('{', end=' ')
        print(*self.tab[:self.heap_size], sep=', ', end = ' ')
        print( '}')

def main():
    pass

main()



#usuwając z kopca nie usuwać z tablicy, tablica może być większa od kopca
#trzeba pamietać rozmiar kopca niezależnie od rozmiaru tablicy
#przy wstawianiu nie wystarczy append/pop tylko trzeba porównywać 
#jesli rozmiar tablicy == rozmiar kopca -> append
#jesli nie to wykorzystujemy wolne miejsce