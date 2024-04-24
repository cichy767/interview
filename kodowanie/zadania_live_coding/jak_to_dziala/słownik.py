# co może być kluczem w słowniku? obiekty niemutowalne - hashable
# kluczem może być string, bool, int, float, complex
# może być też tuple, ale pod warunkiem, że nie ma w sobie mutowalnego obiektu! np. listy

d = {
    'a': 1,
    1: 2,
    (1, 2, 3): [1, 2, 3],
    True: False
}

print(d[True])
