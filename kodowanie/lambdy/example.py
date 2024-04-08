# lambda to funkcja anonimowa która pozwala na zdefiniowanie jednorazowej funkcji składającej sie z jednego wyrażenia
# tworzy sie ją gdy tworzenie funkcji w klasyczny sposób wydaje się zbędne bo zajmuje więcej miejsca
text_list = ['x', 'xxx', 'xxxxx', 'xxxxxxx', '']

result = list(map(lambda x: len(x), text_list))
print(result)

result = list(filter(lambda x: len(x) > 5, text_list))
print(result)

l = lambda x: x % 2

print(l(5))
