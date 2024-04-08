# co może być kluczem w słowniku? obiekty niemutowalne - hashable

d = {
    'a': 1,
    1: 2,
    (1, 2, 3): [1, 2, 3],
    True: False
}

print(d[True])
