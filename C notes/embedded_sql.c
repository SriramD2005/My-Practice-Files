#include <stdio.h>
#include <sqlca.h>  // SQL communication area

EXEC SQL INCLUDE sqlca;

int main() {
    EXEC SQL CONNECT TO myfirstdatabase USER 'root' USING 'sriram2005';

    EXEC SQL DECLARE cursor1 CURSOR FOR 
        SELECT name, mark FROM student WHERE mark > 80;

    EXEC SQL OPEN cursor1;

    char name[20];
    int mark;

    while (SQLCODE == 0) {
        EXEC SQL FETCH cursor1 INTO :name, :mark;
        printf("Name: %s, Mark: %d\n", name, mark);
    }

    EXEC SQL CLOSE cursor1;
    EXEC SQL COMMIT;
    
    return 0;
}