from graph import Graph
from connectivity import bfs, connected_components, find_bridges
from shortest_path import dijkstra, reconstruct_path
from mst import kruskal
from max_flow import edmonds_karp


def main():
    print("Loading graph")
    g = Graph.from_file("data/dataset.txt")
    print(f"Nodes: {len(g.nodes)}, Edges: {len(g.edges)}\n")

    print(f"Available nodes: {g.nodes[:10]}... (0 to {max(g.nodes)})")
    source = int(input("Enter source node for shortest path: "))
    target = int(input("Enter target node for shortest path: "))

    while source not in g.nodes or target not in g.nodes:
        print("Invalid node. Enter different nodes.")
        source = int(input("Enter source node for shortest path: "))
        target = int(input("Enter target node for shortest path: "))

    print("=" * 50)
    print("CONNECTIVITY")
    print("=" * 50)

    components = connected_components(g)
    print(f"Number of components: {len(components)}")
    print(f"Largest component: {len(components[0])} nodes")

    bridges = find_bridges(g)
    print(f"Number of bridges: {len(bridges)}")
    print(f"Sample bridges: {bridges[:3]}")

    start = g.nodes[0]
    visited, distances = bfs(g, start)
    print(f"BFS from node {start}: reached {len(visited)} nodes")
    print(f"Sample distances: {list(distances.items())[:3]}")

    print("\n" + "=" * 50)
    print("SHORTEST PATH (Dijkstra)")
    print("=" * 50)

    dist, prev = dijkstra(g, source)
    path = reconstruct_path(prev, source, target)
    print(f"Source: {source}, Target: {target}")
    print(f"Shortest distance: {dist[target]}")
    print(f"Path: {path}")

    print("\n" + "=" * 50)
    print("MINIMUM SPANNING TREE (Kruskal)")
    print("=" * 50)

    mst, total_weight = kruskal(g)
    print(f"MST edges: {len(mst)}")
    print(f"Total weight: {total_weight}")
    print(f"Sample MST edges: {mst[:3]}")

    print("\n" + "=" * 50)
    print("MAXIMUM FLOW (Edmonds-Karp)")
    print("=" * 50)

    source = g.nodes[0]
    sink = g.nodes[-1]
    max_flow, flow_paths = edmonds_karp(g, source, sink)
    print(f"Source: {source}, Sink: {sink}")
    print(f"Maximum flow: {max_flow}")
    print(f"Number of augmenting paths: {len(flow_paths)}")
    print(f"Sample path: {flow_paths[0] if flow_paths else 'none'}")


if __name__ == "__main__":
    main()
