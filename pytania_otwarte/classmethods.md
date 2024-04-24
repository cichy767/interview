Metoda dekorowana jako classmethod w Pythonie jest używana, aby określić funkcje, które wymagają dostępu do klasy, 
ale nie koniecznie do konkretnej instancji tej klasy. 
Przyjmują one pierwszy argument zazwyczaj nazywany cls, który odnosi się do samej klasy. 

Oto kilka zastosowań i zalet używania classmethod:

* Fabrykacja instancji: classmethod często służy jako alternatywny konstruktor. Może tworzyć instancje klasy z różnymi zestawami danych wejściowych lub wstępnie skonfigurowane instancje.

* Dostęp do danych klasy: Metody te mogą modyfikować stan klasy, który jest wspólny dla wszystkich instancji, np. zmienne klasowe.

* Dziedziczenie i polimorfizm: classmethod jest szczególnie użyteczny w hierarchiach dziedziczenia, gdzie metoda klasy może być wywoływana na klasie pochodnej, dostosowując się do kontekstu tej klasy, co umożliwia bardziej polimorficzne zachowania.

* Operacje związane z klasą: Można ich używać do operacji, które mają być wykonane na poziomie klasy, zamiast na poziomie pojedynczych instancji, takich jak zmiana konfiguracji klasy, analiza lub raportowanie stanu wszystkich instancji itp.


```python
class Book:
    num_books = 0

    def __init__(self, title):
        self.title = title
        Book.num_books += 1

    @classmethod
    def total_books(cls):
        return cls.num_books

    @classmethod
    def create_from_string(cls, title_str):
        title = title_str.strip()
        return cls(title)  # Tworzy instancję klasy

# Tworzenie instancji za pomocą classmethod jako alternatywnego konstruktora
book1 = Book.create_from_string(" Moby Dick ")
book2 = Book.create_from_string("War and Peace")

# Wykorzystanie classmethod do pobrania danych klasy
print(Book.total_books())  # Wyświetli 2, bo stworzyliśmy dwie książki
```

W powyższym przykładzie, create_from_string jest alternatywnym konstruktorem, który pozwala tworzyć instancje Book z ciągu znaków. 
Metoda total_books pozwala zobaczyć, ile książek zostało utworzonych, co jest przykładem wykorzystania classmethod do dostępu do danych klasy.