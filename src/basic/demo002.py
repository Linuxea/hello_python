def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


result = fact(1000)

print(result)
