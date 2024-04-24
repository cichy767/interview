The ORDER BY keyword is used to sort the result in ascending or descending order.

The ORDER BY keyword sorts the records in ascending order by default. To sort the records in descending order, use the DESC keyword.

```SQL
SELECT * FROM products
ORDER BY price;
```
RESULT:
```commandline
 product_id |           product_name           | category_id |         unit         | price
------------+----------------------------------+-------------+----------------------+--------
         33 | Geitost                          |           4 | 500 g                |   2.50
         24 | Guarani Fantastica               |           1 | 12 - 355 ml cans     |   4.50
         13 | Konbu                            |           8 | 2 kg box             |   6.00
         52 | Filo Mix                         |           5 | 16 - 2 kg boxes      |   7.00
         54 | Tourtiare                        |           6 | 16 pies              |   7.45
         ...
```

```SQL
SELECT * FROM products
ORDER BY price DESC;
```

```SQL
SELECT * FROM products
ORDER BY product_name;
```

```SQL
SELECT * FROM products
ORDER BY product_name DESC;
```