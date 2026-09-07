class Graph:

    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [[i] for i in range(num_vertices)]

    def add_edge(self, u, v):
        self.adj_list[u].append(v)

    def print_graph(self):
        for i in range(self.num_vertices):
            print(i, "->", self.adj_list[i])


g = Graph(5)

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)

g.print_graph()