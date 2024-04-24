
Migracja bazy danych bez resetowania aplikacji jest kluczowym zadaniem w przypadku aplikacji działających 24/7, 
które nie mogą sobie pozwolić na długie przerwy w dostępności. Taki proces wymaga starannego planowania i może obejmować kilka etapów, 
w zależności od specyfiki migracji i technologii. Oto ogólne kroki, które pomogą przeprowadzić migrację danych bez wprowadzania przerw w działaniu aplikacji:

1. Planowanie i Przygotowanie
Ocena i planowanie: Przeprowadź dokładną ocenę obecnej bazy danych, wersji, schematu, rozmiaru danych i wszelkich zależności. 
Zrozumienie tych elementów jest kluczowe do zaplanowania migracji.
Testowanie: Utwórz środowisko testowe odzwierciedlające produkcję, na którym będziesz mógł przetestować migrację. 
Umożliwi to identyfikację potencjalnych problemów bez wpływu na działanie produkcyjnej aplikacji.
Backup: Zawsze wykonuj pełny backup danych przed rozpoczęciem migracji, aby móc przywrócić stan poprzedni w razie problemów.
2. Backward compatibility. Trzeba sprawdzić które zmiany są bezpieczne, a które mogą zepsuć aplikacje. 
Jeśli mamy zmiany, które mogą sprawiać problemy to można zastanowić się nad przeprowadzeniem migracji w kilku krokach.
Np. dodanie nowej kolumny bez usuwania starej, a dopiero w kolejnym kroku usunięcie starej.
Możemy skorzystać z widoku który nakłada na korzystającą z bazy danych aplikacje warstwe abstrakcji. 
Aplikacja nie korzysta bezpośrednio ze schemy w bazie danych, tylko z widoku który możemy zmienić, żeby prezentował dane w ten sam sposób.
