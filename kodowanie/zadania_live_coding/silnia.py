# 5! = 1 * 2 * 3 * 4 * 5

def strong(n):
    """Rekurencyjna silnia; duże n może przekroczyć limit rekurencji."""
    if not isinstance(n, int):
        raise TypeError('Silnia wymaga liczby całkowitej.')
    if n < 0:
        raise ValueError('Nie można policzyć silni z liczby ujemnej.')
    if n <= 1:
        return 1
    return n * strong(n - 1)


if __name__ == "__main__":
    print(strong(5))
