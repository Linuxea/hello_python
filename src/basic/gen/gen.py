# coding=utf-8


def get():
    """
:return range(1000) generator
    """
    for i in range(1000):
        yield i


if __name__ == '__main__':
    num_yield = get()
    for x in num_yield:
        print(x)
