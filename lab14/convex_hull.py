class Point:
    def __init__(self, x, y, id) -> None:
        self.x = x
        self.y = y
        self.id = id

    def __str__(self):
        return f"{self.x},{self.y}"

class Set:
    def __init__(self, data) -> None:
        self.dataset = []
        for i, elem in enumerate(data):
            x, y = elem
            point = Point(x, y, i)
            self.dataset.append(point)

    def __str__(self):
        string = ""
        for elem in self.dataset:
            string += f"{elem.x}, {elem.y}\n"
        return string
    
    def find_first_left(self):
        new_min = self.dataset[0]
        for elem in self.dataset:
            if elem.x < new_min.x:
                new_min = elem
            elif elem.x == new_min.x:
                if elem.y < new_min.y:
                    new_min = elem
        return new_min

    def jarvis_alg(self):
        start = self.find_first_left()
        p = start
        result = []
        result.append(p)
        q = self.dataset[p.id + 1]
        result.append(q)
        while True:
            for r in self.dataset:
                direction = (q.y - p.y)*(r.x - q.x) - (r.y - q.y)*(q.x - p.x)
                if direction > 0: #prawoskretne
                    q = r
            result.append(q)
            self.dataset[p.id] = q
            if p == start:
                break
        return result
        
    # def jarvis_alg(self):
    #     start = self.find_first_left()
    #     p = start
    #     result = []
    #     result.append(p)
    #     q = self.dataset[p.id + 1]
    #     r = self.dataset[p.id + 2]
    #     while r != start:
    #         result.append(q)
            
    #         direction = (q.y - p.y)*(r.x - q.x) - (r.y - q.y)*(q.x - p.x)
    #         if direction > 0: #prawoskretne
    #             q = r

    #         if r.id + 1 < len(self.dataset):
    #             r = self.dataset[r.id + 1]
    #         else:
    #             r = self.dataset[0]
    #         p = q
                
    #     return result
        
def main():
    Z1 = [(0, 3), (0, 0), (0, 1), (3, 0), (3,3)]
    Z2 = [(0, 3), (0, 1), (0, 0), (3, 0), (3, 3)]
    Z3 = [(2, 2), (4, 3), (5, 4), (0, 3), (0, 2), (0, 0), (2, 1), (2, 0), (4, 0)]

    Set_1 = Set(Z1)
    result = Set_1.jarvis_alg()
    for elem in result:
        print(elem)
    print('\n')
    Set_2 = Set(Z2)
    result = Set_2.jarvis_alg()
    for elem in result:
        print(elem)
    print('\n')
    Set_3 = Set(Z3)
    result = Set_3.jarvis_alg()
    for elem in result:
        print(elem)
    print('\n')
    
main()