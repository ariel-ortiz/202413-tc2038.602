from heapq import heapify, heappop
from typing import NamedTuple

type WeightedGraph = dict[str, set[tuple[str, int]]]


class Edge(NamedTuple):

    weight: int
    u: str
    v: str

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Edge):
            return False
        return (self.weight == other.weight
                and ((self.u == other.u and self.v == other.v)
                     or (self.u == other.v and self.v == other.u)))

    def __hash__(self) -> int:
        return hash(self.u) + hash(self.v) + hash(self.weight)


def make_heap(graph: WeightedGraph) -> list[Edge]:
    result: set[Edge] = set()
    u: str
    neighbors: set[tuple[str, int]]
    for u, neighbors in graph.items():
        v: str
        weight: int
        for v, weight in neighbors:
            result.add(Edge(weight, u, v))
    queue: list[Edge] = list(result)
    heapify(queue)
    return queue


def add_edge(graph: WeightedGraph, edge: Edge) -> None:
    weight, u, v = edge
    graph[u].add((v, weight))
    graph[v].add((u, weight))


def remove_edge(graph: WeightedGraph, edge: Edge) -> None:
    weight, u, v = edge
    graph[u].remove((v, weight))
    graph[v].remove((u, weight))


def has_cycle(
        initial: str,
        graph: WeightedGraph,
        visited: set[str] | None = None,
        parent: str | None = None) -> bool:
    if visited is None:
        visited = set()
    visited.add(initial)
    for vertex, _ in graph[initial]:
        if vertex in visited:
            if vertex != parent:
                return True
        elif has_cycle(vertex, graph, visited, initial):
            return True
    return False


def kruskal_mst(graph: WeightedGraph) -> tuple[int, WeightedGraph]:
    queue: list[Edge] = make_heap(graph)
    result: WeightedGraph = {k: set() for k in graph}
    remaining_edges: int = len(graph) - 1
    total: int = 0
    visited: set[str] = set()
    while remaining_edges:
        edge: Edge = heappop(queue)
        add_edge(result, edge)
        if (edge.u in visited
                and edge.v in visited
                and has_cycle(edge.u, result)):
            remove_edge(result, edge)
        else:
            visited.add(edge.u)
            visited.add(edge.v)
            total += edge.weight
            remaining_edges -= 1
    return (total, result)


if __name__ == '__main__':
    from pprint import pprint
    g1 = {
        'A': {('B', 5), ('C', 4), ('D', 2), ('E', 10)},
        'B': {('A', 5), ('C', 9), ('D', 6), ('E', 7)},
        'C': {('A', 4), ('B', 9), ('D', 8), ('E', 1)},
        'D': {('A', 2), ('B', 6), ('C', 8), ('E', 3)},
        'E': {('A', 10), ('B', 7), ('C', 1), ('D', 3)}
    }
    pprint(kruskal_mst(g1))
    g2 = {
        'A': {('B', 10), ('C', 5)},
        'B': {('A', 10), ('C', 1), ('D', 8)},
        'C': {('A', 5), ('B', 1), ('D', 3), ('E', 6)},
        'D': {('B', 8), ('C', 3), ('E', 4)},
        'E': {('C', 6), ('D', 4), ('F', 7), ('G', 15)},
        'F': {('E', 7), ('G', 2), ('H', 5)},
        'G': {('E', 15), ('F', 2), ('H', 9)},
        'H': {('F', 5), ('G', 9)}
    }
    pprint(kruskal_mst(g2))
