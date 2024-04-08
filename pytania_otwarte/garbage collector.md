https://www.youtube.com/watch?v=pyqa47b4Fys

Kiedy tworzymy obiekty w pythonie, python śledzi liczbę referencji do danego obieku. Gdy liczba referencji wyniesie 0, python memory manager zniszczy ten obiekt i odzyska pamięc poświęconą na te obiekty.
Jednak czasem to nie działa, bo pojawiają się circular references i wtedy do akcji wchodzi Garbage collector.


W Pythonie Garbage Collector (GC) jest mechanizmem, który automatycznie zarządza pamięcią poprzez usuwanie obiektów, które nie są już używane przez program. Głównym celem Garbage Collector jest zapewnienie efektywnego wykorzystania pamięci i uniknięcie wycieków pamięci poprzez automatyczne zwalnianie pamięci, które są zajmowane przez nieużywane obiekty.

**Jak działa Garbage Collector w Pythonie?**

Śledzenie referencji: Garbage Collector śledzi referencje do wszystkich obiektów w programie. Każdy obiekt w Pythonie ma zlicznik referencji, który odnosi się do liczby referencji wskazujących na ten obiekt.

Identyfikacja obiektów do usunięcia: GC cyklicznie analizuje zbiór obiektów w poszukiwaniu obiektów, które nie są dostępne ani przez żadne zmienne ani przez żaden inny obiekt w programie. Te obiekty są uważane za "śmieci" i są gotowe do usunięcia z pamięci.

Usuwanie nieużywanych obiektów: Po zidentyfikowaniu nieużywanych obiektów, Garbage Collector zwalnia pamięć, którą zajmują te obiekty, przez ich usunięcie.

**W jaki sposób można kontrolować Garbage Collector w Pythonie?**

Python ma wbudowane mechanizmy, które pozwalają programiście na kontrolowanie zachowania Garbage Collector. Niektóre z tych mechanizmów to:

Moduł gc: Moduł gc w Pythonie umożliwia programiście kontrolę nad Garbage Collectorem, na przykład włączanie lub wyłączanie go, ręczne wywoływanie procesu zbierania śmieci oraz dostęp do informacji o obiektach i referencjach.

Zmienne globalne: Można manipulować zachowaniem Garbage Collector poprzez ustawianie wartości zmiennych globalnych, takich jak gc.disable() lub gc.enable().

**Zalety Garbage Collector w Pythonie:**
* Unikanie wycieków pamięci poprzez automatyczne usuwanie nieużywanych obiektów.
* Uproszczenie procesu programowania poprzez eliminację konieczności ręcznego zarządzania pamięcią.

**Wady Garbage Collector w Pythonie:**
* Koszt obliczeniowy: Proces zbierania śmieci może być kosztowny pod względem obliczeniowym, co może prowadzić do spadku wydajności w niektórych przypadkach.

Garbage Collector w Pythonie jest kluczowym elementem zarządzania pamięcią, który znacznie ułatwia proces tworzenia aplikacji, eliminując wiele potencjalnych problemów związanych z zarządzaniem pamięcią w ręczny sposób.