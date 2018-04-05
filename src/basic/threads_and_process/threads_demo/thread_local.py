import threading

local = threading.local()


def print_me():
    name = local.name
    print("name is %s in (%s)" % (name, threading.current_thread().name))


def set_me(name):
    local.name = name
    print_me()


if __name__ == '__main__':
    t1 = threading.Thread(target=set_me, args=("linuxea",))
    t1.start()

    t2 = threading.Thread(target=set_me, args=("bonnie",))
    t2.start()

    t1.join()
    t2.join()
