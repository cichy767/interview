https://www.youtube.com/watch?v=pTB30aXS77U
https://github.com/ArjanCodes/betterpython/tree/main/9%20-%20solid

SOLID to akronim odnoszący się do pięciu zasad projektowania obiektowego i programowania, które mają na celu poprawę czytelności, 
skalowalności oraz możliwości utrzymania kodu. 
Zasady SOLID są uniwersalne i mogą być stosowane w różnych językach programowania, w tym w Pythonie. 
Oto one:

**Single Responsibility Principle (Zasada Pojedynczej Odpowiedzialności):**

Każda klasa powinna mieć tylko jeden powód do zmiany. To oznacza, że klasa powinna mieć tylko jedno zadanie lub odpowiedzialność.
W Pythonie, to często oznacza użycie prostych klas i funkcji, które wykonują jedną rzecz i robią to dobrze.

**Open/Closed Principle (Zasada Otwarte/Zamknięte):**

Oprogramowanie powinno być otwarte na rozszerzenia, ale zamknięte na modyfikacje. Innymi słowy, powinieneś być w stanie dodać nową funkcjonalność bez zmiany istniejącego kodu.
W Pythonie można to osiągnąć za pomocą dziedziczenia i polimorfizmu, tworząc klasy bazowe, które mogą być rozszerzane przez klasy pochodne bez potrzeby zmiany kodu klas bazowych.

**Liskov Substitution Principle (Zasada Podstawienia Liskov):**

Obiekty w programie powinny być zamienne z instancjami ich klas bazowych bez wpływu na poprawność programu. To znaczy, jeśli klasa B dziedziczy po klasie A, to powinno być możliwe użycie obiektu klasy B wszędzie tam, gdzie oczekiwany jest obiekt klasy A.
W Pythonie, to zasada przypomina o konieczności zachowania spójności interfejsów i zachowań w hierarchii klas.

**Interface Segregation Principle (Zasada Segregacji Interfejsu):**

Klienci nie powinni być zmuszani do polegania na interfejsach, których nie używają. To oznacza, że zamiast jednego dużego interfejsu, lepiej jest mieć wiele mniejszych i bardziej specyficznych.
W Pythonie, który jest językiem o dynamicznym typowaniu, ta zasada może być mniej formalna, ale nadal wartościowa w kontekście definiowania jasnych i zrozumiałych API.
```python
class IMultiFunctionDevice:
    def print(self, document):
        pass

    def scan(self, document):
        pass

    def copy(self, document):
        pass


class SimplePrinter(IMultiFunctionDevice):
    def print(self, document):
        print(f"Drukowanie: {document}")

    def scan(self, document):
        raise NotImplementedError("Funkcja skanowania nie jest dostępna")

    def copy(self, document):
        raise NotImplementedError("Funkcja kopiowania nie jest dostępna")
```
Aby zastosować zasadę segregacji interfejsów, powinniśmy podzielić **IMultiFunctionDevice** na mniejsze, bardziej specyficzne interfejsy.
```python
class IPrinter:
    def print(self, document):
        pass

class IScanner:
    def scan(self, document):
        pass

class ICopier:
    def copy(self, document):
        pass

```

**Dependency Inversion Principle (Zasada Odwrócenia Zależności):**

Moduły wysokiego poziomu (te, które wykonują ważne działania biznesowe) nie powinny być zależne od modułów niskiego poziomu (takich, które wykonują operacje wejścia/wyjścia, komunikację z bazą danych itp.). 
Oba typy modułów powinny być zależne od abstrakcji.
Abstrakcje nie powinny zależeć od szczegółów. Szczegóły (implementacje) powinny zależeć od abstrakcji.
Klasy powinny być zależne od abstrackji klasy a nie jakiejś bardziej wyspecjalicowanej klasy.

Przykład:
```python
from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def save(self, data):
        pass

class MySQLDatabase(Database):
    def save(self, data):
        print(f"Zapisywanie danych do MySQL: {data}")

class DataManager:
    def __init__(self, database: Database):
        self.database = database
    
    def save_data(self, data):
        self.database.save(data)
```

Stosowanie zasad SOLID w Pythonie pomaga tworzyć bardziej elastyczne, utrzymywalne i skalowalne aplikacje. Choć niektóre zasady mogą wydawać się bardziej naturalne lub łatwiejsze do zastosowania w statycznie typowanych językach, ich adaptacja w Pythonie przynosi znaczące korzyści w jakości i trwałości kodu.