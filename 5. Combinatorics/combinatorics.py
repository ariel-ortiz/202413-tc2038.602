
def power_set(s: list) -> list[list]:
    if not s:
        return [[]]
    recursive: list[list] = power_set(s[:-1])
    return recursive + [t + [s[-1]]  for t in recursive]


if __name__ == '__main__':
    print(power_set([]))
    print(power_set(['a']))
    print(power_set(['a', 'b']))
    print(power_set(['a', 'b', 'c']))
