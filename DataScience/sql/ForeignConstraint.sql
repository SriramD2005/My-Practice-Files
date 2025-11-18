 alter table orders add constraint constraintHolder foreign key (Sid) references salesman(Sid);
ERROR 1822 (HY000): Failed to add the foreign key constraint. Missing index for constraint 'constraintHolder' in the referenced table 'salesman'
-- we can only reference column of other table that has the primary key or unique constraint
mysql> alter table salesman add primary key(Sid);
Query OK, 0 rows affected (0.19 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> alter table orders add constraint constraintHolder foreign key (Sid) references salesman(Sid);
Query OK, 8 rows affected (0.22 sec)
Records: 8  Duplicates: 0  Warnings: 0
