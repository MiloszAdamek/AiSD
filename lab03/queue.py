def realloc(tab, size, start_index):
    oldSize = len(tab) 
    new_tab = [None for i in range(size)]

    for i in range(-1 * (oldSize - start_index), 0):
        new_tab[i] = tab[i]

    for j in range(0, start_index):
        new_tab[j] = tab[j]

    return new_tab

class Queue:
    
    def __init__(self, size=5, wr_index=0, rd_index=0) -> None:
        self.size = size
        self.wr_index = wr_index
        self.rd_index = rd_index
        self.tab = [None for i in range(size)]
        
    def is_empty(self):
        return self.wr_index == self.rd_index
    
    def peek(self):
        if self.is_empty():
            return False
        else:
            return self.tab[self.rd_index]
        
    def dequeue(self):
        
        if self.is_empty():
            return False
        else:
            data = self.tab[self.rd_index]
            self.tab[self.rd_index] = None
            self.rd_index += 1
            return data
    
    def enqueue(self, data):
        if self.wr_index >= self.size:
            self.wr_index = 0

        self.tab[self.wr_index] = data
        self.wr_index += 1

        if self.wr_index == self.rd_index:
            new_size = 2*self.size
            self.tab = realloc(self.tab, new_size, self.wr_index)
            self.size = new_size
            
            self.rd_index =- 4
        
    
    def __str__(self) -> str:

        if self.is_empty():
            return "[]"
        
        queue_str = "["
        for elem in self.tab:
            if elem is not None:
                queue_str += f"{elem}, "
        queue_str = queue_str[:-2]
        queue_str += "]" 

        return queue_str

def main():

    new_queue = Queue()
    
    for i in range(1,5):
        new_queue.enqueue(i)
    print(new_queue.dequeue())
    print(new_queue.peek())
    print(new_queue)
    for i in range(5,9):
        new_queue.enqueue(i)
        print(new_queue)
    print(new_queue.tab)

    while not new_queue.is_empty():
        print(new_queue.dequeue())
    print(new_queue)

main()