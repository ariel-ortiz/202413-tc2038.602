def baby_sqrt(s: float, delta: float=1e-10) -> float:
    if (s < 0):
        raise ValueError(f"Can't compute the square root of a negative value: {s}")
    x_current: float = s / 2.0
    while True:
        x_new: float = 1.0 / 2.0 * (x_current + s / x_current)
        if abs(x_current - x_new) < delta:
            return x_new
        x_current = x_new


if __name__ == '__main__':
    n: float = 2.0
    print(f'The square root of { n } is equal to: { baby_sqrt(n) }')
