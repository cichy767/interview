Wybór między Celery a asyncio zależy od konkretnych wymagań i charakterystyki projektu, w tym od rodzaju zadań, architektury aplikacji, skalowalności, wydajności, a także preferencji i doświadczenia zespołu deweloperskiego. Oto kilka czynników, które warto rozważyć przy podejmowaniu decyzji:

**Celery**
* Zadania asynchroniczne i harmonogramowanie: Celery jest silnym narzędziem do obsługi asynchronicznych zadań i harmonogramowania zadań w tle. Jest to szczególnie przydatne w przypadku zadań, które wymagają przetwarzania w tle, takich jak wysyłanie e-maili, generowanie raportów, integracje z usługami zewnętrznymi itp.
* Wsparcie dla kolejek zadań: Celery oferuje elastyczne mechanizmy kolejek, które pozwalają na dystrybucję zadań do wielu pracowników (workers) oraz kontrolę nad priorytetami i kolejkami zadań.
* Łatwość konfiguracji: Celery ma bogatą dokumentację i obszerną społeczność, co ułatwia jego konfigurację i rozpoczęcie pracy z tym narzędziem. Posiada również wiele wbudowanych mechanizmów kontroli błędów, monitoringu oraz skalowania.
* Obsługa zarówno CPU-bound, jak i I/O-bound zadań: Celery domyślnie wykorzystuje wieloprocesowość (prefork), co sprawia, że dobrze radzi sobie z zadaniami CPU-bound. Można również skonfigurować go do obsługi zadań I/O-bound poprzez użycie wątków (threads) lub asyncio workers (gevent).

**asyncio**

* Programowanie asynchroniczne w Pythonie: asyncio to biblioteka standardowa Pythona, która umożliwia programowanie asynchroniczne, pozwalając na równoległe wykonywanie wielu zadań I/O-zorientowanych bez blokowania wątków. Jest przydatne w aplikacjach, które muszą obsługiwać wiele równoległych operacji wejścia/wyjścia, takich jak serwisy sieciowe, API, serwisy internetowe itp.

* Wydajność dla zadań I/O-zorientowanych: asyncio może być szczególnie skuteczne w obsłudze zadań, które są zdominowane przez operacje wejścia/wyjścia, ponieważ umożliwia asynchroniczne wykonanie wielu takich operacji w jednym wątku. Jednak operacje muszą wspierać asyncio (np. asyncpg zamiast psycopg2, httpx zamiast requests).
* Prostota i minimalizm: asyncio oferuje prostszy i bardziej minimalistyczny model programowania niż Celery, co może być korzystne w przypadku prostszych projektów lub tych, które nie wymagają pełnego systemu zarządzania zadaniami w tle.  asyncio nie wykorzystuje tradycyjnych wątków, ale korutyny i pętlę zdarzeń (event loop), co daje pełną kontrolę nad momentem przełączania kontekstu (await).
 
## Podsumowanie
Celery: Bardziej odpowiedni dla złożonych aplikacji wymagających zarządzania zadaniami w tle, harmonogramowaniem, monitorowaniem i skalowaniem.

asyncio: Lepszy wybór dla aplikacji opartych na operacjach I/O, gdzie wydajność i równoległe wykonywanie wielu operacji są kluczowe, a zarządzanie zadaniami w tle nie jest głównym wymaganiem.

W niektórych przypadkach można również wykorzystać oba podejścia równocześnie, np. używając asyncio w warstwie serwerowej do obsługi wielu żądań I/O-zorientowanych, a Celery do obsługi zadań asynchronicznych i zadań tła. Ostateczny wybór zależy od specyfiki projektu oraz preferencji deweloperów i zespołu.

**CPU-bound tasks**: Zadania, które wykorzystują moc obliczeniową procesora, np. przetwarzanie danych, analiza obrazów, obliczenia matematyczne. Najlepszy wybór: Celery/multiprocessing.

**I/O-bound tasks**: Zadania, które oczekują na wejście/wyjście, np. czytanie/pisanie do pliku, operacje sieciowe, zapytania do bazy danych. Najlepszy wybór: asyncio/threading.

Wykorzystanie thredingu do zadań które wmagają dużej mocy obliczeniowej może wpłynąć negatywnie na czas wykonania.

* Wąskie gardło CPU: Wielowątkowość jest najbardziej efektywna, gdy zadania są ograniczone przez operacje wejścia/wyjścia (I/O) lub gdy zadania są lekko obciążające CPU. W przypadku intensywnych obliczeniowo zadań, uruchomienie wielu wątków na jednym procesorze może doprowadzić do przeciążenia CPU, gdzie każdy wątek konkuruję o dostęp do zasobów procesora, co w efekcie może spowolnić wykonanie programu.

* Problemy z synchronizacją: Większa liczba wątków zwiększa złożoność zarządzania dostępem do współdzielonych zasobów. Mechanizmy synchronizacji, takie jak blokady (locks) i semafory, które są potrzebne do zapewnienia bezpiecznego dostępu do wspólnych danych, mogą wprowadzać opóźnienia i blokady. To z kolei może prowadzić do problemów z wydajnością, takich jak zakleszczenia (deadlocks) i głodzenie (starvation).

* Kontekstualizacja i przelączanie kontekstu: Każdy wątek wymaga pewnych zasobów systemowych, w tym kontekstu, który musi być przechowywany i zarządzany. Częste przelączanie kontekstu między wątkami (context switching), które ma miejsce, gdy system operacyjny przechodzi z obsługi jednego wątka na inny, może powodować dodatkowe obciążenie. Przelączanie to zużywa czas procesora, który mógłby być wykorzystany na wykonanie faktycznych obliczeń.

* Nieefektywne wykorzystanie cache CPU: Wątki działające na tym samym procesorze mogą nieefektywnie korzystać z pamięci podręcznej procesora. Częste zmiany kontekstu mogą prowadzić do tzw. cache misses, gdzie dane potrzebne jednemu wątkowi nie są dostępne w cache po przełączeniu z innego wątka, co wymaga czasochłonnego dostępu do wolniejszej pamięci RAM.


_asyncio is essentially threading where not the CPU but you, as a programmer (or actually your application), 
decide where and when does the context switch happen. In Python you use an await keyword to suspend the execution of your coroutine (defined using async keyword)._

Threading:

![img.png](obrazki/img.png)


Threading w pythonie tak na prawdę nie jest prawdziwym threadingiem.
Taski nie zaczynają się wykonywać jednocześnie, tylko po chwili gdy zadanie I/O zablokuje wątek, to GIL oblokowuje kolejny. 


```
if io_bound:
    if io_very_slow:
        print("Use Asyncio")
    else:
        print("Use Threads")
else:
    print("Multi Processing")
```