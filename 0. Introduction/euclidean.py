def gcd(a: int, b: int) -> int:
    if a == b == 0:
        raise ValueError('GCD is not defined for both inputs being zeroo')
    while b != 0:
        a, b = b, a % b
    return abs(a)
