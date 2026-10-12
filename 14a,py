size = 10
hash_table = [None] * size

def insert(roll, name):
    index = roll % size
    for i in range(size):
        pos = (index + i) % size
        if hash_table[pos] is None:
            hash_table[pos] = (roll, name)
            print("Student inserted successfully")
            return
        if hash_table[pos][0] == roll:
            print("Roll number already exists")
            return
    print("Hash table is full")

def search(roll):
    index = roll % size
    for i in range(size):
        pos = (index + i) % size
        if hash_table[pos] is None:
            continue
        if hash_table[pos][0] == roll:
            print("Student Found:", hash_table[pos][1])
            return
    print("Student Not Found")

def delete(roll):
    index = roll % size
    for i in range(size):
        pos = (index + i) % size
        if hash_table[pos] is not None and hash_table[pos][0] == roll:
            hash_table[pos] = "DELETED"
            print("Student deleted successfully")
            return
    print("Student Not Found")

def display():
    print("Hash Table:")
    for i in range(size):
        if hash_table[i] is None:
            print(i, ":", "Empty")
        elif hash_table[i] == "DELETED":
            print(i, ":", "Deleted")
        else:
            print(i, ":", hash_table[i][0], hash_table[i][1])

while True:
    print("\n1.Insert\n2.Search\n3.Delete\n4.Display\n5.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        roll = int(input("Enter roll number: "))
        name = input("Enter student name: ")
        insert(roll, name)
    elif choice == 2:
        roll = int(input("Enter roll number: "))
        search(roll)
    elif choice == 3:
        roll = int(input("Enter roll number: "))
        delete(roll)
    elif choice == 4:
        display()
    elif choice == 5:
        break
    else:
        print("Invalid choice")
