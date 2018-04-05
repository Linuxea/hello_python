# coding=utf-8

import functools


def map_test():
    """
map test
    """
    # map 函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
    i = (1, 2, 3, 4, 5, 6, 7, 8, 9, 19)
    map_process = map(lambda x: str(x) + ".", i)
    for i in map_process:
        print(i)


def reduce_test():
    """
reduce test
    """
    # 再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]
    # 上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
    i = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print(functools.reduce(lambda x, y: x + y, i, 0))


def filter_test():
    """
filter test
    """
    print("filter test begin")
    i = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    for x in filter(lambda x: x % 2 == 0, i):
        print(x)


def sort_test():
    """
sort test
    """
    print("sort test begin")
    i = (1, 6, 7, 8, 9, 10, 2, 3, 4, 5)
    new_list = sorted(i, key=abs, reverse=True)
    for x in new_list:
        print(x)


if __name__ == '__main__':
    map_test()
    reduce_test()
    filter_test()
    sort_test()
