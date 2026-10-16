# WHERE a HAVING

`WHERE` filtruje pojedyncze wiersze przed grupowaniem, a `HAVING` filtruje grupy
po obliczeniu agregatów.

```sql
SELECT name, AVG(height)
FROM users
WHERE name IS NOT NULL
GROUP BY name
HAVING AVG(height) > 180;
```

- `WHERE` występuje w `SELECT`, `UPDATE` i `DELETE`. `INSERT ... SELECT` może
  korzystać z `WHERE` w części `SELECT`; `INSERT ... VALUES` nie ma własnego `WHERE`.
- W `WHERE` nie używamy agregatów obliczanych na tym samym poziomie zapytania.
  Możemy natomiast odwołać się do wyniku agregacji w podzapytaniu.
- W PostgreSQL `HAVING` bez `GROUP BY` nadal filtruje grupę: wszystkie wybrane
  wiersze traktowane są jako jedna grupa. Nie jest to odpowiednik `WHERE`.

```sql
SELECT COUNT(*) AS total
FROM users
HAVING COUNT(*) > 10;
```

Ostatnie zapytanie zwróci jeden wiersz z liczbą użytkowników, jeśli jest ich więcej
niż 10; w przeciwnym razie nie zwróci żadnego wiersza.

Źródło: [PostgreSQL — HAVING](https://www.postgresql.org/docs/current/sql-select.html#SQL-HAVING).
