n = int(input())
a = list(map(int, input().split()))
x = int(input())

found = False
for i in range(n):
    if a[i] == x:
        found = True
        break

if found:
    print("Linear Search: Element found")
else:
    print("Linear Search: Element not found")

a.sort()
low = 0
high = n - 1
found = False

while low <= high:
    mid = (low + high) // 2
    if a[mid] == x:
        found = True
        break
    elif a[mid] < x:
        low = mid + 1
    else:
        high = mid - 1

if found:
    print("Binary Search: Element found")
else:
    print("Binary Search: Element not found")

