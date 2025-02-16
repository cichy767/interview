# Jak przeprowadzić migracja bazy danych bez resetowania aplikacji?

Migracja bazy danych w aplikacjach działających 24/7 to kluczowe zadanie, które wymaga starannego planowania i minimalizowania przestojów. 
Taki proces można przeprowadzić w kilku krokach, dostosowanych do specyfiki migracji i wykorzystywanej technologii. 
Poniżej przedstawiamy ogólne zasady i metody umożliwiające migrację bez wpływu na działanie aplikacji.

1. Planowanie i Przygotowanie
Ocena i planowanie: Przeprowadź dokładną ocenę obecnej bazy danych, wersji, schematu, rozmiaru danych i wszelkich zależności. 
Zrozumienie tych elementów jest kluczowe do zaplanowania migracji.
Testowanie: Utwórz środowisko testowe odzwierciedlające produkcję, na którym będziesz mógł przetestować migrację. 
Umożliwi to identyfikację potencjalnych problemów bez wpływu na działanie produkcyjnej aplikacji.
Backup: Zawsze wykonuj pełny backup danych przed rozpoczęciem migracji, aby móc przywrócić stan poprzedni w razie problemów.


2. Backward compatibility. Trzeba sprawdzić które zmiany są bezpieczne, a które mogą zepsuć aplikacje. 
Niektóre zmiany w schemacie bazy danych mogą zepsuć aplikację. Aby tego uniknąć, warto przeprowadzać migrację w kilku etapach.

## Stopniowa zmiana schematu

Dodawanie nowych kolumn – najpierw dodaj nową kolumnę, a starej nie usuwaj od razu.

Modyfikacja danych – jeśli zmiana dotyczy np. typu danych, skonwertuj dane w kilku krokach.

Usunięcie kolumn – dopiero po upewnieniu się, że nowa struktura działa poprawnie i aplikacja już jej używa.

## Widoki i warstwy abstrakcji

Zamiast zmieniać tabelę bezpośrednio, można utworzyć widok (VIEW), który odwzorowuje dane w sposób zgodny ze starą strukturą.
Aplikacja korzysta wtedy z widoku zamiast bezpośrednio z tabeli, co pozwala na płynne przejście do nowej struktury.
