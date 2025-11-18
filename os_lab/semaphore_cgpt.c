#include <stdio.h>
#include <stdlib.h>

#define MAX_QUEUE_SIZE 10

typedef struct {
    int id;
} Process;

typedef struct {
    int value;
    Process* queue[MAX_QUEUE_SIZE];
    int front, rear, count;  // 'count' tracks number of elements
} Semaphore;

// Initialize semaphore and queue
void initSemaphore(Semaphore* s, int initialValue) {
    s->value = initialValue;
    s->front = s->rear = 0;  // Circular queue
    s->count = 0;
}

// Push process into circular queue
void push(Semaphore* s, Process* p) {
    if (s->count == MAX_QUEUE_SIZE) {
        printf("Queue is full, cannot add process.\n");
        return;
    }
    s->queue[s->rear] = p;
    s->rear = (s->rear + 1) % MAX_QUEUE_SIZE;  // Circular increment
    s->count++;
}

// Pop process from circular queue
Process* pop(Semaphore* s) {
    if (s->count == 0) {
        printf("Queue is empty.\n");
        return NULL;
    }
    Process* p = s->queue[s->front];
    s->front = (s->front + 1) % MAX_QUEUE_SIZE;  // Circular increment
    s->count--;
    return p;
}

// Simulate blocking a process
void block() {
    printf("Process blocked.\n");
}

// Simulate waking up a process
void wakeup(Process* p) {
    printf("Process %d waking up.\n", p->id);
}

// P operation (Down)
void P(Semaphore* s, Process* p) {
    s->value -= 1;
    if (s->value < 0) {
        push(s, p);
        block();
    }
}

// V operation (Up)
void V(Semaphore* s) {
    s->value += 1;
    if (s->value <= 0) {
        Process* p = pop(s);
        if (p) wakeup(p);
    }
}

// Example usage
int main() {
    Semaphore s;
    initSemaphore(&s, 1);

    Process p1 = {1}, p2 = {2}, p3 = {3};

    P(&s, &p1);
    P(&s, &p2);  // p2 gets blocked
    P(&s, &p3);  // p3 gets blocked
    V(&s);       // p1 releases, p2 wakes up
    V(&s);       // p2 releases, p3 wakes up
    V(&s);       // Final release

    return 0;
}