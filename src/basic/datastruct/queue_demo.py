from queue import Queue

queue = Queue()


def put(elements):
    for i in elements:
        queue.put(i)
    print("put ok")


def get():
    while True:
        some = queue.get(timeout=4)
        if some is not None:
            print("some is: %s" % some)
        else:
            break


if __name__ == '__main__':
    put(["a", "b", "c", "d"])
    get()
