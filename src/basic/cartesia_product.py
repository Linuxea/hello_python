from itertools import product

i = 0
for x, y, z in product(['a', 'b', 'c'], ['d', 'e', 'f'], ['m', 'n']):
    # python大法好
    i += 1
    print(x, y, z)

print(i)
