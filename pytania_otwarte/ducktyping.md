```python
def read_data(source):
    return source.read()

# Możemy teraz przekazać dowolny obiekt, który ma metodę read(),
# niezależnie od jego typu.
```

Dzięki temu nasza funkcja read_data może przyjmować różne rodzaje obiektów, takie jak pliki, strumienie danych, obiekty tymczasowe i inne, pod warunkiem, że posiadają one metodę read. Nie musimy więc ograniczać się do jednego typu obiektów, co czyni nasz kod bardziej elastycznym i wielofunkcyjnym.

**Zalety Duck Typing**

* Elastyczność: Kod staje się bardziej elastyczny, gdyż może obsługiwać różnorodne typy obiektów, o ile spełniają one określone wymagania (posiadają odpowiednie metody lub atrybuty).
* Zmniejszenie zależności: Nie ma potrzeby polegania na konkretnych typach danych, co zmniejsza zależności między komponentami systemu.
* Łatwość rozszerzania: Dodawanie nowych funkcjonalności, które mają współpracować z istniejącym kodem, jest łatwiejsze, ponieważ nowe obiekty muszą jedynie "udawać" (mieć odpowiednie metody), że są typem oczekiwanym przez istniejący kod.

**Wady Duck Typing**

* Błędy w czasie wykonywania: Błędy związane z nieodpowiednimi typami obiektów lub brakującymi metodami mogą pojawić się dopiero w czasie wykonywania programu, co może utrudniać debugowanie.
* Zrozumiałość kodu: Kod może stać się mniej zrozumiały dla osób nieznających szczegółów implementacji, ponieważ nie jest od razu oczywiste, jakie typy obiektów mogą być przekazywane do funkcji.


Duck typing jest jedną z kluczowych cech języka Python, która sprzyja pisaniu elastycznego i dynamicznego kodu. Jednak jak każde podejście, ma ono swoje zalety i wady, które warto rozważyć przy projektowaniu oprogramowania.