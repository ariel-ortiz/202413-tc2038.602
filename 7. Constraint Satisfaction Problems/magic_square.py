from itertools import permutations
from typing import NamedTuple
from csp import Constraint, CSP


type Grid = list[list[int]]


class GridLocation(NamedTuple):
    row: int
    column: int


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


def assignment_2_grid(assignment: dict[int, GridLocation]) -> Grid:
    square: Grid = [[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]]
    for var, (row, column) in assignment.items():
        square[row][column] = var
    return square


class MagicPuzzleContraint(Constraint[int, GridLocation]):

    def __init__(self, variables: list[int]):
        super().__init__(variables)
        self.variables: list[int] = variables

    def satisfied(self, assignment: dict[int, GridLocation]) -> bool:
        if len(assignment) != len(set(assignment.values())):
            return False
        if len(assignment) < 9:
            return True
        return check_square(assignment_2_grid(assignment))


def solve_csp():
    variables: list[int] = list(range(1, 10))
    all_grid_locations: list[GridLocation] = [GridLocation(r, c) for r in range(3)
                                                                 for c in range(3)]
    domains: dict[int, list[GridLocation]] = {
        var: all_grid_locations for var in variables
    }
    csp: CSP[int, GridLocation] = CSP(variables, domains)
    csp.add_constraint(MagicPuzzleContraint(variables))
    solution: dict[int, GridLocation] | None = csp.backtracking_search()
    if solution:
        print(assignment_2_grid(solution))
    else:
        print('Found no solution :(')


if __name__ == '__main__':
    solve_brute_force()
    solve_csp()
