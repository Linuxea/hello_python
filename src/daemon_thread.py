import threading
from time import sleep


def main():
    print("current thread is: %s" % threading.current_thread().name)
    thread1 = threading.Thread(target=goOne, name="goone")
    thread2 = threading.Thread(target=goTwo, name="gotwo")

    ''' cannot set daemon status of active thread '''
    thread1.daemon = True
    thread2.daemon = True

    thread1.start()
    thread2.start()

    print("main thread exit")


def goOne():
    while True:
        print("i am go one")
        sleep(1)


def goTwo():
    while True:
        print("i am go two")
        sleep(1)


if __name__ == "__main__":
    main()
