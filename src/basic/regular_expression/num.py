import re

phone_re = r'\d{11}'
# match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None。
result = re.match(phone_re, "15302483999")
print(result)
print(result.string)
print(result.re)
print(result.pos)
