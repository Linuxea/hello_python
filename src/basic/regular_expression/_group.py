import re

""" 分组 """

if __name__ == '__main__':
    test = "ab cd ef gh ijk 12"
    match = re.match(r'(\w{2})', test)
    print("原始信息: %s " % match.group(0))
    if match:
        print(match.groups())
