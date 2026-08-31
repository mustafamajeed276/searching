class Graph:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.adj_matrix = [[0 for i in range(num_nodes)] for j in range(num_nodes)]

    def add_edge(self, node1, node2, weight=1):
        self.adj_matrix[node1][node2] = weight
        self.adj_matrix[node2][node1] = weight

    def get_nodes(self):
        return range(self.num_nodes)

    def get_edges(self):
        edges = []
        for i in range(self.num_nodes):
            for j in range(self.num_nodes):
                if self.adj_matrix[i][j] != 0:
                    edges.append((i, j))
        return edges

    def __repr__(self):
        return str(self.adj_matrix)

graph = Graph(3)

graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)

print(graph)