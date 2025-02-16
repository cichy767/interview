Najprościej mówiąc WHERE służy do filtrowania wierszy przed grupowaniem (agregowaniem), natomiast HAVING służy do filtrowania danych po grupowaniu bądź wyników funkcji agregujących.

```SQL
SELECT Name, AVG(high)
FROM dbo.Users
WHERE Name IS NOT NULL
GROUP BY Name
HAVING AVG(high) > 180;
```

Pozostałe różnice:
* Klauzula WHERE może być używana wraz z poleceniami SELECT, INSERT oraz UPDATE, natomiast HAVING jedynie z poleceniem SELECT
* W klauzuli WHERE nie można używać funkcji agregujących, w klauzuli HAVING można.

Ważne: W przypadku, gdy w zapytaniu nie użyto GROUP BY, HAVING ma takie samo zastosowanie jak WHERE









