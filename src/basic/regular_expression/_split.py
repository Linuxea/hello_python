import re

if __name__ == '__main__':
    test = "a b c d e  f"
    print(test.split(' '))
    print(re.split(r"\s+", test))
    print(re.split(r"\s{2}", test))
