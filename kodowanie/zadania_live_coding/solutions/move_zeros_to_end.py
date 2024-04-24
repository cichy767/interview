"""
Stwórz funkcję która posortuje liczby w następujący sposób.
Zera mają iść na koniec, a pozostałe liczby bez zmian.

[12, 3, 10, 0, 2, 0] -> [12, 3, 10, 2, 0, 0]
[-10, 0, 20, 0, 5, 9, 13] -> [-10, 20, 5, 9 , 13, 0, 0]
"""


def move_zeros_to_end(nums):
    # Lista do przechowywania niezerowych elementów
    non_zero = [x for x in nums if x != 0]
    # Lista do przechowywania zer
    zeros = [x for x in nums if x == 0]
    # Zwróć połączenie obu list
    return non_zero + zeros


print(move_zeros_to_end([12, 3, 10, 0, 2, 0]))  # Powinno zwrócić [12, 3, 10, 2, 0, 0]
print(move_zeros_to_end([-10, 0, 20, 0, 5, 9, 13]))  # Powinno zwrócić [-10, 20, 5, 9, 13, 0, 0]
