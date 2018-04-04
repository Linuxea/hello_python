
""" for small white """

li = "I love python".split("这个为空在ｊａｖａ 里面是可以的，可是在ｐｙｔｈｏｎ不行，烦恼啊")

print(li)


result = list(map(lambda x: x, "I love python"))
print(result)
