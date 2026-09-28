n = int(input("Enter the number of vertices: "))

graph = [[] for _ in range(n)]

e = int(input("Enter the number of edges: "))

print("Enter the edges:")

for i in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def bfs(start):
    visited = [False] * n
    queue = [start]
    visited[start] = True

    print("BFS Traversal:", end=" ")

    while queue:
        vertex = queue.pop(0)
        print(vertex, end=" ")

        for neighbour in graph[vertex]:
            if not visited[neighbour]:
                visited[neighbour] = True
                queue.append(neighbour)

    print()



def dfs(start):
    visited = [False] * n
    stack = [start]

    print("DFS Traversal:", end=" ")

    while stack:
        vertex = stack.pop()

        if not visited[vertex]:
            visited[vertex] = True
            print(vertex, end=" ")

            for neighbour in reversed(graph[vertex]):
                if not visited[neighbour]:
                    stack.append(neighbour)

    print()


start = int(input("Enter the starting vertex: "))

bfs(start)
dfs(start)
