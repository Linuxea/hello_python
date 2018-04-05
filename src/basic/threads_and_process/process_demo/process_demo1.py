import os
from multiprocessing import Process


def run(name):
    print("my name is %s" % name)


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p1 = Process(target=run("hello"))
    p1.start()
    p1.join()
    print("over")
