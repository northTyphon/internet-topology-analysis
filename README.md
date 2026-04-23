# Internet Topology Analysis

Graph analysis of internet autonomous system (AS) topology using the CAIDA AS
Relationships dataset (November 2007).

Nodes represent autonomous systems, independently managed networks such as ISPs,
universities and tech companies. Edges represent peering relationships between them.

## Algorithms

All algorithms are implemented from scratch in Python, using
igraph for graph loading and representation.

- **Connectivity:** BFS, connected components, bridge detection (Tarjan)
- **Shortest Path:** Dijkstra with path reconstruction
- **Minimum Spanning Tree:** Kruskal with Union-Find
- **Maximum Flow:** Edmonds-Karp (BFS-based Ford-Fulkerson)

## Setup

```bash
git clone https://github.com/northTyphon/internet-topology-analysis
cd internet-topology-analysis
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Place the dataset in `data/` as described in `data/README.md`, then:

```bash
python main.py
```

## Dataset

See 'data/README.md' for download instructions.
Licensed under the CAIDA Acceptable Use Agreement, not redistributed in this repository.

A subgraph of 400 nodes is extracted via BFS from the highest-degree node.
To use a larger subgraph, modify the `target_size` parameter in `Graph.from_file()`
in `graph.py`. Note that Edmonds-Karp scales poorly on large graphs (O(VE²)).
