from collections import deque

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

class PalindromeChecker:
    def is_palindrome(self, text):
        stack = Stack()
        queue = Queue()

        # Store characters
        for ch in text:
            if ch.isalnum():
                ch = ch.lower()
                stack.push(ch)
                queue.enqueue(ch)

        # Compare without pop()
        for i in range(len(stack.items)):
            if stack.items[len(stack.items) - 1 - i] != queue.items[i]:
                return False

        return True


# Main Program
text = input("Enter a string: ")

checker = PalindromeChecker()

if checker.is_palindrome(text):
    print("Palindrome")
else:
    print("Not a palindrome")
