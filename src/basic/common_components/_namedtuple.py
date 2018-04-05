from collections import namedtuple

if __name__ == '__main__':
    Point = namedtuple("Point", ["x", "y"])
    point = Point(1, 2)
    print(point)
    print(point.x)
    print(point.y)
    print(isinstance(point, Point))

    Coordinate = namedtuple("coordinate", ["x", "y", "z"])
    coordinate = Coordinate(10, 20, 30)
    print(coordinate)
