Rodzaje indeksów: Jest ich dużo. Dokumentacja Django opisuje ich 7.

Indeksy B-tree (B-drzewo) Charakterystyka: Najczęściej używane indeksy, które działają na zasadzie zbalansowanego drzewa. Są efektywne dla szerokiego zakresu operacji, w tym wyszukiwania, sortowania i agregacji. Indeksy B-tree mogą skutecznie odnaleźć pojedyncze wiersze, jak i zakresy wierszy. Zastosowanie: Uniwersalne; szczególnie przydatne dla operacji równości i zakresu.
Indeksy Hash
Indeksy GIN
Indeksy GiST
Indeksy SP-GiST
Indeksy BRIN
BloomIndex


Indeksy są kluczowymi komponentami systemów zarządzania bazami danych, systemów plików i innych struktur przechowujących dane, 
pozwalając na szybki dostęp do danych bez konieczności przeglądania wszystkich elementów. 
Implementacja indeksów może wykorzystywać różne struktury danych, zależnie od wymagań dotyczących wydajności, 
typu przechowywanych danych i rodzaju operacji, które mają być na nich wykonywane. 
Oto kilka popularnych implementacji indeksów:

1. Tablice Hashujące
Zastosowanie: Szybkie wyszukiwanie, wstawianie i usuwanie.
Jak działa: Tablice hashujące mapują klucze na wartości poprzez funkcję hashującą. Dzięki temu dostęp do danych jest bardzo szybki, ponieważ obliczenie hasha pozwala bezpośrednio odnaleźć miejsce w pamięci, gdzie przechowywany jest dany element.
Wady: Nie zachowują naturalnego porządku danych, co sprawia, że są nieefektywne dla operacji takich jak wyszukiwanie zakresów.
2. Drzewa B i B+
Zastosowanie: Systemy baz danych, systemy plików.
Jak działa: Drzewa B i B+ to zbalansowane drzewa wyszukiwania, gdzie węzły mogą mieć wiele dzieci, co sprawia, że są bardzo efektywne dla operacji na dyskach. 
Drzewa B+ w szczególności przechowują wszystkie dane w liściach i utrzymują porządek posortowany, co sprawia, że są idealne do zakresowych zapytań.
Wady: Większa złożoność implementacji w porównaniu do prostszych struktur danych.