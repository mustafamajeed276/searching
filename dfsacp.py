def dfs(graph, start):

    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                stack.append(neighbor)

    return visited

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'F', 'E'],
    'C': ['A', 'D'],
    'D': ['C'],
    'E': ['B', 'F'],
    'F': ['A', 'E']
}

visited = dfs(graph, 'A')


print(visited)