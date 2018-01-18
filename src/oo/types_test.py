

__author__ = 'linuxea'


import types
from Student import * 


stu = Student('linuxea', 12)
result = type(stu) == types.FunctionType
print("%s" % result)


# isinstance for oo