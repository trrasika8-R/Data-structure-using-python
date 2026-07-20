class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


top = None


def push():
    global top
    data = input("Enter Book title: ")
    newnode = Node(data)

    if top is None:
        top = newnode
    else:
        newnode.next = top
        top = newnode

    print("Book inserted successfully")


def pop():
    global top

    if top is None:
        print("Stack is Empty!!!")
    else:
        temp = top
        print("Deleted Book:", temp.data)
        top = top.next


def display():
    global top

    if top is None:
        print("Stack is Empty!!!")
    else:
        temp = top
        print("Stack:")
        while temp is not None:
            print(temp.data, end=" --> ")
            temp = temp.next
        print("NULL")


while True:
    print("\nSTACK USING LINKED LIST")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        display()
    elif choice == 4:
        print("Program Ended")
        break
    else:
        print("Invalid choice")
