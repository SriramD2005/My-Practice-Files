#include <stdio.h>
#include <stdlib.h>

typedef struct process {
    int id;
    int wt;
    int tat;
    int bt;
    int rt; // remaining time
} process;

int main() {
    int pids[] = {1, 2, 3, 4, 5};
    int bts[] = {10, 4, 7, 3, 9};
    process p = {2, 4, 6, 78, 4};

    printf("Process ID: %d\n", p.id);

    return 0;
}