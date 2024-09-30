
from typing import Iterator
from collections import deque

type Tree = list | None

def in_order(root: Tree) -> Iterator:
    if not root:
        return
    yield from in_order(root[1])
    yield root[0]
    yield from in_order(root[2])

def pre_order(root: Tree) -> Iterator:
    if not root:
        return
    yield root[0]
    yield from pre_order(root[1])
    yield from pre_order(root[2])


def post_order(root: Tree) -> Iterator:
    if not root:
        return
    yield from post_order(root[1])
    yield from post_order(root[2])
    yield root[0]


def level_order(root: Tree) -> Iterator:
    queue: deque[Tree] = deque()
    queue.append(root)
    while queue:
        current: Tree = queue.popleft()
        if current:
            value, left, right = current
            yield value
            queue.append(left)
            queue.append(right)


if __name__ == '__main__':
    root: Tree = [5,
                  [3,
                   None,
                   [4, None, None]],
                  [7,
                   [6, None, None],
                   [10,
                    [8, None, None],
                    None]]]
    print(list(in_order(root)))
    print(list(pre_order(root)))
    print(list(post_order(root)))
    print(list(level_order(root)))

    for elem in in_order(root):
        if elem % 2 == 0:
            print(f'Found first even number: { elem }')
            break
