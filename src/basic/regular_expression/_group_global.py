import re

""" 分组 """

if __name__ == '__main__':
    test = "ab cd ef gh ijk 12"
    match = re.findall(r'(\w{2})', test)
    if match:
        print(match)
