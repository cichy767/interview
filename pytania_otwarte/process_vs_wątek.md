Wątek (ang. thread) – część programu wykonywana współbieżnie w obrębie jednego procesu; w jednym procesie może istnieć wiele wątków.


Procesy i wątki to dwa fundamentalne pojęcia w systemach operacyjnych, które odnoszą się do różnych sposobów realizacji zadań przez komputer. Choć oba są związane z wykonaniem kodu programu, różnią się w kilku kluczowych aspektach.

Proces
to instancja działającego programu, która zawiera kod programu, jego bieżący stan (np. wartości rejestrów, wskaźnik instrukcji), stos, dane oraz atrybuty związane z zarządzaniem procesem przez system operacyjny, takie jak identyfikator procesu (PID), priorytet, własność plików itp. Procesy mają oddzielne przestrzenie adresowe, co oznacza, że pamięć jednego procesu jest izolowana od pamięci innego procesu. Komunikacja między procesami (IPC - Inter-Process Communication) jest możliwa, ale jest zazwyczaj bardziej kosztowna niż komunikacja między wątkami tego samego procesu.

Wątek
(nazywany też lekkim procesem) to podstawowa jednostka, na której system operacyjny wykonuje szeregowanie zadań. Wątek działa w ramach procesu i dzieli z innymi wątkami tego samego procesu te same zasoby, w tym przestrzeń adresową, pliki i inne zasoby systemowe. W przeciwieństwie do procesów, wszystkie wątki należące do jednego procesu mogą dostępować do tych samych danych i zasobów, co ułatwia komunikację i wymianę danych między wątkami. Wątki mają własny stos oraz lokalny stan rejestrów, ale dzielą segment kodu, segment danych oraz inne zasoby procesu.

Kluczowe różnice
Izolacja pamięci:

Procesy są całkowicie izolowane od siebie pod względem przestrzeni adresowej.
Wątki dzielą przestrzeń adresową i zasoby swojego procesu macierzystego.

Koszt utworzenia i zarządzania:

Procesy są cięższe w utworzeniu i zarządzaniu przez system operacyjny ze względu na konieczność alokacji oddzielnej przestrzeni adresowej i zasobów.
Wątki są lżejsze i szybsze w tworzeniu oraz zarządzaniu, ponieważ dzielą zasoby procesu macierzystego.
Komunikacja:

Komunikacja międzyprocesowa (IPC) jest bardziej skomplikowana i kosztowna w realizacji.
Wątki mogą łatwiej i szybciej komunikować się i wymieniać dane, korzystając z wspólnych zasobów.
Wpływ na wydajność:

Niezależne procesy mogą lepiej wykorzystać systemy wieloprocesorowe lub wielordzeniowe, ale kosztem większego zużycia zasobów.
Wątki mogą zwiększyć wydajność aplikacji, które wymagają współdzielenia dużych ilości danych lub zasobów, przez minimalizację narzutu na komunikację i synchronizację.
Podsumowując, główna różnica między procesem a wątkiem tkwi w sposobie izolacji i współdzielenia zasobów. Wybór między użyciem procesów a wątkami zależy od wymagań aplikacji, w tym potrzeby izolacji, bezpieczeństwa, wydajności oraz modelu programowania.