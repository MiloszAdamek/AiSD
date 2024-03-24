class Element:
    
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return f"{self.key}:{self.value}"

class hashTable:
    
    def __init__(self, size, c1=1, c2=0) -> None:
        self.tab = [None for i in range(size)]
        self.c1 = c1
        self.c2 = c2
        self.size = size

    def hash(self, key):
        if isinstance(key, str):
            key = sum(ord(char) for char in key)
        return key % self.size 
            
    def collision(self, hv, n):
        t = (hv + self.c1 * n + self.c2 * n**2) % self.size
        return t
        
    def search(self, key):
        hv = self.hash(key)
        n = 0

        while n < self.size:
            new_hv = self.collision(hv, n)
            if self.tab[new_hv] is None:
                return None
            elif self.tab[new_hv].key == key:
                return self.tab[new_hv].value
            n += 1
        return None      
     
    def insert(self, key, data):
        elem = Element(key, data)
        hv = self.hash(key)
        n = 0

        while n < self.size:
            new_hv = self.collision(hv, n)
            if self.tab[new_hv] is None:
                self.tab[new_hv] = elem
                return 
            elif self.tab[new_hv].key == key:
                self.tab[new_hv] = elem #nadpisanie wartości
                return
            n += 1
        print('Brak miejsca')
    
    def remove(self, key):
        hv = self.hash(key)
        n = 0
        while n < self.size:
            new_hv = self.collision(hv, n)
            if self.tab[new_hv] is None:
                print("Brak danej")
                return
            elif self.tab[new_hv].key == key:
                self.tab[new_hv] = None
                return
            n += 1

    def __str__(self):
        result = "{"
        for elem in self.tab:
            result += str(elem)
            result += ", "
        if result.endswith(", "):
            result = result[:-2]
        result += "}"
        return result

def test1(c1, c2):
    list_dict = hashTable(size=13, c1=c1, c2=c2)
    print(list_dict)
    letter = 'A'
    for i in range(1, 16):
        if i == 6: i = 18
        if i == 7: i = 31
        list_dict.insert(i,letter)
        letter = ord(letter) + 1
        letter = chr(letter)
    print(list_dict)
    print(list_dict.search(5))
    print(list_dict.search(14))
    list_dict.insert(5, 'Z')
    print(list_dict.search(5))
    list_dict.remove(5)
    print(list_dict)
    print(list_dict.search(31))
    
    list_dict.insert('test', 'W')
    print(list_dict)

def test2(c1, c2):
    list_dict = hashTable(size=13, c1=c1, c2=c2)
    letter = 'A'
    for i in range(1, 16):
        list_dict.insert(13*i,letter)
        letter = ord(letter) + 1
        letter = chr(letter)
    list_dict.insert(5, 'Z')
    list_dict.remove(5)
    list_dict.insert('test', 'W')
    print(list_dict)

def main():
    test1(c1=1, c2=0)
    print('----------------------------------------------')
    test2(c1=1, c2=0)
    print('----------------------------------------------')
    test2(c1=0, c2=1)
    print('----------------------------------------------')
    test1(c1=0, c2=1)

main()

