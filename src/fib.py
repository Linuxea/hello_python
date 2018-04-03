""" 菲波那契函数
"""


class Fib:
    def __init__(self):
        print("init")
        self.a, self.b = 1, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100:
            raise StopIteration
        return self.a


for n in Fib():
    print(n)
