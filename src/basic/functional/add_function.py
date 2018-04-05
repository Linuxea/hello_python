# coding=utf-8
import math


def add(f, x, y):
    return f(x) + f(y)


if __name__ == '__main__':
    print(add(math.fabs, -3, 234))
