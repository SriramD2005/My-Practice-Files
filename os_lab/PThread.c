#include<stdio.h>
#include<pthread.h>
#define num_threads 5
#define num_iter 3
int counter = 0;
pthread_mutex_t lock;
void* printer(){
    for (int i = 0;i<num_iter;i++){
        counter++;
        printf("%d ",counter);
        
    }
    return NULL;
}
void* printer2(){
    printf("\n i increase the counter:%d",counter);
    return NULL;
}
int main(){
    int mutexstatus = pthread_mutex_init(&lock,NULL);
    pthread_t first;
    pthread_t second;
    pthread_mutex_lock(&lock);
    pthread_create(&first,NULL,printer,NULL);
    pthread_mutex_unlock(&lock);
    pthread_create(&second,NULL,printer2,NULL);
    pthread_join(second,NULL);
}