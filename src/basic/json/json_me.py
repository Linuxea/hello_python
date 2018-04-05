# coding=utf-8


import json


class Person:
    """
Person class for test
    """

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


if __name__ == '__main__':
    person = Person("linuxea", 12, "boy")
    # print(json.dumps(person))  error defined json rule
    print(json.dumps(person, default=lambda x: x.__dict__))
