# coding=utf-8
import math

if __name__ == '__main__':
    print(math.fabs(-1))
    # copy
    abs_point = math.fabs
    print(abs_point(-23))
    # change
    abs_point = 12
    # print(abs_point(-23))
    # not effect
    print(math.fabs(-1))

    # dont do like that
    math.fabs = 10
    print(math.fabs)
