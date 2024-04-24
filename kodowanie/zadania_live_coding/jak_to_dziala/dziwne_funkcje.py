funs = []
i = 1
for i in range(4):
    def f():
        print(i)
    funs.append(f)

i = 5
for f in funs:
    f()
