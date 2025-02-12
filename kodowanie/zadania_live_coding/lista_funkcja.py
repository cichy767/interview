i = [1,2]


def foo():
    pass


def some_fun(i):
    i.append(55)


some_fun(i)
print(i)