# !5 = 1*2*3*4*5

def strong(n):
    if n == 1:
        return 1
    else:
        return n * strong(n - 1)


print(strong(5))
