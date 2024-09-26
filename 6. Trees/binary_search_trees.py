
from typing import Iterator


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
