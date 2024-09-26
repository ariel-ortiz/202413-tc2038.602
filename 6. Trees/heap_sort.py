from heapq import heappush, heappop
from typing import Iterable

# Time complexity: O(N log N)
def heap_sort[T](data: Iterable[T]) -> list[T]:
    tree: list[T] = []
    for elem in data:
        heappush(tree, elem)
    result: list[T] = []
    while tree:
        result.append(heappop(tree))
    return result


if __name__ == '__main__':
    print(heap_sort([15, 42, 8, 4, 16, 23]))
    print(heap_sort('hello world'))
