import threading
from time import sleep


def main():
    print("current thread is: %s" % (threading.current_thread().name))
    thread1 = threading.Thread(target=goOne, name="goone")
    thread2 = threading.Thread(target=goTwo, name="gotwo")
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()


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
