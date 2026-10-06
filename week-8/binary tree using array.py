class binarytreearray:
    def __init__(self, size):
        self.tree = [None] * size 
        self.size = size

    ##insert root
    def set_root(self, data):
        self.tree[0] = data

    #set left child
    def set_left(self, parent_index, data):
        child_index = 2 * parent_index + 1
        if child_index < self.size:
            self.tree[child_index] = data
        else:
            print("index out of range!")

    #set right child
    def set_right(self, parent_index, data):
        child_index = 2 * parent_index + 2
        if child_index < self.size:
            self.tree[child_index] = data
        else:
            print("index out of range")

    #pre order traversal
    def preorder(self, index=0):
        if index >= self.size or self.tree[index] is None:
            return
        print(self.tree[index], end=" ")
        self.preorder(2 * index + 1)
        self.preorder(2 * index + 2)

    #inorder traversal
    def inorder(self, index=0):
        if index >= self.size or self.tree[index] is None:
            return
        self.inorder(2 * index + 1)
        print(self.tree[index], end=" ")
        self.inorder(2 * index + 2)

    #post order traversal
    def postorder(self, index=0):
        if index >= self.size or self.tree[index] is None:
            return
        self.postorder(2 * index + 1)
        self.postorder(2 * index + 2)
        print(self.tree[index], end=" ")

    #level-order traversal
    def level_order(self):
        for value in self.tree:
            if value is not None:
                print(value, end=" ")

    #display array
    def display(self):
        print("\narray representation")
        for i in range(self.size):
            print(f"index {i}: {self.tree[i]}")

#main program
tree = binarytreearray(7)
tree.set_root('A')
tree.set_left(0, 'B')
tree.set_right(0, 'C')

tree.set_left(1, 'D') 
tree.set_right(1, 'E')
tree.set_left(2, 'F')

tree.display()

print("\npreorder: ", end="")
tree.preorder()

print("\ninorder: ", end="")
tree.inorder()

print("\npostorder: ", end="")
tree.postorder()

print("\nlevel_order: ", end="")
tree.level_order()
