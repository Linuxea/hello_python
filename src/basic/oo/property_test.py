class Student(object):

    def __init__(self, value):
        self._score = value

    @property
    def score(self):
        return self._score

    @score.setter
    def set_score(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('分数需要为数字')


s = Student()

# old way
# s.set_score(123)
# print(s.score)
# s.set_score('nothing')
# print(s.score)


# new way
# why error
s.score = 123
print(s.score)
