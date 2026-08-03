class Node:
    def __init__(self, coeff, power):
        self.coeff = coeff
        self.power = power
        self.next = None
class Polynomial:
    def __init__(self):
        self.head = None
    def insert(self, coeff, power):
        new = Node(coeff, power)
        if self.head is None:
            self.head = new
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new
    def display(self):
        temp = self.head
        first = True
        while temp:
            if not first:
                print(" + ", end="")
            print(f"{temp.coeff}x^{temp.power}", end="")
            first = False
            temp = temp.next
        print()
def add_poly(p1, p2):
    result = Polynomial()
    t1 = p1.head
    t2 = p2.head
    while t1 and t2:
        if t1.power == t2.power:
            s = t1.coeff + t2.coeff
            if s != 0:
                result.insert(s, t1.power)
            t1 = t1.next
            t2 = t2.next
        elif t1.power < t2.power:
            result.insert(t1.coeff, t1.power)
            t1 = t1.next
        else:
            result.insert(t2.coeff, t2.power)
            t2 = t2.next
    while t1:
        result.insert(t1.coeff, t1.power)
        t1 = t1.next
    while t2:
        result.insert(t2.coeff, t2.power)
        t2 = t2.next
    return result
p1 = Polynomial()
p2 = Polynomial()
n1 = int(input("Enter number of terms in the first polynomial: "))
print("Enter coefficient and power:")
for _ in range(n1):
    c, p = map(int, input().split())
    p1.insert(c, p)
n2 = int(input("Enter number of terms in the second polynomial: "))
print("Enter coefficient and power:")
for _ in range(n2):
    c, p = map(int, input().split())
    p2.insert(c, p)
print("First polynomial:")
p1.display()
print("Second polynomial:")
p2.display()
result = add_poly(p1, p2)
print("Resultant polynomial:")
result.display()
