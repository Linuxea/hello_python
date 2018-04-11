# coding=utf-8


class Animal:
    def __init__(self):
        print("I am animal")


class Mammal(Animal):
    def __init__(self):
        print("I am mammal")


class Bird(Animal):
    def __init__(self):
        print("I am bird")


class Flyable:
    def __init__(self):
        print("I can fly")


class Runnable:
    def __init__(self):
        print("I can run")


class Dog(Mammal, Runnable):
    def __init__(self):
        print("I am a dog dog")


class Dove(Bird, Mammal):
    def __init__(self):
        print("I am a bird")


dog = Dog()
bird = Bird()

# 比一般多继承多了层级关系
