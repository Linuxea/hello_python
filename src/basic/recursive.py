
def come():
    i = input("请输入一个东西，以0作为结尾")
    if int(i) == 0:
        return
    else:
        come()

    print(i)

come()