a = 'hello there'
a = a.replace('there', 'general kenobi')
print(a)

star = ['hello there', 'general kenobi']
b = ' '.join(star)
print(f"b: {b}")

# JOIN DZIAŁA TYLKO ZE STRINGAMI!
result = "".join(["A", "B", 1])
print(result)
