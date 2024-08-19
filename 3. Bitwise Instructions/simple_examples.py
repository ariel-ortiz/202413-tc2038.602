x = 5   # 00000101b
y = 8   # 00001000b
z = 10  # 00001010b

print(bin(x))
print(oct(y))
print(hex(z))
print(f'{x & y = :08b}')
print(f'{y & z = :08b}')
print(f'{x | y = :08b}')
print(f'{y | z = :08b}')
print(f'{x ^ y = :08b}')
print(f'{y ^ z = :08b}')
print(f'{~x = :08b}')
print(f'{~y = :08b}')
print(f'{x << 1 = :08b}')
print(f'{y << 2 = :08b}')
print(f'{x >> 1 = :08b}')
print(f'{y >> 2 = :08b}')
print(f'{37 << 3 = }')
print(f'{37 >> 3 = }')
