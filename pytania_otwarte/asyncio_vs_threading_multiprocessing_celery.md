# asyncio, threading, multiprocessing i Celery

## Krótka odpowiedź rekrutacyjna

Wybór zależy od rodzaju pracy oraz wymagań dotyczących wykonywania zadań w tle.

| Narzędzie | Typowe zastosowanie | Ograniczenia |
| --- | --- | --- |
| `asyncio` | Wiele oczekujących operacji sieciowych z bibliotekami async | Blokujący kod zatrzymuje pętlę zdarzeń |
| `threading` | Blokujące I/O i biblioteki synchroniczne | Współdzielony stan wymaga synchronizacji; GIL ogranicza kod bajtowy CPU-bound |
| `multiprocessing` | Równoległe obliczenia CPU-bound w czystym Pythonie | Koszt procesów, serializacji danych i IPC |
| Celery | Kolejki zadań w tle, rozproszeni pracownicy, ponawianie i harmonogramowanie | Dodatkowa infrastruktura, broker oraz obsługa powtórzeń zadań |

## asyncio i wątki

`asyncio` wykonuje korutyny współbieżnie na pętli zdarzeń. Zadanie może oddać
sterowanie przy `await`, jeśli musi czekać. Nie oznacza to równoległych obliczeń
na wielu rdzeniach. Zwykłe wywołanie `requests.get()` lub `time.sleep()` w wątku
pętli blokuje pozostałe zadania; użyj biblioteki async albo `asyncio.to_thread()`.

Wątki Pythona są rzeczywistymi wątkami systemowymi. Przy włączonym GIL wiele
operacji I/O zwalnia blokadę, pozwalając innym wątkom wykonywać pracę. GIL nie
zastępuje blokad chroniących złożone operacje na współdzielonych danych.

Dla obliczeń CPU-bound w czystym Pythonie standardowy CPython z GIL zwykle wymaga
osobnych procesów, aby wykorzystać wiele rdzeni. Rozszerzenia natywne zwalniające
GIL i opcjonalny CPython free-threaded (od 3.13) wymagają osobnej oceny wydajności.

## Celery

Celery zarządza zadaniami przekazywanymi do pracowników przez brokera. Domyślny
model `prefork` wykorzystuje procesy. Dostępne są też m.in. pule wątków i `gevent`.
**Gevent używa greenletów i nie jest workerem asyncio.** Dobór puli wpływa na
obsługiwane funkcje, np. limity czasu.

Celery i asyncio można łączyć w jednej architekturze: np. serwer async obsługuje
żądanie i zleca długie zadanie pracownikowi Celery. Sama korutyna uruchomiona
w procesie serwera nie daje gwarancji przetrwania restartu tego procesu.
Zadania kolejki projektuj z uwzględnieniem ponowień i idempotencji.

## Źródła

- [Python 3.12 — blokujący kod w asyncio](https://docs.python.org/3.12/library/asyncio-dev.html#running-blocking-code)
- [Python — free threading](https://docs.python.org/3/howto/free-threading-python.html)
- [Celery — modele współbieżności](https://docs.celeryq.dev/en/stable/userguide/concurrency/index.html)
