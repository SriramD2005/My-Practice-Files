#include <stdio.h>
#define maxQsize 10
typedef struct process{
    int id;
};
typedef struct semaphore{
    int value;
    int front = -1, rear = -1;
    process* ps[];
}
void push(semaphore* s, process* p){
    if (semaphore->rear%maxQsize+1 == semaphore->front){
        printf("the queue is full\n");
    }
    else{
        semaphore->ps[semaphore->rear++];
    }
}
void wakeup(process* p){
    printf("the process woke up");
}