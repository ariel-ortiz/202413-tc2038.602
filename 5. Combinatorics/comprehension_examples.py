# [ expression
#   for x in ...
#   for y in ...
#   for z in ...
#   if condition1
#   if condition2
# ]

from pprint import pprint

print([2 * x for x in range(5)])
# [0, 2, 4, 6, 8]

print([x * x for x in range(11) if x % 2 == 0])
# [0, 4, 16, 36, 64, 100]

# Pythagorean triples
pprint([(a, b, c) for a in range(100)
                  for b in range(100)
                  for c in range(100)
                  if a <= b <= c and a ** 2 + b ** 2 == c ** 2])

print({c.upper() for c in 'Hello World' if c not in ' o'})
# {'D', 'E', 'R', 'W', 'H', 'L'}

print([c.upper() for c in 'Hello World' if c not in ' o'])
# ['H', 'E', 'L', 'L', 'W', 'R', 'L', 'D']

print({x : 2 ** x for x in range(10)})
# {0: 1, 1: 2, 2: 4, 3: 8, 4: 16, 5: 32, 6: 64, 7: 128,
#  8: 256, 9: 512}

g = (x * x for x in range(1, 50_000_000))
for elem in g:
    print(elem)
    if elem % 666 == 0:
        break
