# 多线程和多进程最大的不同在于，
# 多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，
# 多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改
# 因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。
import threading

import time

total = 0


def opt_total():
    add_me()
    sub_me()

def add_me():
    global total
    total = total + 1


def sub_me():
    global total
    total = total - 1


def print_total():
    global total
    print("total is %s" % total)


if __name__ == '__main__':
    threads = []
    for i in range(12324):
        t1 = threading.Thread(target=opt_total)
        threads.append(t1)
    print_total()
    for i in threads:
        i.start()
    time.sleep(5)
    print_total()
