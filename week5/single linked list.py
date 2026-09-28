class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # A. Create linked list
    def create(self):
        n = int(input("Enter number of nodes: "))

        for i in range(n):
            data = int(input("Enter data: "))
            new_node = Node(data)

            if self.head is None:
                self.head = new_node
            else:
                temp = self.head
                while temp.next is not None:
                    temp = temp.next
                temp.next = new_node

    # B. Insert at beginning
    def insert_beginning(self):
        data = int(input("Enter data: "))
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    # C. Insert at end
    def insert_end(self):
        data = int(input("Enter data: "))
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

    # D. Insert at index
    def insert_index(self):
        data = int(input("Enter data: "))
        index = int(input("Enter index: "))

        new_node = Node(data)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head

        for i in range(index - 1):
            if temp is None:
                print("Invalid index")
                return
            temp = temp.next

        if temp is None:
            print("Invalid index")
            return

        new_node.next = temp.next
        temp.next = new_node

    # E. Delete by value
    def delete_value(self):
        value = int(input("Enter value to delete: "))

        if self.head is None:
            print("List is empty")
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        temp = self.head

        while temp.next is not None:
            if temp.next.data == value:
                temp.next = temp.next.next
                return
            temp = temp.next

        print("Value not found")

    # F. Delete first node
    def delete_first(self):
        if self.head is None:
            print("List is empty")
        else:
            self.head = self.head.next

    # G. Delete last node
    def delete_last(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head

        while temp.next.next is not None:
            temp = temp.next

        temp.next = None

    # H. Count number of nodes
    def count(self):
        count = 0
        temp = self.head

        while temp is not None:
            count += 1
            temp = temp.next

        print("Number of nodes:", count)

    # I. Display / Traverse
    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# Main program
list1 = SinglyLinkedList()

while True:

    print("\n----- SINGLY LINKED LIST -----")
    print("A. Create linked list")
    print("B. Insert at beginning")
    print("C. Insert at end")
    print("D. Insert at index")
    print("E. Delete by value")
    print("F. Delete first node")
    print("G. Delete last node")
    print("H. Count number of nodes")
    print("I. Display / Traverse")
    print("J. Exit")

    choice = input("Enter your choice: ").upper()

    if choice == 'A':
        list1.create()

    elif choice == 'B':
        list1.insert_beginning()

    elif choice == 'C':
        list1.insert_end()

    elif choice == 'D':
        list1.insert_index()

    elif choice == 'E':
        list1.delete_value()

    elif choice == 'F':
        list1.delete_first()

    elif choice == 'G':
        list1.delete_last()

    elif choice == 'H':
        list1.count()

    elif choice == 'I':
        list1.display()

    elif choice == 'J':
        print("Program ended")
        break

    else:
        print("Invalid choice")
