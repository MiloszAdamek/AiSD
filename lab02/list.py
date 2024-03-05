class Element():

    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList():

    def __init__(self, head=None): #tworzy pustą listę
        self.head = head #wskazanie na pierwszy element listy

    def destroy(self):
        self.head = None

    def add(self, data):
        if not self.head:
            self.head = Element(data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Element(data)
        
    def append(self, data):
        pass

    def remove(self): #usuwanie elementu z początku listy
        self.data.remove()

    def remove_end(self):
        i = len(self.data)
        del self.data[i]

    def is_empty(self):
        flag = True
        for i, elem in enumerate(self.data):
            if elem is None:
                flag = True
            else:
                return False
        return flag
    
    def length(self):
        current = self.head
        len = 0
        while current.next:
            current = current.next
            len += 1
        return len
    
    def get(self):
        return self.data[0]
    
    # def __str__(self):
    #     for elem in self.data:
    #         print(f"{elem}\n",end='')

        
def main():
    data = [('AGH', 'Kraków', 1919),
            ('UJ', 'Kraków', 1364),
            ('PW', 'Warszawa', 1915),
            ('UW', 'Warszawa', 1915),
            ('UP', 'Poznań', 1919),
            ('PG', 'Gdańsk', 1945)]
    
    uczelnie = LinkedList()
    for i in range(3):
        uczelnie.add(Element(data[i]))
    print(uczelnie)

main()