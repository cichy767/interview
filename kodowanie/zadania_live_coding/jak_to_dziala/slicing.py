# Jak działa slicing?


foo = [1, 2, 3, 4]

print(foo[1:3])  # [2, 3]
print(foo[-3:-1])  # [2, 3]
print(foo[-1:-3])  # [] to nie działa bo iteracja idzie w złą stronę
print(foo[-1:-3:-1])  # [4, 3] to zadziała po zmieniliśmy kierunek iteracji
print(foo[::-1])  # [4, 3, 2, 1]
