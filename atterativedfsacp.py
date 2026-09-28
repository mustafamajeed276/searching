class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]

    def add_edge(self, v, w):
        self.adj[v].append(w)

    def DFS(self, s):

        visited = [False for i in range(self.V)]

        stack = []

        stack.append(s)

        while (len(stack)):

            s = stack[-1]
            stack.pop()

            if (not visited[s]):
                print(s, end=" ")
                visited[s] = True

            for node in self.adj[s]:
                if (not visited[node]):
                    stack.append(node)

g = Graph(5)
g.add_edge(0, 2)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)
g.add_edge(3, 4)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(4, 2)
g.add_edge(4, 3)
g.add_edge(4, 4)
print("Following is Depth First Traversal (starting from vertex 2)")
g.DFS(0)