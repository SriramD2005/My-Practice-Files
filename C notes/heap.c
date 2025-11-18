#include<stdio.h>
#include<stdlib.h>
void percup(int heap[],int i){
    int curr=i;
    while (curr>=0){
        int* parent=&heap[(int)((curr-1)/2)];
        if (*parent<heap[curr]){
            int temp=heap[curr];
            heap[curr]=*parent;
            *parent=temp;
        }
        else break;
        curr=(int)((curr-1)/2);
    }
}
void percdown(int heap[],int* length);
int popmax(int heap[],int* length){
    int max;
    if (length){
        max=heap[0];
    }
    else return -1;
    heap[0]=heap[--(*length)];
    percdown(heap,length);
}
void percdown(int heap[],int* length){
    int curr=0;
    while (curr<=*length-1){
        int* child1=&heap[(int) ((2*curr)+1)];
        int* child2=&heap[(int) ((2*curr)+2)];
        if ((2*curr+1)>*length-1){
            break;
        }
        if ((2*curr+2)<= *length-1){
            if (*child1<= *child2){
                int temp= *child2;
                *child2=heap[curr];
                heap[curr]=temp;
                curr=(int) ((2*curr)+2);
            }
            else{
                int temp=*child1;
                *child1=heap[curr];
                heap[curr]=temp;
                curr=(int) ((2*curr)+1);
            }
        }
        else{
            int temp=*child1;
            *child1=heap[curr];
            heap[curr]=temp;
            curr=(int) ((2*curr)+1);
        }
        
    }
}

int main()
{
    int size;
    scanf("%d",&size);
    int heap[size];
    for (int i=0;i<size;i++){
        scanf("%d" ,&heap[i]);
        percup(heap,i+1);
    }
    int* hlength;
    int l=size;
    hlength=&size;
    int n;
    scanf("%d",&n);
    for (int j=0;j<n;j++){
        printf("hey");
        printf("%d ",popmax(heap,hlength));
    }
}