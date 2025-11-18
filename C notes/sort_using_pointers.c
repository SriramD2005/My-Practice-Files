#include <stdio.h>
void sort(int *,int);
int main(){
    int array[]={3,1,7,5};
    int *ar=array+0;
    sort(array,4);
    for(int i=0;i<4;i++){
        printf("%d",array[i]);
    }
}
void sort(int *arr,int n){
    for(int i=0;i<n;i++){
        for(int j=0;j<n-i-1;j++){
            if (*(arr+j)>*(arr+j+1)){
                int tmp=*(arr+j);
                *(arr+j)=*(arr+j+1);
                *(arr+j+1)=tmp;
            }
        }
    }
}