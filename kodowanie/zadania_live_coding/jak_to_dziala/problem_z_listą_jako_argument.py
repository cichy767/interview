# nie powinno się deklarować listy jako argumentu domyślnego, bo potem wszystkie wywołania tej funkcji będą miały referencje do tej samej listy

def test(n, x=[]):
    x.extend((range(n)))
    return x


a = test(2)
b = test(3)

print(b)
