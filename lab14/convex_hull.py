class Point:
    def __init__(self, x, y, id) -> None:
        self.x = x
        self.y = y
        self.id = id

    def __str__(self):
        return f"({self.x},{self.y})"

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
            string += f"({elem.x}, {elem.y})\n"
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

    def orientation(self, p, q, r):
        direction = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
        if direction == 0:
            return 0
        elif direction > 0:
            return 1
        else:
            return 2

    def is_between_or_collinear(self, p, q, r):
        if (p.x < q.x < r.x) or (r.x < q.x < p.x):
            return True
        elif p.x == q.x == r.x:
            if (p.y < q.y < r.y) or (r.y < q.y < p.y):
                return True
        return False

    def jarvis_alg_1(self):
        result = []
        start = self.find_first_left()
        p = start

        while True:
            result.append(p)
            q = self.dataset[(p.id + 1) % len(self.dataset)]

            for r in self.dataset:
                if self.orientation(p, r, q) == 2:
                    q = r
            p = q
            if p == start:
                break
        
        return result

    def jarvis_alg_2(self):
        result = []
        start = self.find_first_left()
        p = start

        while True:
            result.append(p)
            q = self.dataset[(p.id + 1) % len(self.dataset)]

            for r in self.dataset:
                if self.orientation(p, r, q) == 2:
                    q = r
                elif self.orientation(p, r, q) == 0:
                    if self.is_between_or_collinear(p, q, r):
                        q = r
            p = q
            if p == start:
                break
        
        return result

def main():
    Z1 = [(0, 3), (0, 0), (0, 1), (3, 0), (3, 3)]
    Z2 = [(0, 3), (0, 1), (0, 0), (3, 0), (3, 3)]
    Z3 = [(2, 2), (4, 3), (5, 4), (0, 3), (0, 2), (0, 0), (2, 1), (2, 0), (4, 0)]

    # Set_1 = Set(Z1)
    # result = Set_1.jarvis_alg_1()
    # for elem in result:
    #     print(elem)
    # print('\n')

    # result = Set_1.jarvis_alg_2()
    # for elem in result:
    #     print(elem)
    # print('\n')

    # Set_2 = Set(Z2)
    # result = Set_2.jarvis_alg_1()
    # for elem in result:
    #     print(elem)
    # print('\n')

    # result = Set_2.jarvis_alg_2()
    # for elem in result:
    #     print(elem)
    # print('\n')

    Set_3 = Set(Z3)
    result = Set_3.jarvis_alg_1()
    for elem in result:
        print(elem)
    print('\n')

    result = Set_3.jarvis_alg_2()
    for elem in result:
        print(elem)
    print('\n')

main()
