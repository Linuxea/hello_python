# coding=utf-8


def return_fun():
    return lambda x, y: x + y


if __name__ == '__main__':
    result = return_fun()
    print(result)
    print(result(1, 2))
    print(result(3, 4))
