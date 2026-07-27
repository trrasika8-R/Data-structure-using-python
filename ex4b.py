class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        newNode = Node(data)
        if self.rear is None:
            self.front = self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode
        print(data, "entered the queue")

    def dequeue(self):
        if self.front is None:
            print("Queue is Empty")
        else:
            temp = self.front
            print(temp.data, "left the queue")
            self.front = self.front.next
            if self.front is None:
                self.rear = None

    def display(self):
        if self.front is None:
            print("Queue is Empty")
        else:
            temp = self.front
            print("\nQueue Elements:")
            while temp:
                print(temp.data, end=" ->")
                temp = temp.next
            print("NULL")
queue = Queue()
while True:
    print("\n----- QUEUE MENU -----")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")
    choice = int(input("Enter your Choice: "))
    if choice == 1:
        item = input("Enter car number ")
        queue.enqueue(item)
    elif choice == 2:
        queue.dequeue()
    elif choice == 3:
        queue.display()
    elif choice == 4:
        print("Exiiting Program...")
        break
    else:
        print("Invalid choice")
