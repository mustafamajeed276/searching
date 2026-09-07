class Graph:

    def __init__(self):
        self.nodes = set()
        self.edges = {}

    def add_node(self, node):
        self.nodes.add(node)

    def add_edge(self, node1, node2, weight=1):
        if node1 not in self.nodes:
            self.nodes.add(node1)
        if node2 not in self.nodes:
            self.nodes.add(node2)

        if node1 not in self.edges:
            self.edges[node1] = set()
        self.edges[node1].add((node2, weight))

        if node2 not in self.edges:
            self.edges[node2] = set()
        self.edges[node2].add((node1, weight))

    def get_nodes(self):
        return self.nodes

    def get_edges(self):
        return self.edges

    def __repr__(self):
        return str(self.nodes) + " -> " + str(self.edges)

graph = Graph()

graph.add_node("E")
graph.add_node("F")
graph.add_node("G")

graph.add_edge("E", "F")
graph.add_edge("E", "G")
graph.add_edge("F", "G")

print(graph)