#include <stdio.h>
int main(){
    int arr[]={5,2,2,1,3,4,5,3};
    int size=8;
    //to delete the duplicates from the array
    for (int i=0;i<size;i++){
        for(int j=i+1;j<size;){
           if(arr[i]==arr[j]){
             for (int k=j;k<size-1;k++) 
                arr[k]=arr[k+1];
            size--;
           }
           else j++;
        }            
    }
    for(int i=0;i<size;i++)printf("%d",arr[i]);
}