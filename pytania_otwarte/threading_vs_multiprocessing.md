# Threading vs multiprocessing

## Kluczowe różnice:
### Definicja

* threading → Wykorzystuje wątki (threads), które współdzielą pamięć w obrębie jednego procesu.

* multiprocessing → Tworzy osobne procesy (processes), każdy z własną pamięcią i interpreterem Pythona.

Obsługa Global Interpreter Lock (GIL)

threading → Podlega GIL, więc wątki nie mogą wykonywać kodu Python równocześnie na różnych rdzeniach CPU.

multiprocessing → Nie podlega GIL, ponieważ każdy proces ma własną instancję interpretera Pythona i może działać równolegle na różnych rdzeniach CPU.

### Zastosowanie

threading → Dobre dla zadań I/O-bound (np. operacje na plikach, pobieranie danych z API, obsługa sieci).

multiprocessing → Dobre dla zadań CPU-bound (np. operacje numeryczne, analiza danych, AI/ML).

### Pamięć

threading → Wątki współdzielą pamięć, co ułatwia komunikację, ale wymaga synchronizacji (np. Lock).

multiprocessing → Każdy proces ma osobną pamięć, co zwiększa stabilność, ale wymaga mechanizmów IPC (np. Queue, Pipe, Manager).
Koszt tworzenia

threading → Tworzenie wątku jest szybsze i mniej zasobożerne niż tworzenie procesu.

multiprocessing → Tworzenie procesu jest droższe (czas i pamięć), ale eliminuje problemy związane z GIL.


🔹 Podsumowanie
Używaj threading, gdy masz małą liczbę zadań I/O-bound, ale musisz korzystać z kodu, który nie obsługuje asyncio (np. starsze biblioteki).
Używaj asyncio, gdy chcesz obsłużyć dużo operacji I/O jednocześnie w sposób bardziej efektywny (np. serwery HTTP, klienci baz danych).
Jeśli zadania są CPU-bound, to ani threading, ani asyncio nie są dobrym wyborem – w takim przypadku multiprocessing będzie lepsze.
Chcesz rozwinąć któryś z tych punktów bardziej szcze


```python
import threading
import time

def worker():
    print("Start wątku")
    time.sleep(2)
    print("Koniec wątku")

threads = []
for _ in range(5):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("Wszystkie wątki zakończone")

```

```python
import multiprocessing
import time

def worker():
    print("Start procesu")
    time.sleep(2)
    print("Koniec procesu")

processes = []
for _ in range(5):
    p = multiprocessing.Process(target=worker)
    p.start()
    processes.append(p)

for p in processes:
    p.join()

print("Wszystkie procesy zakończone")
```