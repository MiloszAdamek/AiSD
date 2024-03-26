#do zadania domowego -> pamiętanie ścieżki
class Root:
    
    def __init__(self, root=None):
        self.root = root

    def print_tree(self):
        print("==============")
        self.__print_tree(self.root, 0)
        print("==============")

    def __print_tree(self, node, lvl):
        if node!=None:
            self.__print_tree(node.right, lvl+5)
            
            print()
            print(lvl*" ", node.key, node.value)
     
            self.__print_tree(node.left, lvl+5)

    def print(self):
        """ Print sorted values from tree key: value"""
        return self.__print(self.root)

    def __print(self, current):
        if current.left:
            self.__print(current.left)
        print(f"{current.key} : {current.value}", end=', ')
        if current.right:
            self.__print(current.right)
class Node:
    
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

    def insert(self, key, value): #nie pamieta poprzednika
        if key < self.key:
            if self.left is None:
                self.left = Node(key, value)
            else:
                self.left.insert(key, value)
        elif key > self.key:
            if self.right is None:
                self.right = Node(key, value)
            else:
                self.right.insert(key,value)
        else:
            self.value = value
    
    def search(self, key):
        temp = 0
        if key < self.key:
            if self.left is not None:
                if self.left.key == key:
                    return self.left.value
                else:
                    temp = self.left.search(key)
        elif key > self.key:
            if self.right is not None:
                if self.right.key == key:
                    return self.right.value
                else:
                    temp = self.right.search(key)
        else:
            return self.value
        return temp


    def _delete(self, key): #funkcja zwraca wskaznik na poprzedni node, node do usunięcia i dzieci
        if self.left is None and self.right is None:
            self = None

        if self.left is None and self.right is not None:
            pass

        if self.left is not None and self.right is None:
            pass

        if self.left is not None and self.right is not None:
            pass

    def delete(self, key):
        
        if self is None:
            print('Tree is not exist!')
        return self._delete(key)

    def height(self):
        pass


def main():
    
    BST = Root()
    BST.root = Node(50, 'A')
    data = {15:'B', 62:'C', 5:'D', 20:'E', 58:'F', 
            91:'G', 3:'H', 8:'I', 37:'J', 60:'K', 24:'L'}
    
    for key in data:
        BST.root.insert(key, data[key])

    BST.print_tree()
    BST.print()
    print('\n')
    print(BST.root.search(24))
    BST.root.insert(20, 'AA')
    BST.root.insert(6, 'M')
    BST.root.delete(62)
    BST.root.insert(59, 'N')
    BST.root.insert(100, 'P')
    BST.root.delete(8)
    BST.root.delete(15)
    BST.root.insert(55, 'R')
    BST.root.delete(50)
    BST.root.delete(5)
    BST.root.delete(24)
    print(BST.root.height())
    BST.print()
    BST.print_tree()

main()
