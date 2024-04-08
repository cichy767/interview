Memoization to technika programistyczna stosowana do zwiększenia wydajności poprzez przechowywanie wyników kosztownych obliczeń i ponowne wykorzystanie tych wyników, 
gdy te same dane wejściowe są używane ponownie. 
Idea ta opiera się na zasadzie, że jeśli funkcja jest wywoływana wielokrotnie z tymi samymi argumentami, wynik będzie zawsze taki sam. 
Dlatego zamiast wielokrotnie przeprowadzać te same obliczenia, wynik jest przechowywany i przy ponownym wywołaniu funkcji z tymi samymi argumentami, 
wynik jest po prostu pobierany z pamięci, co znacznie skraca czas potrzebny na wykonanie programu.

Memoization jest szczególnie przydatna w przypadku obliczeń rekurencyjnych, gdzie te same wartości są często obliczane wielokrotnie, 
tak jak w przypadku ciągu Fibonacciego, gdzie bez memoizacji czas potrzebny na obliczenie dużych wartości ciągu rośnie eksponencjalnie.

Zastosowanie memoizacji może być realizowane na różne sposoby, w zależności od języka programowania. W niektórych językach, takich jak Python, 
istnieją wbudowane dekoratory, które automatycznie zapewniają memoizację funkcji. 
W innych przypadkach programiści mogą ręcznie implementować memoizację, używając struktur danych takich jak słowniki, 
do przechowywania par argumentów i ich odpowiadających wyników obliczeń.


```python
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]
```


```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_cache(n):
    if n <= 1:
        return n
    return fibonacci_cache(n-1) + fibonacci_cache(n-2)
```