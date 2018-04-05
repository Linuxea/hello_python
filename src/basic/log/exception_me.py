# coding=utf-8


import logging

logging.basicConfig(filename="exception_test.log", level="DEBUG")


def exception_test():
    """
异常日志记录测试
    """
    try:
        i = 1 / 0
        print(i)
    except Exception as e:
        logging.exception(e)
    finally:
        print("try-exception-finally")


if __name__ == '__main__':
    exception_test()
