Jak można zoptymalizować zapytanie SQL?
Optymalizacja polega na skróceniu czasu egzekucji zapytania lub zmniejszenia wykorzystywania zasobów.
1. Można sprawdzić czy dodanie indexów pomoże. Indexy pomagają przy zapytaniach SELECT. Ale spowalniają CREATE UPDATE DELETE.
2. Warto sprawdzić zasoby, które wykorzystuje baza. 
Jeśli procesor jest mocno wykorzystywany to możemy go odciążyć wykorzystując pamięć na stworzenie widoków zmaterializowanych lub tabeli tymczasowej.
3. Jeśli wykonujemy jakieś cykliczne zapytania to można je wykonywać w nocy za pomocą jobów. Dzięki temu odciążymy bazę danych w dzień.
4. Jeśli nasz system polega na cyklicznym odpytywaniu API, żeby uzyskać jakąś informacje to możemy użyć event driven communication, dzięki której ograniczymy ilość zapytań.
5. Można sprawdzić czy pewnych informacji nie da się cacheować


Widok (ang. view) w PostgreSQL, podobnie jak w innych systemach zarządzania relacyjnymi bazami danych (RDBMS), to wirtualna tabela reprezentująca wyniki zapytań SQL. 
Nie przechowuje on fizycznie danych, lecz jest zdefiniowany przez zapytanie operujące na jednej lub wielu tabelach. Widoki mogą służyć różnym celom, takim jak:

* Uproszczenie złożonych zapytań: Zamiast pisać skomplikowane zapytania za każdym razem, można stworzyć widok, który je reprezentuje. 
Dzięki temu użytkownicy mogą wykonywać proste zapytania do widoku bez potrzeby rozumienia jego złożoności.

* Bezpieczeństwo: Widoki mogą być wykorzystywane do ograniczenia dostępu do pewnych danych. 
Na przykład, można utworzyć widok, który pokazuje tylko ograniczony zestaw kolumn z tabeli, ukrywając wrażliwe dane przed nieupoważnionymi użytkownikami.

* Abstrakcja: Widoki pozwalają na oddzielenie sposobu przechowywania danych od sposobu ich prezentacji użytkownikom końcowym, 
co umożliwia zmiany w strukturze bazy danych bez wpływu na aplikacje korzystające z tych danych przez widoki.



Widok zmaterializowany (ang. materialized view) w SQL to specjalny rodzaj widoku, który fizycznie przechowuje dane na dysku, w przeciwieństwie do standardowego widoku, 
który jest tylko zdefiniowanym zapytaniem i nie przechowuje fizycznie danych. Dzięki temu, odczyty z widoku zmaterializowanego mogą być znacznie szybsze, 
zwłaszcza przy dużych i złożonych zapytaniach, ponieważ dane są już obliczone i przechowywane w postaci tabeli.

Widoki zmaterializowane są szczególnie przydatne w sytuacjach, gdy:
* Zapytania są kosztowne obliczeniowo: Jeśli zapytanie bazowe widoku jest złożone i jego wykonanie trwa długo, zmaterializowanie wyników może znacząco przyspieszyć czas dostępu do danych.
* Dane nie zmieniają się często: Widoki zmaterializowane są szczególnie przydatne, gdy dane, na których operują, 
nie są często aktualizowane, ponieważ odświeżanie widoku (aktualizacja przechowywanych danych) może być procesem kosztownym.
* Potrzebna jest szybka dostępność danych: W scenariuszach wymagających szybkiego dostępu do przetworzonych danych, 
widoki zmaterializowane mogą znacząco poprawić wydajność, ponieważ omijają konieczność ponownego obliczania zapytań przy każdym dostępie.


Tabela tymczasowa w SQL to specjalny rodzaj tabeli, która jest używana do przechowywania danych tymczasowych, 
przeważnie w ramach jednej sesji bazy danych lub transakcji. Tabele tymczasowe są bardzo przydatne w różnych scenariuszach, 
takich jak przetwarzanie pośrednich wyników złożonych operacji, przechowywanie danych pomocniczych podczas wykonywania skomplikowanych zapytań, 
lub jako mechanizm izolacji danych w procedurach składowanych.
