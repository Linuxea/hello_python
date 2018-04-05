# coding=utf-8


def return_fun():
    fs = []
    for i in range(3):
        def f():
            return i * i

        fs.append(f)
    return fs


if __name__ == '__main__':
    print(return_fun()[0]())
    print(return_fun()[1]())
    print(return_fun()[2]())
