# Global Interpreter Lock (GIL)

## Krótka odpowiedź rekrutacyjna

W standardowym wariancie CPythona GIL pozwala jednemu wątkowi wykonywać kod bajtowy
Pythona naraz w obrębie danego interpretera. Ułatwia ochronę wewnętrznych struktur
interpretera i zarządzanie pamięcią, ale nie zastępuje synchronizacji danych aplikacji.
Złożone operacje na współdzielonym stanie nadal mogą wymagać `threading.Lock`.

## Wersja i implementacja mają znaczenie

- Opis dotyczy standardowego CPythona z włączonym GIL, w tym wersji 3.11 i 3.12.
- Od CPythona 3.13 istnieje opcjonalny wariant free-threaded, który może działać bez GIL.
- Rozszerzenia C nieprzystosowane do free threading mogą ponownie włączyć GIL.
- GIL nie jest wymogiem języka Python; inne implementacje mogą działać inaczej.

## Wątki, I/O i obliczenia

Wątki są rzeczywistymi wątkami systemowymi. CPython zwalnia GIL przy wielu
blokujących operacjach I/O, więc wątki mogą obsługiwać oczekiwanie na sieć lub dysk
współbieżnie. Rozszerzenia natywne mogą również zwalniać GIL podczas obliczeń.

Dla obliczeń CPU-bound w czystym Pythonie, przy włączonym GIL, zwykle wybiera się
osobne procesy. Każdy proces ma własny interpreter i nie konkuruje o ten sam GIL.
Dobór rozwiązania należy potwierdzić pomiarem na rzeczywistych danych.

## asyncio

`asyncio` pozwala przeplatać korutyny na pętli zdarzeń, zwykle w jednym wątku.
Gdy zadanie oczekuje na niezakończoną operację przez `await`, inne zadania mogą działać.
Nie każde `await` musi jednak oddać sterowanie, np. gdy wynik jest już gotowy.

`asyncio` nie usuwa GIL i samo nie zapewnia równoległych obliczeń CPU-bound.
Długie obliczenie lub blokujące wywołanie w wątku pętli zatrzymuje pozostałe zadania.
Blokujące I/O można przenieść do `asyncio.to_thread()`, a obliczenia w standardowym
CPythonie do puli procesów, np. przez `run_in_executor()`.

## Źródła

- [Python — threading i GIL](https://docs.python.org/3/library/threading.html#gil-and-performance-considerations)
- [Python — free threading, od wersji 3.13](https://docs.python.org/3/howto/free-threading-python.html)
- [Python 3.12 — blokujący kod w asyncio](https://docs.python.org/3.12/library/asyncio-dev.html#running-blocking-code)
