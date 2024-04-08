# zwróć temperaturę najbliższą 0, jeśli jest np. -2 i 2 to zwróć 2


def find_closet_to_zero(temperatures: list) -> int:
    temperatures.sort()
    temp_to_compare = abs(temperatures[0])
    # temp_to_compare = [abs(x) for x in temperatures][0]
    print(f"temp_to_compare: {temp_to_compare}")
    print(f"temperatures: {temperatures}")

    for t in temperatures:
        if abs(t) <= abs(temp_to_compare):
            print(f"abs(t): {abs(t)}  abs(temp_to_compare: {abs(temp_to_compare)}")
            temp_to_compare = t
    return temp_to_compare


assert find_closet_to_zero([2, 7, -4, 3, 9]) == 2
assert find_closet_to_zero([2, 7, -4, 3, 9, -2]) == 2, print(find_closet_to_zero([2, 7, -4, 3, 9, -2]))
assert find_closet_to_zero([-2, 7, -4, 3, 9, 2]) == 2, print(find_closet_to_zero([-2, 7, -4, 3, 9, 2]))
assert find_closet_to_zero([-2, 7, 1, -3, 9, 2]) == 1, print(find_closet_to_zero([-2, 7, 1, -3, 9, 2]))
