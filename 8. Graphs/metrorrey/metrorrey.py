from graph import Graph
from generic_search import bfs, Node, node_to_path


if __name__ == '__main__':
    metrorrey: Graph[str] = Graph(["Talleres",
                                   "San Bernabé",
                                   "Unidad Modelo"])
    metrorrey.add_edge_by_vertices("Talleres", "San Bernabé")
    metrorrey.add_edge_by_vertices("San Bernabé", "Unidad Modelo")

    result: Node[str] | None = bfs(
        "Talleres",
        lambda x: x == "Unidad Modelo",
        metrorrey.neighbors_for_vertex
    )

    if result:
        path: list[str] = node_to_path(result)
        print(path)
    else:
        print('No solution found.')
