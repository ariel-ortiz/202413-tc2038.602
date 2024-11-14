
# Fibonacci, common recursive solution
def fib1(n: int) -> int:
    if n <= 1:
        return n
    return fib1(n - 1) + fib1(n - 2)


# Fibonacci, using DP (dynamic programming)
def fib2(n: int) -> int:
    if n == 0:
        return 0
    dp: list[int] = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


if __name__ == '__main__':
    print(f'{fib1(0) = } ')
    print(f'{fib1(1) = } ')
    print(f'{fib1(9) = } ')
    print(f'{fib1(40) = } ')
    print(f'{fib2(0) = } ')
    print(f'{fib2(1) = } ')
    print(f'{fib2(9) = } ')
    print(f'{fib2(40) = } ')
