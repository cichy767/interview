Terminy "pass by reference" i "pass by value" odnoszą się do sposobu, w jaki funkcje otrzymują argumenty od swoich wywołań w różnych językach programowania. To, czy język używa przekazywania przez wartość czy przez referencję, ma znaczący wpływ na to, jak działają funkcje i metody, w tym jak mogą one modyfikować przekazane im argumenty.

Wskaźniki i referencje w innych językach

W językach takich jak C i C++, programista może jawnie określić, czy zmienna jest przekazywana przez wartość czy przez referencję:

W C domyślnie przekazywane są wartości, ale można przekazywać wskaźniki (adresy zmiennych).
W C++ można używać referencji (&), aby zmieniać oryginalne dane przekazane do funkcji.

**Pass by Value**

W przypadku "pass by value" (przekazywanie przez wartość), funkcja otrzymuje kopię wartości argumentu. Oznacza to, że każda modyfikacja tej wartości wewnątrz funkcji nie wpłynie na oryginalną zmienną przekazaną jako argument. Przekazywanie przez wartość jest bezpieczne w kontekście niemodyfikowania danych wejściowych, ponieważ operacje wykonane na argumencie wewnątrz funkcji nie zmienią jego oryginalnej wartości poza funkcją.

**Pass by Reference**

W przypadku "pass by reference" (przekazywanie przez referencję), funkcja otrzymuje referencję (czyli bezpośredni odnośnik) do oryginalnej zmiennej przekazanej jako argument. Oznacza to, że zmiany dokonane na tej zmiennej wewnątrz funkcji będą miały wpływ na oryginalną zmienną. Przekazywanie przez referencję pozwala funkcjom na modyfikację danych wejściowych, co może być zarówno potężne, jak i źródłem błędów, jeśli nie jest odpowiednio kontrolowane.

**Jak to działa w Pythonie?**

Python często jest opisywany jako język, który stosuje "pass by assignment" (przekazywanie przez przypisanie), co jest pewnym uproszczeniem. W rzeczywistości, Python zachowuje się jak "pass by value", gdzie wartością jest referencja do obiektu. To oznacza, że funkcje otrzymują referencję do obiektu, a nie sam obiekt, ale referencja ta jest przekazywana przez wartość. Efekt ten sprawia, że zachowanie jest mieszanką obu podejść:

* Jeśli przekazany argument jest obiektem niemutowalnym (takim jak liczba całkowita, krotka niemodyfikowalna, czy łańcuch znaków), każda próba jego zmodyfikowania w funkcji spowoduje utworzenie nowego obiektu, nie wpływając na oryginalny.
* Jeśli argument jest obiektem mutowalnym (takim jak lista, słownik, czy zbiór), modyfikacje tego obiektu w funkcji będą miały wpływ na oryginalną zmienną, ponieważ zarówno oryginalna zmienna, jak i argument funkcji odnoszą się do tego samego obiektu w pamięci.