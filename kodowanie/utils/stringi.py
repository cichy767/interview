"""Operacje na napisach i celowy przykład błędu join()."""


if __name__ == "__main__":
    text = 'hello there'.replace('there', 'general kenobi')
    print(text)
    print(' '.join(['hello there', 'general kenobi']))

    # join przyjmuje wyłącznie napisy. Błąd jest częścią demonstracji.
    try:
        print(''.join(['A', 'B', 1]))
    except TypeError as exc:
        print(f'Oczekiwany TypeError: {exc}')

    print(''.join(map(str, ['A', 'B', 1])))  # AB1
