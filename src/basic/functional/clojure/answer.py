# coding=utf-8


""" 解决闭包不优雅的方式"""


def return_fun():
    fs = []

    def go(j):
        def fun():
            return j * j

        return fun

    for temp in range(3):
        fs.append(go(temp))
    return fs


if __name__ == '__main__':
    result = return_fun()
    print(result)
    for x in result:
        print(x)
        print(x())
