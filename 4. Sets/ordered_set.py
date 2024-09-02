from __future__ import annotations
from collections.abc import Iterator, Iterable
from typing import cast


class _Node[N]:

    info: N | None
    next: _Node[N]
    prev: _Node[N]

    # Complexity: O(1)
    def __init__(self, value: N | None = None) -> None:
        self.info = value
        self.next = self
        self.prev = self


class OrderedSet[T]:

    __sentinel: _Node[T]
    __count: int

    # Complexity: O(N^2), where N is the size of values
    def __init__(self, values: Iterable[T] = []) -> None:
        self.__sentinel = _Node()
        self.__count = 0
        for elem in values:
            self.add(elem)

    # Complexity: O(N)
    def add(self, value: T) -> None:
        if value in self:
            return
        self.__count += 1
        new_node: _Node[T] = _Node(value)
        new_node.next = self.__sentinel
        new_node.prev = self.__sentinel.prev
        self.__sentinel.prev.next = new_node
        self.__sentinel.prev = new_node

    # Complexity: O(1)
    def __len__(self) -> int:
        return self.__count

    # Complexity: O(N)
    def __repr__(self) -> str:
        return f'OrderedSet({ list(self) if self else ""})'

    # Complexity: O(1)
    def __iter__(self) -> Iterator[T]:
        current: _Node[T] = self.__sentinel.next
        while current != self.__sentinel:
            yield cast(T, current.info)
            current = current.next

    # Complexity: O(N)
    def __contains__(self, value: T) -> bool:
        for elem in self:
            if elem == value:
                return True
        return False

    # Complexity: O(N*M + N^2), where N = len(self) and M = len(other)
    def __and__(self, other: OrderedSet[T]) -> OrderedSet[T]:
        result: OrderedSet[T] = OrderedSet()
        for elem in self:
            if elem in other:
                result.add(elem)
        return result

    # Complexity: O(N*M), where N = len(self) and M = len(other)
    def __eq__(self, other: object) -> bool:
        if self is other:
            return True
        if not isinstance(other, OrderedSet):
            return False
        if len(self) != len(other):
            return False
        for elem in self:
            if elem not in other:
                return False
        return True

    def __le__(self, other: OrderedSet[T]) -> bool:
        if len(self) > len(other):
            return False
        for elem in self:
            if elem not in other:
                return False
        return True


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
    b: OrderedSet[int] = OrderedSet([1, 2, 3])
    c: OrderedSet[int] = OrderedSet([3, 1, 2])
    print(f'{b == c = }')
    print(f'{b <= c = }')
    b = OrderedSet([1, 3])
    print(f'{b == c = }')
    print(f'{b <= c = }')
