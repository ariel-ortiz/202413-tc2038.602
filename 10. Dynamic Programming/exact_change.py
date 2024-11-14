
def coin_change(coins: list[int], amount: int) -> list[int] | None:
    omega: list[int] = [0] * (amount + 1)
    dp: list[list[int]] = [omega] * (amount + 1)
    dp[0] = []
    i: int
    for i in range(1, amount + 1):
        coin: int
        for coin in coins:
            if i >= coin:
                candidate: list[int] = dp[i - coin] + [coin]
                if len(candidate) < len(dp[i]):
                    dp[i] = candidate
    if dp[amount] is omega:
        return None
    return sorted(dp[amount], reverse=True)


if __name__ == '__main__':
    for i in range(101):
        print(i, coin_change([1, 2, 5, 10, 20], i))
