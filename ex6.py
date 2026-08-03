stack = []

def precedence(op):
    if op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2
    elif op == '^':
        return 3
    else:
        return 0

infix = input("Enter Infix Expression: ")
postfix = ""

for ch in infix:
    if ch.isalnum():
        postfix += ch

    elif ch == '(':
        stack.append(ch)

    elif ch == ')':
        while stack and stack[-1] != '(':
            postfix += stack.pop()
        stack.pop()

    else:
        while stack and stack[-1] != '(' and precedence(stack[-1]) >= precedence(ch):
            postfix += stack.pop()
        stack.append(ch)

while stack:
    postfix += stack.pop()

print("Postfix Expression:", postfix)
