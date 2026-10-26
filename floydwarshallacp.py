V = 6

INF = 999999

def floydWarshall(graph):

    dist = [row[:] for row in graph]

    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    printSolution(dist)    

def printSolution(dist):
    print("Shortest matrix shows the shortest distances between every pair of vertices")

    for i in range(V):
        for j in range(V):
            if dist[i][j] == INF:
                print("INF", end=" ")
            else:
                print(dist[i][j], end=" ")
        print(" ")

if __name__ == "__main__":
    graph = [[0, 3, INF, INF, 6, INF],
             [INF, 0, 1, INF, INF, INF],
             [INF, INF, 0, 7, INF, 2],
             [INF, INF, INF, 0, INF, 1],
             [INF, INF, INF, 2, 0, INF],
             [INF, INF, INF, INF, 4, 0]]
    floydWarshall(graph)