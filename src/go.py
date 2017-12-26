
gen = 13

while True:
    i = int(input("请输入一个数字"))
    if i == gen:
        print("good!")
        break
    elif i > gen:
        print("猜大了!")
    else:
        print("猜小了")