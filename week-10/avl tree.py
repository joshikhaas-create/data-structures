
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:

    def height(self, root):
        if root is None:
            return 0
        return root.height

    def balance(self, root):
        if root is None:
            return 0
        return self.height(root.left) - self.height(root.right)

    # Right Rotation
    def right_rotate(self, y):
        x = y.left
        t = x.right

        x.right = y
        y.left = t

        y.height = 1 + max(self.height(y.left),
                           self.height(y.right))
        x.height = 1 + max(self.height(x.left),
                           self.height(x.right))

        return x

    # Left Rotation
    def left_rotate(self, x):
        y = x.right
        t = y.left

        y.left = x
        x.right = t

        x.height = 1 + max(self.height(x.left),
                           self.height(x.right))
        y.height = 1 + max(self.height(y.left),
                           self.height(y.right))

        return y

    # Insert
    def insert(self, root, key):
        if root is None:
            return Node(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root

        root.height = 1 + max(self.height(root.left),
                              self.height(root.right))

        b = self.balance(root)

        # LL Case
        if b > 1 and key < root.left.key:
            return self.right_rotate(root)

        # RR Case
        if b < -1 and key > root.right.key:
            return self.left_rotate(root)

        # LR Case
        if b > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # RL Case
        if b < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    # Find smallest node
    def min_value(self, root):
        temp = root
        while temp.left is not None:
            temp = temp.left
        return temp

    # Delete
    def delete(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)

        elif key > root.key:
            root.right = self.delete(root.right, key)

        else:
            if root.left is None:
                return root.right

            elif root.right is None:
                return root.left

            temp = self.min_value(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        if root is None:
            return root

        root.height = 1 + max(self.height(root.left),
                              self.height(root.right))

        b = self.balance(root)

        # LL Case
        if b > 1 and self.balance(root.left) >= 0:
            return self.right_rotate(root)

        # LR Case
        if b > 1 and self.balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # RR Case
        if b < -1 and self.balance(root.right) <= 0:
            return self.left_rotate(root)

        # RL Case
        if b < -1 and self.balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    # Search
    def search(self, root, key):
        if root is None:
            return False

        if root.key == key:
            return True

        if key < root.key:
            return self.search(root.left, key)

        return self.search(root.right, key)

    # Inorder Traversal
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

    # Preorder Traversal
    def preorder(self, root):
        if root:
            print(root.key, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    # Postorder Traversal
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.key, end=" ")

    # Display Height and Balance Factor
    def show_details(self, root):
        if root:
            self.show_details(root.left)
            print("Node:", root.key,
                  "Height:", root.height,
                  "Balance Factor:", self.balance(root))
            self.show_details(root.right)

    # Display Tree
    def display(self, root, level=0):
        if root:
            self.display(root.right, level + 1)
            print("    " * level, root.key)
            self.display(root.left, level + 1)


# Main Program
tree = AVLTree()
root = None

while True:
    print("\n--- AVL TREE OPERATIONS ---")
    print("1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Inorder Traversal")
    print("5. Preorder Traversal")
    print("6. Postorder Traversal")
    print("7. Display Tree")
    print("8. Height and Balance Factor")
    print("9. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter value: "))
        root = tree.insert(root, value)
        print("Value inserted")

    elif choice == 2:
        value = int(input("Enter value to delete: "))
        if tree.search(root, value):
            root = tree.delete(root, value)
            print("Value deleted")
        else:
            print("Value not found")

    elif choice == 3:
        value = int(input("Enter value to search: "))
        if tree.search(root, value):
            print("Element found")
        else:
            print("Element not found")

    elif choice == 4:
        print("Inorder:")
        tree.inorder(root)
        print()

    elif choice == 5:
        print("Preorder:")
        tree.preorder(root)
        print()

    elif choice == 6:
        print("Postorder:")
        tree.postorder(root)
        print()

    elif choice == 7:
        print("AVL Tree:")
        tree.display(root)

    elif choice == 8:
        if root is None:
            print("Tree is empty")
        else:
            tree.show_details(root)

    elif choice == 9:
        print("Program ended")
        break

    else:
        print("Invalid choice")
