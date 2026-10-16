# Threading, multiprocessing i asyncio

## Krótka odpowiedź rekrutacyjna

- `threading`: wątki współdzielą pamięć procesu. Przydatne przy blokującym I/O;
  współdzielone dane mogą wymagać blokad.
- `multiprocessing`: osobne procesy z własną pamięcią i interpreterami. Umożliwia
  równoległe obliczenia w czystym Pythonie także przy włączonym GIL, kosztem
  uruchamiania procesów i komunikacji między nimi.
- `asyncio`: korutyny i pętla zdarzeń; przydatne przy wielu operacjach I/O
  obsługiwanych przez biblioteki asynchroniczne.

W standardowym CPythonie z GIL wątki nie wykonują równolegle kodu bajtowego w tym
samym interpreterze. Wyjątkiem są m.in. obliczenia w rozszerzeniach zwalniających GIL.
Od Pythona 3.13 dostępny jest też opcjonalny wariant free-threaded bez GIL.
`asyncio` samo nie zrównolegla obliczeń CPU-bound.

## Przykład wątków

```python
from threading import Thread
from time import sleep


def worker():
    print("Start wątku")
    sleep(2)
    print("Koniec wątku")


if __name__ == "__main__":
    threads = [Thread(target=worker) for _ in range(5)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
```

## Przykład procesów

Przy metodzie startu `spawn`, używanej m.in. na Windows, kod tworzący procesy musi
być pod `if __name__ == "__main__":`. Funkcja pracownika musi być importowalna,
więc zapisz przykład do pliku `.py` i uruchom go jako skrypt.

```python
from multiprocessing import Process
from time import sleep


def worker():
    print("Start procesu")
    sleep(2)
    print("Koniec procesu")


if __name__ == "__main__":
    processes = [Process(target=worker) for _ in range(5)]
    for process in processes:
        process.start()
    for process in processes:
        process.join()
```

## Źródła

- [Python — threading](https://docs.python.org/3/library/threading.html)
- [Python — bezpieczny import przy multiprocessing](https://docs.python.org/3/library/multiprocessing.html#safe-importing-of-main-module)
- [Python — free threading](https://docs.python.org/3/howto/free-threading-python.html)
