SIZE = 5
queue = [0] * SIZE
front = -1
rear = -1

def enqueue(value):
    global front, rear

    if rear == SIZE - 1:
        print("Queue is FULL!")
    else:
        rear += 1
        queue[rear] = value
        print(value, "inserted into queue")

def dequeue():
    global front, rear

    if front == rear:
        print("Queue is EMPTY!")
    else:
        front += 1
        print(queue[front], "deleted from queue")

        if front == rear:
            front = rear = -1

def display():
    if front == rear:
        print("Queue is EMPTY!")
    else:
        print("Queue elements are:")
        for i in range(front + 1, rear + 1):
            print(queue[i], end=" ")
        print()

while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = input("Enter car number: ")
        enqueue(value)

    elif choice == 2:
        dequeue()

    elif choice == 3:
        display()

    elif choice == 4:
        print("Program terminated.")
        break

    else:
        print("Invalid choice!")
