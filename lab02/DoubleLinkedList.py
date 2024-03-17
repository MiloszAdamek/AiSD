class Element():

    def __init__(self, data: list):
        self.data = data #pole data wskazuje na dane
        self.next = None #pole next wskazuje na następny element
        self.prev = None #pole prev wskazuje na poprzedni element w liście
    
class DoubleLinkedList():

    def __init__(self, head=None, tail=None): #tworzy pustą listę
        self.head = head #wskazanie na pierwszy element listy
        self.tail = tail

    def destroy(self):
        while self.length() != 1:
            new_head = self.head.next
            self.head = new_head
        self.head = None
            
    def add(self, data): #adding to the head
        new_element = Element(data)
        self.head.prev = new_element #ustawienie prev aktualnego elementu z głowy na nowy element
        new_element.next = self.head #ustawia next nowego elementu na bieżącą głowę listy -> nowy element staje się pierwszym elementem listy
        self.head = new_element #ustawia self.head na nowy element, czyniąc go nową głową listy
        
    def append(self, data): #adding to the tail
        new_element = Element(data)
        if self.is_empty(): 
            self.head = new_element
            self.tail = new_element
        else:
            new_element.prev = self.tail
            self.tail.next = new_element
            self.tail = new_element

            
    def remove(self):
        if not self.is_empty():
            first_elem = self.head
            secound_elem = first_elem.next
            self.head = secound_elem
            self.head.prev = None

    # #TODO:
    def remove_end(self):
        if not self.is_empty():
            if self.length() == 1:
                self.head = None
                self.tail = None
            else:
                last_element = self.tail
                self.tail = last_element.prev
                self.tail.next = None
                last_element = None

    def is_empty(self):
        return self.head == None

    def length(self):
        length = 0
        if not self.is_empty():
            element = self.head
            while element:
                element = element.next
                length += 1
            return length

    def get(self): 
        first_elem = self.head
        return first_elem.data
    
    def __str__(self):
        list_str = ""
        current_element = self.head
        while current_element:
            list_str += f"-> {current_element.data}\n"
            current_element = current_element.next
        return list_str

def main():
    data = [('AGH', 'Kraków', 1919),
            ('UJ', 'Kraków', 1364),
            ('PW', 'Warszawa', 1915),
            ('UW', 'Warszawa', 1915),
            ('UP', 'Poznań', 1919),
            ('PG', 'Gdańsk', 1945)]
    
    uczelnie = DoubleLinkedList()
    for i in range(3):
        uczelnie.append(data[i])
    for i in range(3, len(data)):
        uczelnie.add(data[i])
    print(uczelnie)
    print(f"{uczelnie.length()}\n")
    uczelnie.remove()
    print(f"{uczelnie.get()}\n")
    uczelnie.remove_end()
    print(uczelnie)
    uczelnie.destroy()
    print(uczelnie.is_empty())
    uczelnie.remove()
    uczelnie.append(data[0])
    uczelnie.remove_end()
    print(uczelnie.is_empty())

main()