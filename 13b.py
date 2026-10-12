n = int(input())
a = list(map(int, input().split()))

b = a.copy()
for i in range(n):
    for j in range(0, n - i - 1):
        if b[j] > b[j + 1]:
            b[j], b[j + 1] = b[j + 1], b[j]
print("Bubble Sort:", *b)

c = a.copy()
for i in range(1, n):
    key = c[i]
    j = i - 1
    while j >= 0 and c[j] > key:
        c[j + 1] = c[j]
        j -= 1
    c[j + 1] = key
print("Insertion Sort:", *c)

d = a.copy()
for i in range(n):
    least = i
    for j in range(i + 1, n):
        if d[j] < d[least]:
            least = j
    d[i], d[least] = d[least], d[i]
print("Selection Sort:", *d)
