import random

"""
1 2 3
2 1 3
2 3 1
3 2 1
"""

random_numbers = [random.randint(0, 10) for _ in range(10)]

while 1:
    swapped = False
    for i in range(len(random_numbers)):
        a = random_numbers[i]
        try:
            b = random_numbers[i + 1]
        except IndexError:
            continue
        if a < b:
            random_numbers[i] = b
            random_numbers[i + 1] = a
            swapped = True

    if not swapped:
        break
