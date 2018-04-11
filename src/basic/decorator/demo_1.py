# coding=utf-8


class Student:

    # get
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name


stu = Student()
stu.name = "linuxea"
print(stu.name)

# 注意到这个神奇的@property，我们在对实例属性操作的时候，就知道该属性很可能不是直接暴露的，而是通过getter和setter方法来实现的。
