class Animal():
    def talk(self) :
        print("I am a animal")


class Dog(Animal) :
    def talk(self):
        print("I am a dog")


class Pig(Animal) :
    pass


class Orange:
    def talk(self):
        print("I am a orange")


def test(x):
    x.talk()


test(Animal())
test(Dog())
test(Pig())
test(Orange())