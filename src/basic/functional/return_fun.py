# coding=utf-8


def return_fun():
    """
return a function
    :return:
    """

    def add(x, y):
        """
return result of x plus y
        :param x:
        :param y:
        :return:
        """
        return x + y

    return add


if __name__ == '__main__':
    add = return_fun()
    print(add)
    print(add(1, 2))

    # not the same function False
    print(return_fun() == return_fun())
