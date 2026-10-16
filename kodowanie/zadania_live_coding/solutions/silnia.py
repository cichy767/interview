# 5! = 1 * 2 * 3 * 4 * 5

def silnia(n):
    if not isinstance(n, int):
        raise TypeError('Silnia wymaga liczby całkowitej.')
    if n == 0:
        return 1
    elif n < 0:
        raise ValueError('Nie można policzyć silni z liczby ujemnej.')

    r = 1
    for num in range(1, n + 1):
        r *= num

    return r


def silnia_req(n):
    """Wariant rekurencyjny; dla dużych n użyj wersji iteracyjnej."""
    if not isinstance(n, int):
        raise TypeError('Silnia wymaga liczby całkowitej.')
    if n < 0:
        raise ValueError('Nie można policzyć silni z liczby ujemnej.')
    if n == 0:
        return 1
    return n * silnia_req(n-1)


if __name__ == "__main__":
    print(silnia(5))
    print(silnia_req(5))
