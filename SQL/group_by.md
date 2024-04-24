The GROUP BY clause groups rows that have the same values into summary rows, like "find the number of customers in each country".

The GROUP BY clause is often used with aggregate functions like COUNT(), MAX(), MIN(), SUM(), AVG() to group the result-set by one or more columns.

```SQL
SELECT COUNT(customer_id), country
FROM customers
GROUP BY country;
```

RESULT:
```commandline
 count |   country
-------+-------------
     3 | Argentina
     5 | Spain
     2 | Switzerland
     3 | Italy
     4 | Venezuela
     2 | Belgium
     1 | Norway
     2 | Sweden
...
(21 rows)
```


```SQL
SELECT customers.customer_name, COUNT(orders.order_id)
FROM orders
LEFT JOIN customers ON orders.customer_id = customers.customer_id
GROUP BY customer_name;
```

```commandline
           customer_name            | count
------------------------------------+-------
 Magazzini Alimentari Riuniti       |    10
 Wilman Kala                        |     8
 The Cracker Box                    |     3
 Wellington Importadora             |     9
 Furia Bacalhau e Frutos do Mar     |     8
 Lehmanns Marktstand                |    15
 Supremes delices                   |    12
 Godos Cocina Tipica                |    10
 Rattlesnake Canyon Grocery         |    18
 Toms Spezialiteten                 |     5
 Santa Gourmet                      |     6
 ...
```