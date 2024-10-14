from typing import Iterator
from collections import deque


type Graph = dict[str, list[str]]


def depth_first_search(
        start: str,
        graph: Graph) -> Iterator[str]:
    stack: deque[str] = deque()
    visited: set[str] = set()
    stack.append(start)
    while stack:
        current: str = stack.pop()
        if current not in visited:
            visited.add(current)
            stack.extend(graph[current][::-1])
            yield current


def breadth_first_search(
        start: str,
        graph: Graph) -> Iterator[str]:
    queue: deque[str] = deque()
    visited: set[str] = set()
    queue.append(start)
    while queue:
        current: str = queue.popleft()
        if current not in visited:
            visited.add(current)
            queue.extend(graph[current])
            yield current


if __name__ == '__main__':
    g: Graph = {
        'A': ['B', 'C', 'F'],
        'B': ['A', 'D'],
        'C': ['A', 'E', 'F'],
        'D': ['B'],
        'E': ['C', 'F'],
        'F': ['A', 'C', 'E', 'G'],
        'G': ['F']
    }
    print(list(depth_first_search('A', g)))
    print(list(depth_first_search('G', g)))
    print(list(depth_first_search('D', g)))
    print(list(breadth_first_search('A', g)))
    print(list(breadth_first_search('G', g)))
    print(list(breadth_first_search('D', g)))

    # Do an actual search
    target = 'A'
    start = 'G'
    for i, x in enumerate(breadth_first_search(start, g)):
        if target == x: # Found it in index i
            print(f'Found {target} at index {i}')
            break
    else:
        print(f"Didn't find {target}")
