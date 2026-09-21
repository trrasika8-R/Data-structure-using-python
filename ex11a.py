n = int(input("Enter number of people: "))


matrix = [[0 for j in range(n)] for i in range(n)]

e = int(input("Enter number of connections: "))


for i in range(e):
    print("Enter connection", i + 1, ":")
    u = int(input("Enter first person: "))
    v = int(input("Enter second person: "))

    matrix[u][v] = 1
    matrix[v][u] = 1



print("\nAdjacency Matrix:")

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print()



adj_list = [[] for i in range(n)]

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            adj_list[i].append(j)



print("\nAdjacency List:")

for i in range(n):
    print(i, "->", adj_list[i])
