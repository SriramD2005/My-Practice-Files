mysql> -- NATURAL JOIN
mysql> -- when you use natural join, the tables joined by using the same attributes of the both tables. if the table got multiple attributes same then it wi
ll filter the rows that has all the attributes same
mysql> use twelthPractice;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> select * from customer;
+------+----------------+------------+-------+------+
| Cid  | Cname          | city       | grade | Sid  |
+------+----------------+------------+-------+------+
| 3002 | Nick Rimando   | New York   |   100 | 5001 |
| 3007 | Brad Davis     | New York   |   200 | 5001 |
| 3005 | Graham Zusi    | California |   200 | 5002 |
| 3008 | Julian Green   | London     |   300 | 5002 |
| 3004 | Fabian Johnson | Paris      |   300 | 5006 |
| 3009 | Geoff Cameron  | Berlin     |   100 | 5003 |
| 3003 | Jozy Altidor   | Moscow     |   200 | 5007 |
| 3001 | Brad Guzan     | London     |  NULL | 5005 |
+------+----------------+------------+-------+------+
8 rows in set (0.00 sec)

mysql> select * from salesman;
+------+------------+----------+-----------+
| Sid  | Sname      | city     | commision |
+------+------------+----------+-----------+
| 5001 | James Hoog | New York |      0.15 |
| 5002 | Nail Knite | Paris    |      0.13 |
| 5005 | Pit Alex   | London   |      0.11 |
| 5006 | Mc Lyon    | Paris    |      0.14 |
| 5007 | Paul Adam  | Rome     |      0.13 |
| 5003 | Lauson Hen | San Jose |      0.12 |
+------+------------+----------+-----------+
6 rows in set (0.00 sec)

mysql> select Cname, Sname, city, Sid from salesman natural join customer;
+----------------+------------+----------+------+
| Cname          | Sname      | city     | Sid  |
+----------------+------------+----------+------+
| Nick Rimando   | James Hoog | New York | 5001 |
| Brad Davis     | James Hoog | New York | 5001 |
| Fabian Johnson | Mc Lyon    | Paris    | 5006 |
| Brad Guzan     | Pit Alex   | London   | 5005 |
+----------------+------------+----------+------+
4 rows in set (0.00 sec)
