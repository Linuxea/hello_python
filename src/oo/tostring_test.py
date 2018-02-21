class Student(object):

    def __init__(self, name):
        self.__name = name
    
    def __str__(self):
        return "hi," + self.__name



s = Student('linuxea')
print(s)