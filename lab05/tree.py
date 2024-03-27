#do zadania domowego -> pamiętanie ścieżki
class Root:
    
    def __init__(self, root=None):
        self.root = root

    def print_tree(self):
        print("\n==============")
        self.__print_tree(self.root, 0)
        print("==============")

    def __print_tree(self, node, lvl):
        if node!=None:
            self.__print_tree(node.right, lvl+5)
            
            print()
            print(lvl*" ", node.key, node.value)
     
            self.__print_tree(node.left, lvl+5)

    def print(self):
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

    def delete(self, key):
        if self is None:
            return None

        if key < self.key:
            self.left = self.left.delete(key)
        elif key > self.key:
            self.right = self.right.delete(key)
        else:
            # 0 children
            if self.left is None and self.right is None:
                return None
            # 1 child
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            # 2 childeren
            succParent = self
            succ = self.right
            while succ.left is not None:
                succParent = succ
                succ = succ.left

            self.key = succ.key
            self.value = succ.value

            if succParent == self:
                self.right = self.right.delete(succ.key)
            else:
                succParent.left = succ.right

        return self

    def height(self):
        if self is None:
            return 0
        else:
            left_height = self.left.height() if self.left else 0
            right_height = self.right.height() if self.right else 0
            return max(left_height, right_height) + 1

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
