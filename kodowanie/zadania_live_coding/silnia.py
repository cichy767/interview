# !5 = 1*2*3*4*5

def silnia(n):
    if n == 0:
        return 1
    elif n < 0:
        raise ValueError('Nie można policzyć silni z liczby ujemnej.')

    r = 1
    for num in range(1, n + 1):
        r *= num
        print(r)

    return r


silnia(5)


def silnia_req(n):
    if n == 0:
        return 1
    return n * silnia_req(n-1)


result = silnia_req(5)
print(f'result: {result}')
