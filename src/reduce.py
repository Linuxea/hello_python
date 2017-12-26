
""" reduce """
from functools import reduce

def acc(x, y):
    return x * 10 + y

result = reduce(acc, [1,2,3,4])
print(result)


result2 = reduce(lambda x,y : x * 10 + y , range(1,10))
print(result2)