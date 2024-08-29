from collections.abc import Iterator

# x = [4, 8, 15, 16, 23, 42]
x = 'Hello'
it = iter(x)
try:
    while True:
        print(next(it))
except StopIteration:
    ...


class Pow2Iterator:

    current: int

    def __init__(self) -> None:
        self.current = 1

    def __next__(self) -> int:
        if self.current > 1000:
            raise StopIteration()
        result: int = self.current
        self.current *= 2
        return result

    def __iter__(self) -> Iterator[int]:
        return self

    def rewind(self) -> None:
        self.current = 1


def pow2fun() -> Iterator[int]:
    current = 1
    while current < 1000:
        yield current
        current *= 2


def example(a: int) -> Iterator[int]:
    yield a
    yield a + 1
    yield a * 2

it = example(5)
print(next(it))  # 5
print(next(it))  # 6
print(next(it))  # 10
# print(next(it))  # StopIteration

print()
for n in example(10):
    print(n)

print()
pow2it = Pow2Iterator()
for n in pow2it:
    print(f'{n = }')

print()
for n in pow2fun():
    print(f'{n = }')
