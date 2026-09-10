from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start):
        visited = [False] * (max(self.graph) + 1)
        queue = []

        queue.append(start)
        visited[start] = True

        while queue:
            node = queue.pop(0)
            print(node, end=" ")

            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True

if __name__ == "__main__":
    g = Graph()
    g.add_edge(1,6)
    g.add_edge(1,5)
    g.add_edge(1,4)
    g.add_edge(1,3)
    g.add_edge(1,2)
    g.add_edge(1,1)    
    g.add_edge(2,6)
    g.add_edge(2,5,)
    g.add_edge(2,4)
    g.add_edge(2,3)
    g.add_edge(2,2)
    g.add_edge(2,1)
    g.add_edge(3,6)
    g.add_edge(3,5)
    g.add_edge(3,4)
    g.add_edge(3,3)
    g.add_edge(3,2)
    g.add_edge(3,1)    
    g.add_edge(4,6)
    g.add_edge(4,5,)
    g.add_edge(4,4)
    g.add_edge(4,3)
    g.add_edge(4,2)
    g.add_edge(4,1)
    g.add_edge(6,6)
    g.add_edge(6,5)
    g.add_edge(6,4)
    g.add_edge(6,3)
    g.add_edge(6,2)
    g.add_edge(6,1)

    print("Breadth First Traversal starting from vertex 1:")
    g.bfs(1)