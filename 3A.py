stack = []
MAX = 100

def push():
    if len(stack) >= MAX:
        print("Stack Overflow! Cannot add more books.")
    else:
        book = input("Enter Book Title: ")
        stack.append(book)
        print(f'"{book}" added to the stack.')

def pop():
    if len(stack) == 0:
        print("Stack Underflow! No books to remove.")
    else:
        removed_book = stack.pop()
        print(f'"{removed_book}" removed from the stack.')

def display():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("\nBooks in Stack:")
        for i in range(len(stack) - 1, -1, -1):
            print(stack[i])

while True:
    print("\n--- LIBRARY STACK MENU ---")
    print("1. Push Book")
    print("2. Pop Book")
    print("3. Display Books")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        display()
    elif choice == 4:
        print("Exiting program")
        break
    else:
        print("Invalid choice")
