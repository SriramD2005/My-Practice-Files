#include <stdio.h>
int binsearch(int ar[],int size,int x){
    int mid,first=0,last=size-1;
    while(first<last){
        mid=(first+last)/2;
        if(ar[mid]>x)last=mid;
        if (ar[mid]<x)first=mid+1;
        if (x==ar[mid])return mid+1;
    }
    return (int)NULL;
}
int main(){
    int arr[]={2,4,5,10,13};
    int x=binsearch(arr,5,1);
    printf("%d",x);
    return 0;
}