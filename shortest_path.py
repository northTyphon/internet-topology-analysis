from __future__ import annotations
import heapq

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from graph import Graph


def dijkstra(graph: Graph, start: int):
    dist = {node: float("inf") for node in graph.nodes}
    dist[start] = 0
    prev = {node: None for node in graph.nodes}
    heap = [(0, start)]

    while heap:
        current_dist, node = heapq.heappop(heap)
        if current_dist > dist[node]:
            continue
        for neighbor, weight in graph.adj_list[node]:
            new_dist = current_dist + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                prev[neighbor] = node
                heapq.heappush(heap, (new_dist, neighbor))

    return dist, prev


def reconstruct_path(prev: dict, start: int, target: int):
    path = []
    cur = target
    while cur is not None:
        path.append(cur)
        cur = prev[cur]
    path.reverse()
    if path[0] == start:
        return path

    return []
