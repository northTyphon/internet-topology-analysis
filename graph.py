import igraph as ig
import random


class Graph:
    def __init__(self):
        self.ig = None
        self.nodes = []
        self.edges = []
        self.adj_list = {}
        self.adj_matrix = []

    @classmethod
    def from_file(cls, path, target_size=400):
        edges = {}
        with open(path, "r") as f:
            for line in f:
                if line.startswith("#"):
                    continue
                parts = line.strip().split()
                u, v, rel = int(parts[0]), int(parts[1]), int(parts[2])
                edges[(min(u, v), max(u, v))] = rel

        edges = [(u, v, rel) for (u, v), rel in edges.items()]

        ig_graph = ig.Graph.TupleList([(u, v) for u, v, rel in edges], directed=False)
        edge_rel = {(min(u, v), max(u, v)): rel for u, v, rel in edges}

        components = ig_graph.connected_components()
        largest = components.giant()

        start = largest.vs.select(_degree=largest.maxdegree())[0].index
        visited = []
        queue = [start]
        seen = set([start])

        while queue and len(visited) < target_size:
            node = queue.pop(0)
            visited.append(node)
            for neighbor in largest.neighbors(node):
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)

        subgraph = largest.induced_subgraph(visited)

        random.seed(42)

        def rel_to_weight(rel):
            if rel == 2:
                return random.randint(1, 20)
            elif rel == 0:
                return random.randint(10, 80)
            else:
                return random.randint(50, 200)

        subgraph.es["weight"] = [
            rel_to_weight(
                edge_rel.get((min(e.source, e.target), max(e.source, e.target)), 0)
            )
            for e in subgraph.es
        ]

        obj = cls()
        obj.ig = subgraph

        obj.nodes = [v.index for v in subgraph.vs]

        obj.edges = [(e.source, e.target, e["weight"]) for e in subgraph.es]

        obj.adj_list = {v.index: [] for v in subgraph.vs}
        for e in subgraph.es:
            obj.adj_list[e.source].append((e.target, e["weight"]))
            obj.adj_list[e.target].append((e.source, e["weight"]))

        n = len(obj.nodes)
        obj.adj_matrix = [[0] * n for _ in range(n)]
        for u, v, w in obj.edges:
            obj.adj_matrix[u][v] = w
            obj.adj_matrix[v][u] = w

        return obj


if __name__ == "__main__":
    g = Graph.from_file("data/dataset.txt")
    print(f"Nodes: {len(g.nodes)}, Edges: {len(g.edges)}")
    print(f"Sample adj_list[1]: {g.adj_list[1][:3]}")
    print(f"Matrix[1][2]: {g.adj_matrix[1][2]}")
