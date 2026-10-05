def dijkstra(graph, source, destination):
    n = len(graph)

    distance = [float('inf')] * n
    previous = [-1] * n
    visited = [False] * n

    distance[source] = 0

    for _ in range(n):
        
        min_distance = float('inf')
        u = -1

        for i in range(n):
            if not visited[i] and distance[i] < min_distance:
                min_distance = distance[i]
                u = i

     
        if u == -1:
            break

        visited[u] = True

      
        for v in range(n):
            if graph[u][v] != 0 and not visited[v]:
                new_distance = distance[u] + graph[u][v]

                if new_distance < distance[v]:
                    distance[v] = new_distance
                    previous[v] = u

    
    if distance[destination] == float('inf'):
        return None, None

   
    path = []
    current = destination

    while current != -1:
        path.append(current)
        current = previous[current]

    path.reverse()

    return path, distance[destination]



n = int(input("Enter number of cities: "))

print("Enter the adjacency matrix:")
graph = []

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

source = int(input("Enter source city: "))
destination = int(input("Enter destination city: "))


source -= 1
destination -= 1

if source < 0 or source >= n or destination < 0 or destination >= n:
    print("Invalid city number.")
else:
    path, distance = dijkstra(graph, source, destination)

    if path is None:
        print("No path exists between the given cities.")
    else:
        print("\nShortest Path:")
        print(" -> ".join(str(city + 1) for city in path))

        print("Shortest Distance:", distance)
