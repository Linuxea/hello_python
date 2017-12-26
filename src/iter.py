
from collections import Iterable
from collections import Iterator

""" iterable """
print(isinstance ('abc', Iterable))
print(isinstance (iter([1,2,3]), Iterator))

for x in range(10):
    print(x)

"""
 iterable -> iterator
"""
it = iter([1,2,3,4,5])


while True:
    try:
        temp = next(it)
        print(temp)
    except StopIteration as e :
        print(e)
        break
