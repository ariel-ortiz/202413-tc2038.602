from dataclasses import dataclass


@dataclass(frozen=True)
class Item:
    name: str
    weight: int
    value: int


@dataclass
class Entry:
    value: int
    items: set[Item]


type Table = list[list[Entry]]


def solve(size: int, items: list[Item]) -> Table:
    dp: Table = [[Entry(0, set()) for _ in range(size + 1)]
                 for _ in range(len(items))]
    for i in range(len(items)):
        for j in range(1, size + 1):
            compute_cell(items[i], dp, i, j)
    return dp


def compute_cell(item: Item, dp: Table, i: int, j: int) -> None:
    if i == 0:
        if item.weight <= j:
            dp[0][j] = Entry(item.value, {item})
        return
    previous_max: Entry = dp[i - 1][j]
    dp[i][j] = previous_max
    if item.weight <= j:
        remaining_space: Entry = dp[i - 1][j - item.weight]
        current_value = item.value + remaining_space.value
        if current_value > previous_max.value:
            dp[i][j] = Entry(current_value, remaining_space.items | {item})


if __name__ == '__main__':
    from pprint import pprint
    # dp: Table = solve(6, [Item('water', 3, 10),
    #                       Item('book', 1, 3),
    #                       Item('food', 2, 9),
    #                       Item('jacket', 2, 5),
    #                       Item('camera', 1, 6)])
    dp: Table = solve(4, [Item('laptop', 3, 2_000),
                          Item('iphone', 1, 2_000),
                          Item('guitar', 1, 1_500),
                          Item('collar', 1, 8_000),
                          Item('stereo', 4, 3_000)])
    pprint(dp)
