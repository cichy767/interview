# Przygotowanie do rozmów technicznych

Notatki i ćwiczenia dotyczące Pythona, Django, SQL oraz architektury aplikacji.

## Spis materiałów

- [Python i pytania otwarte](pytania_otwarte/)
- [Architektura i REST](pytania_otwarte/architektura/)
- [Docker, Nginx i wdrożenia](pytania_otwarte/devops/)
- [SQL](SQL/)
- [Django i ORM](kodowanie/django/)
- [Programowanie obiektowe](kodowanie/OOP/)
- [Wzorce projektowe](kodowanie/wzorce_projektowe/)
- [Zadania live coding](kodowanie/zadania_live_coding/)
- [Rozwiązania referencyjne](kodowanie/zadania_live_coding/solutions/)
- [Większe zadania rekrutacyjne — opisy i PDF-y](big_tasks/)
- [Pytania do rekrutera](pytania_do_rekrutera.md)
- [Umiejętności miękkie](umiejętności_miekkie.md)

## Środowisko

Python 3.11 lub nowszy. CI sprawdza wersje 3.11–3.14 na Windows i Linux.
Większość przykładów korzysta wyłącznie z biblioteki standardowej.
Pomiar pamięci procesu wymaga `psutil`, zadeklarowanego w `requirements.txt`.
Nazwy Django, Celery i innych bibliotek w notatkach nie oznaczają, że są potrzebne
do uruchomienia ćwiczeń Pythona.

Windows / PowerShell:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.\.venv\Scripts\python.exe -m pytest
.\.venv\Scripts\python.exe -m ruff check .
```

Linux / macOS:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python -m pytest
.venv/bin/python -m ruff check .
```

## Uruchamianie przykładów

Uruchamiaj moduły z katalogu głównego repozytorium, korzystając z interpretera
środowiska wirtualnego. Po jego aktywowaniu:

```sh
python -m kodowanie.asyncio_examples.example
python -m kodowanie.generatory.example
python -m kodowanie.generatory.third_example
python -m kodowanie.context_manager.function_example
python -m kodowanie.zadania_live_coding.solutions.find_a_bug
python -m kodowanie.zadania_live_coding.solutions.sqaure_game
```

Tryb `-m` zapewnia dostęp do importów zaczynających się od `kodowanie`.
Przykład odczytu rekordów używa pliku względem `__file__`; demonstracja context
managera tworzy własne pliki tymczasowe.

## Zadania, rozwiązania i pułapki

- Pliki bezpośrednio w `zadania_live_coding/` mogą zawierać sam opis lub szkielet
  zadania. `sqaure_game.py` jest ćwiczeniem z `NotImplementedError`;
  implementacja znajduje się w `solutions/sqaure_game.py`.
- W `solutions/` znajdują się rozwiązania. Testy regresyjne są w `tests/`;
  obejmują wyszukiwanie binarne, silnię, teleporty, odczyt plików i stan instancji.
- `jak_to_dziala/` zawiera celowe pułapki: mutowalny argument domyślny, późne
  wiązanie zmiennych w funkcjach, porównania `is` i `==` oraz współdzielony licznik
  wątków. Nie traktuj tych przykładów jako wzorców kodu produkcyjnego.
- `exceptions/custom_exception.py` i `utils/stringi.py` pokazują oczekiwane
  wyjątki i je przechwytują, aby można było uruchomić całą demonstrację.
- Wersje rekurencyjne silni mają limit głębokości rekurencji. Dla dużych danych
  używaj wersji iteracyjnej z `solutions/silnia.py`.

Ruff sprawdza błędy składni, niezdefiniowane nazwy i wybrane błędne konstrukcje.
Konfiguracja zachowuje celowe porównania literałów przez `is` w ćwiczeniu o typach.

## Dodawanie materiałów

W notatce podaj krótką odpowiedź rekrutacyjną, działający przykład, ograniczenia
oraz odnośnik do dokumentacji i wersję omawianej technologii. Dla nowego rozwiązania
algorytmicznego dopisz testy danych przykładowych i przypadków brzegowych.
Kod demonstracyjny w nowych i zmienianych modułach umieszczaj pod
`if __name__ == "__main__":`, aby import nie uruchamiał przykładu.
