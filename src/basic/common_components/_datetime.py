from datetime import datetime

if __name__ == '__main__':
    print(datetime.now())
    print(type(datetime.now()))

    print(datetime.now().timestamp())

    print(datetime.utcnow())
