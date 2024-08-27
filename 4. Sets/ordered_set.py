from __future__ import annotations
from typing import cast


class _Node[N]:

    info: N | None
    next: _Node[N]
    prev: _Node[N]

    def __init__(self, value: N | None = None) -> None:
        self.info = value
        self.next = self
        self.prev = self


class OrderedSet[T]:

    __sentinel: _Node[T]
    __count: int

    def __init__(self) -> None:
        self.__sentinel = _Node()
        self.__count = 0

    def add(self, value: T) -> None:
        # TODO: Check that value is not in self
        self.__count += 1
        new_node: _Node[T] = _Node(value)
        new_node.next = self.__sentinel
        new_node.prev = self.__sentinel.prev
        self.__sentinel.prev.next = new_node
        self.__sentinel.prev = new_node

    def __repr__(self) -> str:
        result: list[T] = []
        current: _Node[T] = self.__sentinel.next
        while current != self.__sentinel:
            result.append(cast(T, current.info))
            current = current.next
        return f'OrderedSet({ result if result else ""})'


if __name__ == '__main__':
    a: OrderedSet[int] = OrderedSet()
    print(a)
    a.add(4)
    a.add(10)
    a.add(5)
    print(a)
