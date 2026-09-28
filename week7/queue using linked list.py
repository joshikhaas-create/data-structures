queue = []
size = int(input("Enter queue size: "))

while True:
    print("\n--- QUEUE ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        if len(queue) == size:
            print("Queue Overflow")
        else:
            value = int(input("Enter value: "))
            queue.append(value)
            print("Value inserted")

    elif choice == 2:
        if len(queue) == 0:
            print("Queue Underflow")
        else:
            print("Deleted:", queue.pop(0))

    elif choice == 3:
        if len(queue) == 0:
            print("Queue is empty")
        else:
            print("Front element:", queue[0])

    elif choice == 4:
        if len(queue) == 0:
            print("Queue is empty")
        else:
            print("Queue:", queue)

    elif choice == 5:
        break

    else:
        print("Invalid choice")
