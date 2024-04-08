Najprościej mówiąc WHERE służy do filtrowania wierszy przed grupowaniem (agregowaniem), natomiast HAVING służy do filtrowania danych po grupowaniu bądź wyników funkcji agregujących.

```SQL
SELECT Name, avg(high)
FROM dbo.Users
WHERE NAME IS NOT NULL
HAVING avg(high) > 180
```

Pozostałe różnice:
* Klauzula WHERE może być używana wraz z poleceniami SELECT, INSERT oraz UPDATE, natomiast HAVING jedynie z poleceniem SELECT
* W klauzuli WHERE nie można używać funkcji agregujących, w klauzuli HAVING można.

Ważne: W przypadku, gdy w kwerendzie nie użyto GROUP BY, HAVING ma takie samo zastosowanie jak WHERE









