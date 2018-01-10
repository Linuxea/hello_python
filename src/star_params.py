

def start_params(*params):
    for param in params:
        print("param:%s" % (param))



start_params(*[1, 2, 3, 4, 'a', 'b'])