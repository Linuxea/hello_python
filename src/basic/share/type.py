

def sum(*lists):
    sum = 0
    for x in lists:
        sum += x
    print(sum)


sum(*[1,2,3,4,5,6,7,8,9,10])