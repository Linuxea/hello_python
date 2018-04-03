class Student(object):
    """ 和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self """

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_name(self):
        print("name: %s" % self.name)

    def get_score(self):
        print("score: %s" % self.score)

# stu = Student('linuxea', 199)
# stu.get_name()
# stu.get_score()
