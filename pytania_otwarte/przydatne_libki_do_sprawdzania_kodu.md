**Black** (code formatter)

* Automatycznie formatuje kod zgodnie z PEP 8 (i własnymi regułami).
* Ujednolica styl kodu, eliminując dyskusje o formatowaniu.
* Nie analizuje jakości ani poprawności kodu – tylko jego wygląd.

to popularne narzędzie służące do formatowania kodu Python, znane również jako "The Uncompromising Code Formatter". 
Głównym celem Blacka jest zapewnienie jednolitego stylu formatowania kodu Python, co z kolei pomaga w utrzymaniu kodu czytelnego, 
zrozumiałego i łatwego w utrzymaniu dla zespołów programistów. Black automatycznie reformatuje Twój kod w sposób, 
który spełnia zestaw z góry określonych reguł stylistycznych, 
eliminując osobiste preferencje w formatowaniu kodu oraz długie dyskusje na temat stylu w przeglądach kodu (code reviews).


**Flake8** (code linter)

* Sprawdza zgodność kodu ze stylem PEP 8.
* Wykrywa podstawowe błędy (np. nieużywane importy, złe nazwy zmiennych).
* Znajduje potencjalne problemy, ale nie analizuje kodu tak dokładnie jak Pylint.

Flake8 to narzędzie służące do sprawdzania stylu kodu Python oraz do wykrywania niektórych błędów programistycznych. 
Jest to wręcz nieocenione narzędzie dla programistów Pythona, które pomaga w utrzymaniu kodu czystego, 
zgodnego z konwencjami PEP 8 (Python Enhancement Proposal 8, czyli propozycji ulepszenia Pythona dotyczącej zasad stylu kodowania) 
oraz w wykrywaniu potencjalnych problemów w kodzie jeszcze przed jego wykonaniem. Flake8 łączy w sobie funkcjonalność kilku innych narzędzi, 
takich jak PyFlakes, pycodestyle (wcześniej znany jako pep8), i dodatkowo może być rozszerzany o wtyczki, co czyni go bardzo elastycznym.


**Pylint** (code linter)

Co robi?

* Sprawdza styl kodu (PEP 8 i więcej).
* Wykrywa błędy, np. literówki w nazwach zmiennych, błędne importy, niezainicjalizowane zmienne.
* Ocenia jakość kodu, podając ocenę od 0 do 10.
* Sugeruje refaktoryzację, aby poprawić czytelność i wydajność kodu.