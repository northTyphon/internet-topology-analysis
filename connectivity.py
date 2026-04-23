from __future__ import annotations
from collections import deque
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from graph import Graph


def bfs(graph: Graph, start: int):
    visited = set()
    queue = deque()
    queue.append(start)
    visited.add(start)
    distances = {start: 0}
    while queue:
        node = queue.popleft()
        for neighbor, weight in graph.adj_list[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                distances[neighbor] = distances[node] + 1
                queue.append(neighbor)

    return visited, distances


def connected_components(graph: Graph):
    visited = set()
    components = []
    for node in graph.nodes:
        if node not in visited:
            component, _ = bfs(graph, node)
            visited.update(component)
            components.append(component)

    return components


def find_bridges(graph: Graph):
    visited = set()
    disc = {}
    low = {}
    timer = [0]
    bridges = []

    def dfs(node, parent):
        visited.add(node)
        disc[node] = low[node] = timer[0]
        timer[0] += 1

        for neighbor, weight in graph.adj_list[node]:
            if neighbor not in visited:
                dfs(neighbor, node)
                low[node] = min(low[node], low[neighbor])
                if low[neighbor] > disc[node]:
                    bridges.append((node, neighbor))
            elif neighbor != parent:
                low[node] = min(low[node], disc[neighbor])

    for node in graph.nodes:
        if node not in visited:
            dfs(node, -1)

    return bridges
