import threading


def print_current_thread_info(name):
    print("current thread name is %s, my args is %s." % (threading.current_thread().name, name))


if __name__ == '__main__':
    print_current_thread_info("main")
    for i in range(10):
        t = threading.Thread(target=print_current_thread_info, name="run" + str(i), args=str(i))
        t.start()
        t.join()
    print("all threads done")
