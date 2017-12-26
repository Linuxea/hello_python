class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def say(self):
        print("my name is %s my age is %d" % (self.name, self.age))


studentOne = Student("linuxea", 29)
studentTwo = Student("kobe", 89)


studentOne.say()
studentTwo.say()