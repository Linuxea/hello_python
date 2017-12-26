from collections import deque


""" 参数数组 """
de = deque([1,2,3])

print(de)

""" 单个元素都可 """
de.append('a')
de.append('b')

print(de)

de.appendleft('left')

print(de)