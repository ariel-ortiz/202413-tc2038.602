from dataclasses import dataclass


@dataclass
class Item:
    name: str
    weight: int
    value: int


@dataclass
class Entry:
    value: int
    items: list[Item]


Table = list[list[Entry]]


def solve(size: int, items: list[Item]) -> Table:
    dp: Table = [[Entry(0, []) for _ in range(size + 1)]
                 for _ in range(len(items))]
    for i in range(len(items)):
        for j in range(1, size + 1):
            compute_cell(items[i], dp, i, j)
    return dp


def compute_cell(item: Item, dp: Table, i: int, j: int) -> None:
    if i == 0:
        if item.weight <= j:
            dp[i][j] = Entry(item.value, [item])
    else:
        previous: Entry = dp[i - 1][j]
        dp[i][j] = previous
        if item.weight <= j:
            remaining_space: Entry = dp[i - 1][j - item.weight]
            current_value: int = item.value + remaining_space.value
            if current_value > previous.value:
                dp[i][j] = Entry(current_value,
                                 remaining_space.items + [item])


if __name__ == '__main__':
    from pprint import pprint
    table: Table = solve(4, [Item('Stereo', 4, 3_000),
                             Item('Laptop', 3, 2_000),
                             Item('Guitar', 1, 1_500),
                             Item('IPhone', 1, 2_000),
                             Item('Collar', 1, 8_000)])
    pprint(table)
