import os
import random
import time
from multiprocessing.pool import Pool


def run(name):
    start_time = time.time()
    print('Run task %s (%s)...' % (name, os.getpid()))
    print("my name is %s " % name)
    time.sleep(random.randint(3, 10))
    end_time = time.time()
    print("spend time is %s." % (end_time - start_time))


def call_me(times):
    print("%s call back over" % times)


if __name__ == '__main__':
    print('Run task %s ...' % os.getpid())
    pool = Pool(4)
    for i in range(5):
        """ 同步与异步的参数区别 """
        pool.apply_async(run, args=(i,), callback=call_me(i))
    print("waiting ... ... ")
    # 对Pool对象调用join()
    # 方法会等待所有子进程执行完毕，调用join()
    # 之前必须先调用close()，调用close()
    # 之后就不能继续添加新的Process了。
    pool.close()
    pool.join()
    print("all process is done.")
