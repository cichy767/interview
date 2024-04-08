CREATE TABLE creates a new table.
```
CREATE TABLE friends(
  id INTEGER,
  name TEXT,
  birthday DATE
)
```

INSERT INTO adds a new row to a table.
````
INSERT INTO friends (id, name, birthday) 
VALUES (1, 'Ororo Munroe', '1940-05-30');
````

SELECT queries data from a table.
````
SELECT * FROM friends;
````

ALTER TABLE changes an existing table.
````
ALTER TABLE friends
ADD COLUMN email TEXT;
````
UPDATE edits a row in a table.
````
UPDATE friends 
SET name = 'Ororo Storm'
WHERE id = 1;
````
DELETE FROM deletes rows from a table.
````
DELETE FROM friends WHERE id = 1;
````