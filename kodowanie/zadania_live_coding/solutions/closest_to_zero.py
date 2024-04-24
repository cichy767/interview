# zwróć temperaturę najbliższą 0, jeśli jest np. -2 i 2 to zwróć 2

#
# def find_closet_to_zero(temperatures: list) -> int:
#     temperatures.sort()
#     temp_to_compare = abs(temperatures[0])
#     # temp_to_compare = [abs(x) for x in temperatures][0]
#     print(f"temp_to_compare: {temp_to_compare}")
#     print(f"temperatures: {temperatures}")
#
#     for t in temperatures:
#         if abs(t) <= abs(temp_to_compare):
#             print(f"abs(t): {abs(t)}  abs(temp_to_compare: {abs(temp_to_compare)}")
#             temp_to_compare = t
#     return temp_to_compare


def find_closest_to_zero(temperatures):
    if not temperatures:
        return None  # Zwróć None, jeśli lista jest pusta
    closest_temp = min(temperatures, key=lambda x: (abs(x), -x))
    print(f"Temperatura najbliższa 0: {closest_temp}")

    return closest_temp


# Lista temperatur do przetestowania
temperatures = [2, 7, -4, 3, 9, -2]

# Wywołanie funkcji i wyświetlenie wyniku
closest_temperature = find_closest_to_zero(temperatures)

assert find_closest_to_zero([2, 7, -4, 3, 9]) == 2
assert find_closest_to_zero([2, 7, -4, 3, 9, -2]) == 2, print(find_closest_to_zero([2, 7, -4, 3, 9, -2]))
assert find_closest_to_zero([-2, 7, -4, 3, 9, 2]) == 2, print(find_closest_to_zero([-2, 7, -4, 3, 9, 2]))
assert find_closest_to_zero([-2, 7, 1, -3, 9, 2]) == 1, print(find_closest_to_zero([-2, 7, 1, -3, 9, 2]))
assert find_closest_to_zero([-2, 7, -1, -3, 9, 2]) == -1
