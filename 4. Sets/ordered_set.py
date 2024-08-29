from __future__ import annotations
from collections.abc import Iterator
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
        if value in self:
            return
        self.__count += 1
        new_node: _Node[T] = _Node(value)
        new_node.next = self.__sentinel
        new_node.prev = self.__sentinel.prev
        self.__sentinel.prev.next = new_node
        self.__sentinel.prev = new_node

    def __len__(self) -> int:
        return self.__count

    def __repr__(self) -> str:
        return f'OrderedSet({ list(self) if self else ""})'

    def __iter__(self) -> Iterator[T]:
        current: _Node[T] = self.__sentinel.next
        while current != self.__sentinel:
            yield cast(T, current.info)
            current = current.next

    def __contains__(self, value: T) -> bool:
        for elem in self:
            if elem == value:
                return True
        return False


if __name__ == '__main__':
    a: OrderedSet[int] = OrderedSet()
    print(f'{a = }')
    print(f'{len(a) = }')
    print(f'{bool(a) = }')
    a.add(4)
    a.add(10)
    a.add(10)
    a.add(5)
    print(f'{a = }')
    print(f'{len(a) = }')
    print(f'{bool(a) = }')
    print(f'{4 in a = }')
    print(f'{6 in a = }')
