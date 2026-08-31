class Node:
    def __init__(self, key, name):
        self.key = key
        self.name = name
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def height(self, node):
        if node is None:
            return 0
        return node.height

    def balance_factor(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def right_rotate(self, y):
        x = y.left
        t = x.right

        x.right = y
        y.left = t

        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        return x

    def left_rotate(self, x):
        y = x.right
        t = y.left

        y.left = x
        x.right = t

        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def insert(self, root, key, name):
        if root is None:
            return Node(key, name)

        if key < root.key:
            root.left = self.insert(root.left, key, name)
        elif key > root.key:
            root.right = self.insert(root.right, key, name)
        else:
            print("Enrollment ID already exists!")
            return root

        root.height = 1 + max(self.height(root.left), self.height(root.right))

        balance = self.balance_factor(root)
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def search(self, root, key):
        if root is None:
            return None

        if key == root.key:
            return root
        elif key < root.key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    def min_value_node(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current

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

            temp = self.min_value_node(root.right)
            root.key = temp.key
            root.name = temp.name
            root.right = self.delete(root.right, temp.key)

        root.height = 1 + max(self.height(root.left), self.height(root.right))

        balance = self.balance_factor(root)
        if balance > 1 and self.balance_factor(root.left) >= 0:
            return self.right_rotate(root)
        if balance > 1 and self.balance_factor(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and self.balance_factor(root.right) <= 0:
            return self.left_rotate(root)
        if balance < -1 and self.balance_factor(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(f"ID: {root.key} | Name: {root.name}")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(f"ID: {root.key} | Name: {root.name}")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(f"ID: {root.key} | Name: {root.name}")

    def count(self, root):
        if root is None:
            return 0
        return 1 + self.count(root.left) + self.count(root.right)

tree = AVLTree()
root = None

while True:
    print("\n--- AVL TREE MENU ---")
    print("1. Insert Enrollment Record")
    print("2. Delete Enrollment Record")
    print("3. Search Student Enrollment")
    print("4. Display All Records (Traversals)")
    print("5. Count Total Enrollments")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        eid = int(input("Enter Enrollment ID: "))
        name = input("Enter Student Name: ")
        root = tree.insert(root, eid, name)
        print("Record inserted successfully.")

    elif choice == 2:
        eid = int(input("Enter Enrollment ID to delete: "))
        if tree.search(root, eid):
            root = tree.delete(root, eid)
            print("Record deleted successfully.")
        else:
            print("Enrollment ID not found.")

    elif choice == 3:
        eid = int(input("Enter Enrollment ID to search: "))
        result = tree.search(root, eid)
        if result:
            print("Enrollment Found!")
            print("ID:", result.key)
            print("Student Name:", result.name)
        else:
            print("Enrollment ID not found.")

    elif choice == 4:
        if not root:
            print("Tree is empty.")
        else:
            print("\n--- SELECT TRAVERSAL TYPE ---")
            print("1. In-order Traversal (Sorted)")
            print("2. Pre-order Traversal (Root First)")
            print("3. Post-order Traversal (Children First)")
            t_choice = int(input("Enter choice: "))
            
            if t_choice == 1:
                print("\nIn-order Traversal:")
                tree.inorder(root)
            elif t_choice == 2:
                print("\nPre-order Traversal:")
                tree.preorder(root)
            elif t_choice == 3:
                print("\nPost-order Traversal:")
                tree.postorder(root)
            else:
                print("Invalid choice!")

    elif choice == 5:
        print("Total Enrollments:", tree.count(root))

    elif choice == 6:
        print("Program terminated.")
        break
    else:
        print("Invalid choice!")
