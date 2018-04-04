for x in range(1, 10):
    for y in range(1, 10):
        if x + 1 == y:
            break
        print("%d * %d = %d\t" % (y, x, x * y), end="")
    print("")
