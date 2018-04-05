# coding=utf-8


def fib(n):
    """
common loop
    :param n:
    """
    first, second = 1, 1
    for i in range(n):
        first, second = second, first + second
        print("%s" % first)


# fib(99)


def fib_gen(n):
    """
fib function by generator
    :param n:
    """
    first, second = 1, 1
    for i in range(n):
        first, second = second, first + second
        yield first


for x in fib_gen(100):
    print(x)
