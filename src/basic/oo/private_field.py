__author__ = 'linuxea'
__doc__ = '__私有变量  __特殊变量__  _虽然我可以被访问但是请把我视为私有变量，不要随意访问'


class Me:

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.__age


me = Me('linuxea', 29)

print("%s" % me.get_name())
print("%s" % me.get_age())
''' we cant '''
# print("%s" % me__age)
