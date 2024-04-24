Rekurencja w Pythonie jest potężnym narzędziem, ale jej niewłaściwe użycie może prowadzić do problemów z wydajnością, czytelnością kodu oraz potencjalnych błędów. 
Oto kilka złych praktyk dotyczących użycia rekurencji w Pythonie, których należy unikać:

1. Brak Warunku Bazowego

Rekurencja wymaga warunku bazowego (przypadku podstawowego), który zatrzymuje rekursję. Pominięcie tego warunku może prowadzić do nieskończonej rekurencji i ostatecznie do przekroczenia maksymalnej głębokości rekursji (RecursionError).

2. Nadmierna Głębokość Rekursji

Python ma limit głębokości rekursji (domyślnie ustawiony na 1000). Rekurencyjne rozwiązania, które mogą przekroczyć ten limit, powinny być zastąpione przez iterację lub inne metody. Próby pracy z bardzo głęboką rekurencją mogą zakończyć się błędem przekroczenia maksymalnej głębokości rekursji.