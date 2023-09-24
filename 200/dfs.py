class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v):
        self.adj_list.setdefault(u, []).append(v)
        self.adj_list.setdefault(v, []).append(u)

    def dfs(self, start_node, visited=set()):
        


# Example usage
graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 5)

print("DFS traversal starting from node 0:")
graph.dfs(0)
