class Student:
    __slots__ = ('__name__', '__age__')  # 用tuple定义允许绑定的属性名称

    def __init__(self, name, age):
        self.__name__ = name
        self.__age__ = age

    def print_me(self):
        print("%s's age is %s" % (self.__name__, self.__age__))


s = Student("linuxea", 90)
s.print_me()
print("dir s:%s" % dir(s))
print("s is:%s" % s)

# error because of __slots__
# s.ok = 12
# print("s.ok is:%s" % s.ok)
