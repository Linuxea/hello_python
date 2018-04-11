# coding=utf-8


class Chain:
    """
chain
    """

    def __init__(self, path=""):
        self.__path = path

    def __getattr__(self, path):
        temp = Chain("%s/%s" % (self.__path, path))
        return temp

    def __str__(self):
        return self.__path

    __repr__ = __str__


print(Chain().one.three.two)
