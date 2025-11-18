 select * from orders;
+------+------+------+------------+-------------+
| Oid  | Cid  | Sid  | Odate      | totalamount |
+------+------+------+------------+-------------+
| 7001 | 3002 | 5001 | 2025-06-01 |         500 |
| 7002 | 3007 | 5001 | 2025-06-05 |         800 |
| 7003 | 3005 | 5002 | 2025-06-07 |         600 |
| 7004 | 3008 | 5002 | 2025-06-10 |        1200 |
| 7005 | 3004 | 5006 | 2025-06-15 |        1500 |
| 7006 | 3009 | 5003 | 2025-06-20 |         300 |
| 7007 | 3003 | 5007 | 2025-06-25 |        1000 |
| 7008 | 3001 | 5005 | 2025-06-28 |         900 |
+------+------+------+------------+-------------+
8 rows in set (0.00 sec)

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
8 rows in set (0.02 sec)

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
6 rows in set (0.02 sec)
-- to ⃣ Retrieve all orders along with customer and salesman details
mysql> select Oid, Sname, Cname from (salesman join customer using (Sid)) join orders using (Sid);
+------+------------+----------------+
| Oid  | Sname      | Cname          |
+------+------------+----------------+
| 7001 | James Hoog | Brad Davis     |
| 7001 | James Hoog | Nick Rimando   |
| 7002 | James Hoog | Brad Davis     |
| 7002 | James Hoog | Nick Rimando   |
| 7003 | Nail Knite | Julian Green   |
| 7003 | Nail Knite | Graham Zusi    |
| 7004 | Nail Knite | Julian Green   |
| 7004 | Nail Knite | Graham Zusi    |
| 7005 | Mc Lyon    | Fabian Johnson |
| 7006 | Lauson Hen | Geoff Cameron  |
| 7007 | Paul Adam  | Jozy Altidor   |
| 7008 | Pit Alex   | Brad Guzan     |
+------+------------+----------------+
12 rows in set (0.01 sec)
-- this is wrong
-- the right method is:
mysql> select Oid, Sname, Cname from (salesman join customer using (Sid)) join orders using (Cid);
+------+------------+----------------+
| Oid  | Sname      | Cname          |
+------+------------+----------------+
| 7001 | James Hoog | Nick Rimando   |
| 7002 | James Hoog | Brad Davis     |
| 7003 | Nail Knite | Graham Zusi    |
| 7004 | Nail Knite | Julian Green   |
| 7005 | Mc Lyon    | Fabian Johnson |
| 7006 | Lauson Hen | Geoff Cameron  |
| 7007 | Paul Adam  | Jozy Altidor   |
| 7008 | Pit Alex   | Brad Guzan     |
+------+------------+----------------+
-- - Customers who placed orders over ₹1000 and the salesmen who handled them
 select Cname, Sname, spent from (select Cid, sum(totalamount) as 'spent' from orders group by Cid having spent>1000) as o join customer c on o.Cid = c.Cid join salesman s on c.Sid = s.Sid;
+----------------+------------+-------+
| Cname          | Sname      | spent |
+----------------+------------+-------+
| Julian Green   | Nail Knite |  1200 |
| Fabian Johnson | Mc Lyon    |  1500 |
+----------------+------------+-------+
2 rows in set (0.00 sec)
-- Most recent order by each customer and who their salesman was:
mysql> select Cname, Sname, recent from (select Cid, min(Odate) as 'Recent' from orders group by Cid) as cal join customer c on c.Cid = cal.Cid join salesma
n s on c.Sid = s.Sid;
+----------------+------------+------------+
| Cname          | Sname      | recent     |
+----------------+------------+------------+
| Nick Rimando   | James Hoog | 2025-06-01 |
| Brad Davis     | James Hoog | 2025-06-05 |
| Graham Zusi    | Nail Knite | 2025-06-07 |
| Julian Green   | Nail Knite | 2025-06-10 |
| Fabian Johnson | Mc Lyon    | 2025-06-15 |
| Geoff Cameron  | Lauson Hen | 2025-06-20 |
| Jozy Altidor   | Paul Adam  | 2025-06-25 |
| Brad Guzan     | Pit Alex   | 2025-06-28 |
+----------------+------------+------------+

