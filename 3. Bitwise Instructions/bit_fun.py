def is_even(n: int) -> bool:
    return (n & 1) == 0


def is_power_of_2(n: int) -> bool:
    return False if n == 0 else (n & (n - 1)) == 0


def twos_complement(n: int) -> int:
    return ~n + 1


def int_mul(n: int, m: int) -> int:
    negative: bool = (n < 0) ^ (m < 0)
    n = abs(n)
    m = abs(m)
    result: int = 0
    while n:
        if n & 1:
            result += m
        n >>= 1
        m <<= 1
    return -result if negative else result


def bin_with_num_bits(n: int, b: int) -> str:
    if b < 1:
        raise ValueError(
            f'The number of bits provided ({b}) should be at least 1')
    if n >= (1 << b) or n < -(1 << (b - 1)):
        raise ValueError(f"Can't fit {n} into {b} bits")
    if n < 0:
        n = (1 << b) + n
    return f'{n:0{b}b}'
