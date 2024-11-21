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


EMPTY_ENTRY: Entry = Entry(0, set())


def knapsack_table(size: int, items: list[Item]) -> Table:
    dp: Table = [[EMPTY_ENTRY for _ in range(size + 1)]
                 for _ in range(len(items))]
    for i, item in enumerate(items):
        for j in range(size + 1):
            dp[i][j] = optimal_entry(item, dp, i, j)
    return dp


def optimal_entry(item: Item, dp: Table, i: int, j: int) -> Entry:
    if i == 0:
        if item.weight <= j:
            return Entry(item.value, {item})
        return EMPTY_ENTRY
    previous_max_entry: Entry = dp[i - 1][j]
    if item.weight <= j:
        remaining_space: Entry = dp[i - 1][j - item.weight]
        possible_better_value: int = item.value + remaining_space.value
        if possible_better_value > previous_max_entry.value:
            return Entry(possible_better_value, remaining_space.items | {item})
    return previous_max_entry


if __name__ == '__main__':
    from pprint import pprint
    # dp: Table = knapsack_table(6, [Item('water', 3, 10),
    #                                Item('book', 1, 3),
    #                                Item('food', 2, 9),
    #                                Item('jacket', 2, 5),
    #                                Item('camera', 1, 6)])
    dp: Table = knapsack_table(4, [Item('laptop', 3, 2_000),
                                   Item('iphone', 1, 2_000),
                                   Item('guitar', 1, 1_500),
                                   Item('collar', 1, 8_000),
                                   Item('stereo', 4, 3_000)])
    pprint(dp)
