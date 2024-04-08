# filter()
text_list = ['x', 'xxx', 'xxxxx', 'xxxxxxx', '']
result = list(filter(lambda x: len(x) > 5, text_list))


# map()

def addition(n):
    return n + n


# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))

# zip()
a = [1, 2, 3]
b = ['a', 'b', 'c']

c = zip(a, b)
print(list(c))
