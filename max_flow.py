from __future__ import annotations
from collections import deque
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from graph import Graph


def bfs_find_path(capacity: dict, source: int, sink: int):
    visited = {source}
    prev = {source: None}
    queue = deque([source])
    while queue:
        node = queue.popleft()
        for neighbor in capacity[node]:
            if neighbor not in visited and capacity[node][neighbor] > 0:
                visited.add(neighbor)
                prev[neighbor] = node
                if neighbor == sink:
                    path = []
                    cur = sink
                    while cur is not None:
                        path.append(cur)
                        cur = prev[cur]
                    path.reverse()
                    return path
                queue.append(neighbor)

    return None


def edmonds_karp(graph: Graph, source: int, sink: int):
    capacity = {node: {} for node in graph.nodes}
    for u, v, w in graph.edges:
        capacity[u][v] = capacity[u].get(v, 0) + w
        capacity[v][u] = capacity[v].get(u, 0) + w

    max_flow = 0
    flow_paths = []

    while True:
        path = bfs_find_path(capacity, source, sink)
        if path is None:
            break

        bottleneck = float("inf")
        for i in range(len(path) - 1):
            bottleneck = min(bottleneck, capacity[path[i]][path[i + 1]])

        for i in range(len(path) - 1):
            u, v = path[i], path[i + 1]
            capacity[u][v] -= bottleneck
            capacity[v][u] += bottleneck

        max_flow += bottleneck
        flow_paths.append((bottleneck, path))

    return max_flow, flow_paths
