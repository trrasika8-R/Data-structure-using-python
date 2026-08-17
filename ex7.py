class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def insert(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)
    return root
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data)
        inorder(root.right)
root = None
n = int(input("Enter the number of book titles: "))
for i in range(n):
    title = input("Enter book title: ")
    root = insert(root, title)
print("\nBook titles in inorder traversal:")
inorder(root)
