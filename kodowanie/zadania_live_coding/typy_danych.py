from copy import deepcopy
# Czym różni się == od is?
# zmienne mutowalne i niemutowalne
# niemutowalne: int, float, complex, krotka, string, bool
# mutowalne: lista, słownik, set
# po dodaniu wartości do zmiennych mutowalnych nadal wskazują na to samo miejsce w pamięci
# przy statemantach if [1,2,3]: dosmth sprawdzany obiekt jest konwertowany do boola. konwersja np. listy do boola daje true lub false w zaleznosci czy jest pusta czy pelna

"""
Technically, it is not quite correct to say an object must be immutable to be used as a dictionary key.
More precisely, an object must be hashable, which means it can be passed to a hash function.
A hash function takes data of arbitrary size and maps it to a relatively simpler fixed-size value called a hash value
(or simply hash), which is used for table lookup and comparison.
"""

"""
is will return True if two variables point to the same object (in memory), == if the objects referred to by the variables are equal.
"""

l1 = [1, 2, 3]
l2 = l1
l1.append(5)
print(f"l1: {l1} id: {id(l1)}, l2: {l2} id: {id(l2)}")

print('----------------------')

l3 = [1, 2, 3]
l4 = l3.copy()
l3.append(5)
print(f"l3: {l3} id: {id(l3)}, l4: {l4} id: {id(l4)}")

l5 = [1, 2, 3, [10, 20]]
l6 = l5
l6.append(10)
l5.append(100)
print(f"l5: {l5}")
print(f"l6: {l6}")

l7 = [1, 2, 3, [10, 20]]
l8 = l7.copy()
l7.append(10)
l8.append(100)
print(f"l7: {l7}")
print(f"l8: {l8}")
l8[3].append(1000)
print(f"l7: {l7}")
print(f"l8: {l8}")

l9 = deepcopy(l8)
l9[3].append(999)
print(f"l8: {l8}")
print(f"l9: {l9}")

print(() == ())  # True
print(() == [])  # False
print([] == [])  # True

print(() is ())  # True
print(() is [])  # False
print([] is [])  # False

print('------------------')
print(f"1 == 1.0: {1 == 1.0}")  # True
print(f"1 is 1.0: {1 is 1.0}")  # False
a = 100000000999
b = 100000000999
print(f"a is b: {a is b}")  # True
print(f"1.0 == 1.0: {1.0 == 1.0}")  # True
print(f"1.0 is 1.0: {1.0 is 1.0}")  # True

print(f"[] is True: {[] is True}")  # False
print(f"() is True: {() is True}")  # False
print(f"(1,2) is True: {(1, 2) is True}")  # False
print(f"[1,2,3] is True: {[1, 2, 3] is True}")  # False

#
