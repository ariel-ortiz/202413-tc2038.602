def is_even(n: int) -> bool:
    return (n & 1) == 0


def is_power_of_2(n: int) -> bool:
    return False if n == 0 else (n & (n - 1)) == 0


def twos_complement(n: int) -> int:
    return ~n + 1
