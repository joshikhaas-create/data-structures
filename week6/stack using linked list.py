class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    # Push
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print("Value pushed")

    # Pop
    def pop(self):
        if self.top is None:
            print("Stack Underflow")
        else:
            print("Popped:", self.top.data)
            self.top = self.top.next

    # Peek
    def peek(self):
        if self.top is None:
            print("Stack is empty")
        else:
            print("Top element:", self.top.data)

    # Display
    def display(self):
        if self.top is None:
            print("Stack is empty")
        else:
            temp = self.top

            while temp is not None:
                print(temp.data, end=" -> ")
                temp = temp.next

            print("None")


stack = Stack()

while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        value = int(input("Enter value: "))
        stack.push(value)

    elif choice == 2:
        stack.pop()

    elif choice == 3:
        stack.peek()

    elif choice == 4:
        stack.display()

    elif choice == 5:
        break

    else:
        print("Invalid choice")
