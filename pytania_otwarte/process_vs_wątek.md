Wątek (ang. thread) – część programu wykonywana współbieżnie w obrębie jednego procesu; w jednym procesie może istnieć wiele wątków.


Procesy i wątki to dwa fundamentalne pojęcia w systemach operacyjnych, które odnoszą się do różnych sposobów realizacji zadań przez komputer. Choć oba są związane z wykonaniem kodu programu, różnią się w kilku kluczowych aspektach.

**Proces**
to instancja działającego programu, która zawiera kod programu, jego bieżący stan (np. wartości rejestrów, wskaźnik instrukcji), stos, dane oraz atrybuty związane z zarządzaniem procesem przez system operacyjny, takie jak identyfikator procesu (PID), priorytet, własność plików itp. Procesy mają oddzielne przestrzenie adresowe, co oznacza, że pamięć jednego procesu jest izolowana od pamięci innego procesu. Komunikacja między procesami (IPC - Inter-Process Communication) jest możliwa, ale jest zazwyczaj bardziej kosztowna niż komunikacja między wątkami tego samego procesu.

**Wątek**
(nazywany też lekkim procesem) to podstawowa jednostka, na której system operacyjny wykonuje szeregowanie zadań. Wątek działa w ramach procesu i dzieli z innymi wątkami tego samego procesu te same zasoby, w tym przestrzeń adresową, pliki i inne zasoby systemowe. W przeciwieństwie do procesów, wszystkie wątki należące do jednego procesu mogą dostępować do tych samych danych i zasobów, co ułatwia komunikację i wymianę danych między wątkami. Wątki mają własny stos oraz lokalny stan rejestrów, ale dzielą segment kodu, segment danych oraz inne zasoby procesu.

**Kluczowe różnice**
* Izolacja pamięci:

Procesy są całkowicie izolowane od siebie pod względem przestrzeni adresowej.
Wątki dzielą przestrzeń adresową i zasoby swojego procesu macierzystego.

* Koszt utworzenia i zarządzania:

Procesy są cięższe w utworzeniu i zarządzaniu przez system operacyjny ze względu na konieczność alokacji oddzielnej przestrzeni adresowej i zasobów.
Wątki są lżejsze i szybsze w tworzeniu oraz zarządzaniu, ponieważ dzielą zasoby procesu macierzystego.

* Komunikacja:

Komunikacja międzyprocesowa (IPC) jest bardziej skomplikowana i kosztowna w realizacji.
Wątki mogą łatwiej i szybciej komunikować się i wymieniać dane, korzystając z wspólnych zasobów.

* Wpływ na wydajność:

Niezależne procesy mogą lepiej wykorzystać systemy wieloprocesorowe lub wielordzeniowe, ale kosztem większego zużycia zasobów.
Wątki mogą zwiększyć wydajność aplikacji, które wymagają współdzielenia dużych ilości danych lub zasobów, przez minimalizację narzutu na komunikację i synchronizację.
Podsumowując, główna różnica między procesem a wątkiem tkwi w sposobie izolacji i współdzielenia zasobów. Wybór między użyciem procesów a wątkami zależy od wymagań aplikacji, w tym potrzeby izolacji, bezpieczeństwa, wydajności oraz modelu programowania.


**Tworzenie nowych procesów zamiast zwiększania liczby wątków** w obrębie jednego procesu może być motywowane różnymi przyczynami, związanych zarówno z charakterystyką działania aplikacji, jak i wymaganiami systemowymi. Oto niektóre z kluczowych powodów:

* Izolacja i niezawodność: Procesy są od siebie izolowane, co oznacza, że awaria jednego procesu (np. wyjątek nieobsłużony, wyciek pamięci) zwykle nie wpłynie bezpośrednio na działanie innych procesów. W kontekście niektórych aplikacji, gdzie stabilność i niezawodność są kluczowe (np. w systemach wbudowanych, aplikacjach krytycznych), izolacja procesów może być bardziej pożądana niż wydajność.
* Wykorzystanie wielu rdzeni: Wieloprocesowość może być efektywniej wykorzystywana na maszynach wielordzeniowych lub wieloprocesorowych. Systemy operacyjne są zaprojektowane tak, aby efektywnie zarządzać procesami na wielu rdzeniach, co może prowadzić do lepszego równoważenia obciążenia i wykorzystania zasobów sprzętowych, szczególnie dla intensywnych obliczeniowo zadań.
* Zabezpieczenia: Procesy działające w oddzielnych przestrzeniach adresowych mogą mieć różne poziomy uprawnień, co umożliwia lepsze zarządzanie dostępem do zasobów systemowych i danych. To sprawia, że wieloprocesowość jest bardziej odpowiednia w aplikacjach wymagających ścisłej kontroli nad bezpieczeństwem i dostępem.
* Uproszczenie zarządzania stanem: Programy wieloprocesowe mogą być prostsze do zrozumienia i debugowania, ponieważ stan jest bardziej izolowany. Każdy proces może być traktowany jako niezależny byt z własnym stanem, co redukuje złożoność zarządzania współdzielonym stanem, charakterystyczną dla programów wielowątkowych.
* Kompatybilność i integracja: Niektóre aplikacje mogą korzystać z procesów zewnętrznych lub bibliotek, które nie są bezpieczne w kontekście wielowątkowym lub wymagają uruchomienia w oddzielnym procesie. W takich przypadkach wieloprocesowość jest naturalnym wyborem.
* Unikanie zablokowań i zakleszczeń: Wielowątkowe aplikacje są podatne na złożone problemy synchronizacji, takie jak zakleszczenia, które mogą być trudne do zdiagnozowania i rozwiązania. W przypadku aplikacji wieloprocesowych, gdzie komunikacja między procesami jest bardziej kontrolowana i zazwyczaj odbywa się przez wyraźnie zdefiniowane interfejsy (np. gniazda, potoki), ryzyko wystąpienia takich problemów jest mniejsze.

**Optymalna Liczba Wątków**

Optymalna liczba wątków zwykle odpowiada liczbie rdzeni procesora, 
ponieważ pozwala to każdemu rdzeniowi na efektywne przetwarzanie jednego wątku w danym momencie. 
Na przykład, jeśli masz procesor czterordzeniowy, utworzenie i uruchomienie czterech wątków może pozwolić na maksymalne wykorzystanie zasobów sprzętowych.

**Wyjątki i Rozważania Specjalne**

Wątki I/O-bound vs. CPU-bound: Jeśli aplikacja wykonuje wiele operacji wejścia-wyjścia (I/O-bound), które często oczekują na zewnętrzne zdarzenia 
(np. odpowiedzi z sieci, dostęp do dysku), może być korzystne uruchomienie większej liczby wątków niż liczba rdzeni. 
Pozwala to na wykorzystanie momentów, gdy inne wątki są zablokowane, czekając na I/O.
Hiperprzetwarzanie (Hyper-threading): Niektóre procesory wspierają hiperprzetwarzanie (technologia Intel Hyper-Threading), 
pozwalając każdemu fizycznemu rdzeniowi na przetwarzanie dwóch wątków jednocześnie. W takim przypadku, optymalna liczba wątków może być dwa razy większa niż liczba rdzeni.