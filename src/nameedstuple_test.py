from collections import namedtuple

Point = namedtuple('point', ['x', 'y'])


p1 = Point(1, 2)

print(p1.x)
print(p1.y)