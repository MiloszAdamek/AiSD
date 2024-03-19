class hashTable:
    
    def __init__(self, size, c1=1, c2=0) -> None:
        self.tab = [None for i in range(size)]
        self.c1 = c1
        self.c2 = c2
        self.size = size

    def hash(self, key):
        if isinstance(key, str):
            key = ord(key)
        return key % self.size 
            
    def collision(self, key, data):
        hv = self.hash(key)
        for i in range(self.size):
            t = (hv + self.c1 * i + self.c2 * i**2) % self.size
            if self.tab[t] != None:
                self.tab[t] = data
        if self.tab[t] == None:
            print('Brak miejsca')
            return None
            
    def search(self, key):
        if self.tab[self.hash(key)] is not None:
            return self.tab[self.hash(key)]
        else: return None
       
    def insert(self, key, data):
        hv = self.hash(key)
        if self.tab[hv] is None:
            self.tab[hv] = data
        else:
            hv = self.collision(key, data)

    def remove(self, key, x=None):
        self.tab[self.hash(key)] = x

    def __str__(self):
        result = "{"
        for i in range(self.size):
            if self.tab[i] is not None:
                result += f"{i}: {self.tab[i]}, "
        if result.endswith(", "):
            result = result[:-2]
        result += "}"
        return result

def test1():
    list_dict = hashTable(size=13)
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

def test2():
    pass

def main():
    test1()
    test2()


main()

