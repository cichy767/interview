**Normalizacja w SQL** odnosi się do procesu organizacji danych w bazie danych w sposób, który redukuje redundancję i zależności przez rozdzielenie danych na różne tabele. 
Proces ten pozwala na zwiększenie spójności danych i optymalizację ich przechowywania. 
Normalizacja jest fundamentem relacyjnego projektowania baz danych i jest osiągana przez stosowanie serii reguł, znanych jako normalne formy (NF).

Istnieje kilka poziomów normalizacji, z których każdy jest zdefiniowany przez określone wymagania (normalne formy), od pierwszej normalnej formy (1NF) do piątej normalnej formy (5NF). Oto kilka pierwszych normalnych form i ich podstawowe założenia:

* Pierwsza normalna forma (1NF): Każda komórka tabeli zawiera tylko jedną wartość (nie ma powtarzających się grup) i każda kolumna zawiera wartości tego samego typu danych.

* Druga normalna forma (2NF): Spełniona jest 1NF, a także wszystkie atrybuty (kolumny) w tabeli są w pełni zależne od klucza głównego tabeli.

* Trzecia normalna forma (3NF): Spełniona jest 2NF, a także żaden atrybut niekluczowy nie jest zależny od innych atrybutów niekluczowych, tylko od klucza głównego.


**Cel normalizacji:**

* Zapobieganie anomalii danych: Dzięki normalizacji zmniejsza się ryzyko wystąpienia anomalii wstawiania, aktualizacji lub usuwania, które mogą prowadzić do niekonsekwentnych danych.
* Oszczędność miejsca: Redukcja redundancji może również zaoszczędzić miejsce w bazie danych.
* Poprawa wydajności: Choć znormalizowana baza danych może czasami wymagać bardziej skomplikowanych zapytań ze względu na konieczność łączenia tabel, 
może to również przyczynić się do szybszego działania niektórych operacji, takich jak aktualizacje, ponieważ mniej danych wymaga modyfikacji.


Z drugiej strony, nadmierna normalizacja może prowadzić do skomplikowania projektu bazy danych i spowolnienia zapytań z powodu konieczności wykonywania wielu operacji łączenia. 
W praktycznych zastosowaniach często stosuje się pewien poziom denormalizacji, aby zoptymalizować wydajność zapytań.