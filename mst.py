from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from graph import Graph


def find(parent: dict, node: int):
    if parent[node] != node:
        parent[node] = find(parent, parent[node])
    return parent[node]


def union(parent: dict, rank: dict, u: int, v: int):
    root_u = find(parent, u)
    root_v = find(parent, v)
    if root_u == root_v:
        return False
    if rank[root_u] < rank[root_v]:
        root_u, root_v = root_v, root_u
    parent[root_v] = root_u
    if rank[root_u] == rank[root_v]:
        rank[root_u] += 1
    return True


def kruskal(graph: Graph):
    parent = {node: node for node in graph.nodes}
    rank = {node: 0 for node in graph.nodes}

    sorted_edges = sorted(graph.edges, key=lambda e: e[2])

    mst = []
    total_weight = 0

    for u, v, weight in sorted_edges:
        if union(parent, rank, u, v):
            mst.append((u, v, weight))
            total_weight += weight

    return mst, total_weight
