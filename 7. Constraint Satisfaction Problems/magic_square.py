from itertools import permutations
from math import factorial


type Grid = list[list[int]]


def check_square(square: Grid) -> bool:
    ((a, b, c),
     (d, e, f),
     (g, h, i)) = square
    return    ((a + b + c)     # Rows
            == (d + e + f)
            == (g + h + i)
            == (a + d + g)     # Columns
            == (b + e + h)
            == (c + f + i)
            == (a + e + i)     # Diagonals
            == (g + e + c))


def solve_brute_force():
    for p in permutations(range(1, 10)):
        grid: Grid = partition(list(p), 3)
        if check_square(grid):
            print(grid)
            break


def partition(s: list, n: int) -> list[list]:
    return [s[i:i + n] for i in range(0, len(s) // n * n, n)]


if __name__ == '__main__':
    solve_brute_force()
