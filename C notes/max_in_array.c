#include <stdio.h>
int findmax(int array[],int size){
    int max;
    for (int i=0;i<size;i++) if (max<array[i]) max=array[i];
    return max;
